import random
import unittest

from Core.gmssl import SM2_MAX_SIGNATURE_SIZE
from easy_sm2_sign_key import EasySM2SignKey, EasySM2VerifyKey


class MyTestCase(unittest.TestCase):
    def test_sign_data(self):
        signer_id = 'test_signer'
        print('signer_id hex:', signer_id.encode('utf-8').hex())
        test = EasySM2SignKey(signer_id = signer_id, pem_private_key_file = './test_keys/tmp_test_sm2_private.pem',
                              password = '123456')
        plain = bytes([random.randint(0, 255) for _ in range(0, 64)])
        print('plain hex:', plain.hex())
        print('private key hex:', test.get_sm2_private_key_in_hex())
        print('public key hex:', test.get_sm2_public_key_in_hex())
        test.UpdateData(plain)
        sign_value = test.GetSignValue()
        print('signature hex:', sign_value.hex())
        self.assertTrue(len(sign_value) <= SM2_MAX_SIGNATURE_SIZE)

        verify_test = EasySM2VerifyKey(signer_id = signer_id, pem_public_key_file = './test_keys/tmp_test_sm2_public.pem')
        print('verify public key:', verify_test.get_sm2_public_key_in_hex())
        verify_test.UpdateData(plain)
        ret = verify_test.VerifySignature(sign_value)
        self.assertTrue(ret is True)

    # def test_origin_sign_verify(self):
    #     sm2_key = gmssl.Sm2Key()
    #     sm2_key.generate_key()
    #     sign_key = Sm2Signature(sm2_key)
    #     plain = 'hello,world'.encode('utf-8')
    #     sign_key.update(plain)
    #     signature = sign_key.sign()
    #
    #     verify_key = Sm2Signature(sm2_key, sign = False)
    #     verify_key.update(plain)
    #     ret = verify_key.verify(signature)
    #     self.assertTrue(ret is True)


if __name__ == '__main__':
    unittest.main()
