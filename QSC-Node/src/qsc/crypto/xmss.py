# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from pyqrllib import pyqrllib
from pyqrllib.pyqrllib import bin2hstr, getRandomSeed, str2bin, bin2mnemonic, mnemonic2bin  # noqa
from pyqrllib.pyqrllib import XmssFast, QRLDescriptor

from .xmssmt.xmssmt import XMSSMT

######################################################################################################
WITH_XMSSMT = True


##################################################################################################
hash_functions = {
    "shake128": pyqrllib.SHAKE_128,
    "shake256": pyqrllib.SHAKE_256,
    "sha2_256": pyqrllib.SHA2_256
}
hash_functions_reverse = {v: k for k, v in hash_functions.items()}



class XMSS(object):
    @staticmethod
    def from_extended_seed(extended_seed: bytes):
        if len(extended_seed) != 51:
            raise Exception('Extended seed should be 51 bytes long')

        descr = QRLDescriptor.fromBytes(extended_seed[0:3])
        if descr.getSignatureType() != pyqrllib.XMSS:
            raise Exception('Signature type nor supported')

        height = descr.getHeight()
        hash_function = descr.getHashFunction()
        tmp = XmssFast(extended_seed[3:], height, hash_function)
        return XMSS(tmp)

    @staticmethod
    def from_height(tree_height: int, hash_function="shake128"):
        if hash_function not in hash_functions:
            raise Exception("XMSS does not support this hash function!")

        seed = getRandomSeed(48, '')
        return XMSS(XmssFast(seed, tree_height, hash_functions[hash_function]))

    def __init__(self, _xmssfast):
        """
        :param
        tree_height: height of the tree to generate. number of OTS keypairs=2**tree_height
        :param _xmssfast:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.height
        4

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp._xmss.getSignatureSize()
        2308

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp._xmss.getPK() )
        '000200eb0372d56b886645e7c036b480be95ed97bc431b4e828befd4162bf432858df83191da3442686282b3d5160f25cf162a517fd2131f83fbf2698a58f9c46afc5d'

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> len( tmp._xmss.getPK() )
        67

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp._xmss.getSK() ) == xmss_sk_expected1
        True

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp._xmss.getRoot() )
        'eb0372d56b886645e7c036b480be95ed97bc431b4e828befd4162bf432858df8'

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp._xmss.getPKSeed() )
        '3191da3442686282b3d5160f25cf162a517fd2131f83fbf2698a58f9c46afc5d'

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp._xmss.getIndex()
        0

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp._xmss.getSKSeed() )
        'eda313c95591a023a5b37f361c07a5753a92d3d0427459f34c7895d727d62816'

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp._xmss.getSKPRF() )
        'b3aa2224eb9d823127d4f9f8a30fd7a1a02c6483d9c0f1fd41957b9ae4dfc63a'

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr(tmp._xmss.getAddress())
        '00020096e5c065cf961565169e795803c1e60f521af7a3ea0326b42aa40c0e75390e5d8f4336de'
        """
        self._xmss = _xmssfast

        if WITH_XMSSMT:
            print(f'-> XMSSMT_v1 is used!')
            self._xmssmt = XMSSMT(self._xmss.getSeed())

        

    @property
    def hash_function(self) -> str:
        descr = self._xmss.getDescriptor()
        function_num = descr.getHashFunction()
        function_name = hash_functions_reverse[function_num]
        if not function_name:
            raise Exception("Could not reverse-lookup the hash function")

        return function_name

    @property
    def signature_type(self):
        descr = self._xmss.getDescriptor()
        answer = descr.getSignatureType()
        return answer

    @property
    def height(self):
        return self._xmss.getHeight()

    @property
    def _sk(self):
        """
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> len(tmp._sk)
        132

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr(tmp._sk) == xmss_sk_expected1
        True

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed2)
        >>> bin2hstr(tmp._sk) == xmss_sk_expected2
        True
        """
        return bytes(self._xmss.getSK()) if not WITH_XMSSMT else bytes(self._xmssmt.getSK())

    @property
    def pk(self):
        """
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr(tmp.pk) == xmss_pk_expected1
        True
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr(tmp.pk) == xmss_pk_expected2
        True
        """
        # after the signature, the OTS_index will be increased; if it is >= 2**height (remaining_signatures==0), avoid exception with dual xmss!
        if self.remaining_signatures == 1:
            # TODO: warn the user?
            pass
            
        return bytes(self._xmss.getPK()) if not WITH_XMSSMT else bytes(self._xmssmt.getPK())

    @property
    def number_signatures(self) -> int:
        """
        Returns the number of signatures in the XMSS tree
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.number_signatures
        16
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.number_signatures
        16
        """
        return self._xmss.getNumberSignatures() if not WITH_XMSSMT else self._xmssmt.getNumberSignatures()

    @property
    def remaining_signatures(self):
        """
        Returns the number of remaining signatures in the XMSS tree
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.remaining_signatures
        16
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.remaining_signatures
        16
        """
        return self._xmss.getRemainingSignatures() if not WITH_XMSSMT else self._xmssmt.getRemainingSignatures()

    @property
    def mnemonic(self) -> str:
        """
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(hstr2bin(xmss_mnemonic_eseed1))
        >>> tmp.mnemonic == xmss_mnemonic_test1
        True
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(hstr2bin(xmss_mnemonic_eseed2))
        >>> tmp.mnemonic == xmss_mnemonic_test2
        True
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(mnemonic2bin(xmss_mnemonic_test1))
        >>> tmp.mnemonic == xmss_mnemonic_test1
        True
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(mnemonic2bin(xmss_mnemonic_test2))
        >>> tmp.mnemonic == xmss_mnemonic_test2
        True
        """
        return bin2mnemonic(self._xmss.getExtendedSeed())

    @property
    def address(self) -> bytes:
        return bytes(self._xmss.getAddress()) if not WITH_XMSSMT else bytes(self._xmssmt.getAddress())

    @property
    def qaddress(self) -> str:
        return 'q' + bin2hstr(self.address)

    @property
    def ots_index(self) -> int:
        """
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.ots_index
        0
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.ots_index
        0
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> s = tmp.sign(str2bin("test"))
        >>> tmp.ots_index
        1
        """
        return self._xmss.getIndex() if not WITH_XMSSMT else self._xmssmt.getIndex()

    def set_ots_index(self, new_index):
        """
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> xmss = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> xmss.set_ots_index(1)
        >>> xmss.ots_index
        1
        >>> from qsc.crypto.doctest_data import *
        >>> xmss = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> xmss.set_ots_index(10)
        >>> xmss.ots_index
        10
        """

        self._xmss.setIndex(new_index) if not WITH_XMSSMT else self._xmssmt.setIndex(new_index)
        
    @property
    def hexseed(self) -> str:
        """
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> tmp.hexseed
        '000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed2)
        >>> tmp.hexseed
        '000200010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101'
        """
        return bin2hstr(self._xmss.getExtendedSeed())

    @property
    def extended_seed(self):
        """
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp.seed )
        '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed2)
        >>> bin2hstr( tmp.extended_seed )
        '000200010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101'
        """
        return self._xmss.getExtendedSeed() 

    @property
    def seed(self):
        """
        :return:
        :rtype:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr( tmp.seed )
        '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed2)
        >>> bin2hstr( tmp.seed )
        '010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101'
        """
        return self._xmss.getSeed()

    def sign(self, message: bytes) -> bytes:
        """
        :param message:
        :return:

        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed1)
        >>> bin2hstr(tmp.sign(str2bin("test_message"))) == xmss_sign_expected1
        True
        >>> from qsc.crypto.doctest_data import *
        >>> tmp = XMSS.from_extended_seed(xmss_test_eseed2)
        >>> bin2hstr(tmp.sign(str2bin("test_message"))) == xmss_sign_expected2
        True
        """
        
        return bytes(self._xmss.sign(message)) if not WITH_XMSSMT else bytes(self._xmssmt.sign(message))

    @staticmethod
    def get_height_from_sig_size(sig_size: int) -> int:
        min_size = 4 + 32 + 67 * 32

        if sig_size < min_size:
            raise Exception("Invalid Signature Size")

        if (sig_size - 4) % 32 != 0:
            raise Exception("Invalid Signature Size")

        height = (sig_size - min_size) // 32

        return height

    @staticmethod
    def validate_signature(message_hash, signature, PK):
        if not WITH_XMSSMT:
            return XmssFast.verify(message_hash, signature, PK)
        else:
            return XMSSMT.validate_signature(message_hash, signature, PK[3:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
