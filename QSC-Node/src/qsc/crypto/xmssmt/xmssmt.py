
import hashlib
import xmssmt_wrapper as xmssmt

from pyqrllib.pyqrllib import XmssFast, QRLHelper, QRLDescriptor

################################################################
_param_str = "XMSSMT-SHA2_20/4_256" #"XMSSMT-SHA2_20/2_256" 
_desc_bytes = b'\x10\x0a\x00' # NOTE: XMSSMT, SHA2-256, height=20

VERBOSE = False
##############################################################

class XMSSMT(object):
    def __init__(self, seed, height=20, hash_function=None):
        # Convert parameter string to OID
        try:
            oid = xmssmt.str_to_oid(_param_str)
            #if VERBOSE: print(f"OID for '{_param_str}': {oid}")
            self.params = xmssmt.XmssParams(oid)
            n = self.params.get_n()
            h_seed = hashlib.shake_256(bytes(seed)).digest(n*3) # 48 bytes to 32 bytes
            if VERBOSE: print(f'-> hashed seed: {h_seed}, length={len(h_seed)}')
            pk, sk = xmssmt.core_seed_keypair(self.params, h_seed)
            if VERBOSE: print(f'-> xmssmt-ref: pk size={len(pk)}, sk size={len(sk)}')
            # sk: index | sk_seed | sk_prf | root | pub_seed, 3 + 32 + 32 + 32 + 32 
            # pk: root | pub_seed, 32 + 32
            self.pk = _desc_bytes + pk
            self.sk = sk
            if VERBOSE: print(f'-> xmssmt: pk size={len(self.pk)}, sk size={len(self.sk)}')
            if VERBOSE: 
                print(f'-> pk={self.pk}')
                print(f'-> sk={self.sk}')

            self.seed = seed # NOTE: original seed uint8 tuple
            
        except ValueError as e:
            print(f"Error XMSSMT init: {e}")
            return


    def getDescriptor(self):
        return QRLDescriptor.fromBytes(_desc_bytes)

    def getHeight(self):
        return 20

    def getSK(self):
        return self.sk

    def getPK(self):
        return self.pk

    def getNumberSignatures(self):
        return 2 ** self.params.get_height()


    def getRemainingSignatures(self):
        ots_idx, rs = XMSSMT.get_ots_index_and_remaining_signatures(self.params, self.sk)
        return rs

    def getAddress(self):
        pk = self.getPK()
        if VERBOSE: print(f'-> pk={pk}, length={len(pk)}')
        return QRLHelper.getAddress(pk)

    def getIndex(self):
        ots_idx, rs = XMSSMT.get_ots_index_and_remaining_signatures(self.params, self.sk)
        return ots_idx

    def setIndex(self, new_index):

        """
        Set the OTS index in the secret key.

        Parameters:
            params (XmssParams): The XMSS parameters.
            sk (bytearray): The secret key as a mutable bytearray.
            new_index (int): The new OTS index to set.

        Raises:
            ValueError: If the new index is invalid.
        """
        self.sk = bytearray(self.sk)
        # Determine the number of bytes used for the index
        index_bytes = self.params.get_index_bytes()

        # Compute the maximum index (total number of signatures - 1)
        max_index = (2 ** self.params.get_height()) - 1

        # Extract the current index
        current_index = int.from_bytes(self.sk[:index_bytes], byteorder='big')

        # Validate the new index
        if new_index < current_index:
            raise ValueError("New index cannot be less than the current index to prevent OTS key reuse.")
        if new_index > max_index:
            raise ValueError(f"New index exceeds maximum index {max_index}.")

        # Convert the new index to bytes (big-endian)
        new_index_bytes = new_index.to_bytes(index_bytes, byteorder='big')

        # Update the index in the secret key
        self.sk[:index_bytes] = new_index_bytes
        

    def getExtendedSeed(self):
        pass

    def getSeed(self):
        return self.seed

    def sign(self, message: bytes):
        try:
            signature = xmssmt.core_sign(self.params, bytes(self.sk), bytes(message))
            if VERBOSE: print(f"Signature ({len(signature)} bytes): {signature.hex()}")
        except ValueError as e:
            print(f"Error signing message: {e}")
            return None
        
        return signature

    @staticmethod
    def validate_signature(message_hash, signature, pk):
        try:
            oid = xmssmt.str_to_oid(_param_str)
            if VERBOSE: print(f"OID for '{_param_str}': {oid}")
            params = xmssmt.XmssParams(oid)
            r_message = xmssmt.core_sign_open(params, pk, signature)
            if VERBOSE: 
                print(f"->Message hash: {bytes(message_hash)}")
                print(f"->Recovered message: {r_message}")
            if r_message == bytes(message_hash):
                return True
            else:
                return False
            
        except ValueError as e:
            print(f"Error verifying signature: {e}")
            return False
        

    @staticmethod
    def get_ots_index_and_remaining_signatures(params, sk):
        """
        Extract the OTS index from the secret key and compute remaining signatures.

        Parameters:
            params (XmssParams): The XMSS parameters.
            sk (bytes): The secret key.

        Returns:
            index (int): The current OTS index.
            remaining_signatures (int): The number of signatures remaining.
        """
        # Determine the number of bytes used for the index
        index_bytes = params.get_index_bytes()

        # Extract the index bytes from the secret key
        index_bytes_value = sk[:index_bytes]

        # Convert the bytes to an integer (assuming big-endian)
        index = int.from_bytes(index_bytes_value, byteorder='big')

        # Compute the total number of signatures
        total_signatures = 2 ** params.get_height()

        # Compute the number of remaining signatures
        remaining_signatures = total_signatures - index

        return index, remaining_signatures

