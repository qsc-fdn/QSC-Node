# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from unittest import TestCase

from pyqrllib import pyqrllib
from pyqrllib.pyqrllib import str2bin, XmssFast, bin2hstr, SHAKE_128, SHAKE_256, SHA2_256

from qsc.core.misc import logger
from qsc.crypto.xmss import XMSS

from qsc.core.txs.TransferTransaction import TransferTransaction

#import oqs
import platform  # to learn the OS we're on
import random
########################################################################################################




#######################################################################################################
logger.initialize_default()

def get_alice_xmss(xmss_height=6) -> XMSS:
    seed = bytes([i for i in range(48)])
    return XMSS(XmssFast(seed, xmss_height))


def get_bob_xmss(xmss_height=6) -> XMSS:
    seed = bytes([i + 5 for i in range(48)])
    return XMSS(XmssFast(seed, xmss_height))

if platform.system() == "Windows":
    disabled_sig_patterns = ["Rainbow-V"]
    
def check_correctness(alg_name):
    with oqs.Signature(alg_name) as sig:
        print(f'-> algo name: {alg_name}')
        message = bytes(random.getrandbits(8) for _ in range(100))
        pk = sig.generate_keypair()
        sk = sig.export_secret_key()
        print(f'-> pk={bin2hstr(pk)}')
        print(f'-> sk={bin2hstr(sk)}')
        signature = sig.sign(message)
        
        #assert XmssFast.verify(message, signature, pk), 'failed verified by XmssFast!'
        
        assert sig.verify(message, signature, pk)
        
def test_not_enabled():
    # TODO: test broken as the compiled lib determines which algorithms are supported and enabled
    for alg_name in oqs.get_supported_sig_mechanisms():
        print(f'-> algo name: {alg_name}')
        if alg_name not in oqs.get_enabled_sig_mechanisms():
            # Found a non-enabled but supported alg
            try:
                with oqs.Signature(alg_name) as sig:
                    raise AssertionError("oqs.MechanismNotEnabledError was not raised.")
            except oqs.MechanismNotEnabledError:
                pass
            except Exception as ex:
                raise AssertionError("An unexpected exception was raised. " + ex)
            
def test_correctness():
    for alg_name in oqs.get_enabled_sig_mechanisms():
        #if any(item in alg_name for item in disabled_sig_patterns):
        #    continue
        check_correctness(alg_name)
            
def get_ots_from_signature(signature):
    try:
        return int(bin2hstr(signature)[0:8], 16)
    except ValueError:
        raise ValueError('OTS Key Index: First 4 bytes of signature are invalid')

class TestXMSS2(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestXMSS2, self).__init__(*args, **kwargs)

    def test_sign_verify(self):
        message = "This is a test"
        message_bin = str2bin(message)

        xmss_height = 8
        seed = bytearray([i for i in range(48)])
        xmss = XMSS(XmssFast(seed, xmss_height))

        SIDX = 1
        xmss.set_ots_index(SIDX)

        for i in range(260):
            print(f'-> OTS index: {xmss.ots_index}, remaining: {xmss.remaining_signatures}, PK: {bin2hstr(xmss.pk)}, address: {bin2hstr(xmss.address)}')
            print(f'-> SK: {bin2hstr(xmss._sk)}')
            print(f'-> seed: {xmss.hexseed}')
            #self.assertTrue(xmss.ots_index == SIDX + i)
            signature = xmss.sign(message_bin)
            ots_key = get_ots_from_signature(signature)
            print(f'-> OTS key: {ots_key}, XMSS height: {xmss.height}, pk: {bin2hstr(xmss.pk)}, address: {bin2hstr(xmss.address)}')
            self.assertTrue(XmssFast.verify(message_bin, signature, xmss.pk))
            
            '''
            with oqs.Signature('Falcon-512', xmss._sk) as sig:
                pk2 = sig.generate_keypair()
                message2 = message.encode()
                signature2 = sig.sign(message2)
                assert sig.verify(message2, signature2, pk2), 'failed by ops'
                print(f'-> pk2: {bin2hstr(pk2)}')
            '''
    def test_tx(self):
        self.alice = get_alice_xmss()
        self.bob = get_bob_xmss()
    
        for i in range(200):
            print(f'-> Tx: {i}')
            tx = TransferTransaction.create(
                addrs_to=[self.bob.address],
                amounts=[100],
                message_data=None,
                fee=1,
                xmss_pk=self.alice.pk
            )
            tx.sign(self.alice)
            self.assertTrue(tx.validate_or_raise())

        ''''
        tx._data.transaction_hash = b'abc'
        # Should fail, as we have modified with invalid transaction_hash
        with self.assertRaises(ValueError):
            tx.validate_or_raise()
        '''

def benchmark():
    import time

    seed = bytearray([i for i in range(48)])
    for i in range(5):
        h = i * 2 + 8
        st = time.time()
        xmss = XMSS(XmssFast(seed, h, pyqrllib.SHAKE_256))
        print(f'Height: {h}, Time: {time.time() - st}')
            
if __name__  == '__main__':
    benchmark()
    exit()

    #test_correctness()
    #exit()
    
    #test_not_enabled()
    #exit()
    
    tester = TestXMSS2()
    #tester.test_sign_verify()
    tester.test_tx()
        