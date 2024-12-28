import base64
import random
import unittest

from .easy_sm2_key import EasySm2EncryptionKey, EasySm2Key, SM2CipherFormat, SM2CipherMode
from .gmssl import SM2_MAX_CIPHERTEXT_SIZE, SM2_MAX_PLAINTEXT_SIZE


class SM2KeyCase(unittest.TestCase):
    def test_new_sm2_key(self):
        test1 = EasySm2Key()
        self.assertTrue(test1.get_sm2_public_key_in_hex() != '')
        self.assertTrue(test1.get_sm2_private_key_in_hex() != '')
        self.assertTrue('X' in test1.get_point_in_hex().keys())
        self.assertTrue(test1.get_point_in_hex()['X'] != '')
        self.assertTrue('Y' in test1.get_point_in_hex().keys())
        self.assertTrue(test1.get_point_in_hex()['Y'] != '')

        test1_pub_key = test1.get_sm2_public_key_in_hex()
        test1_pri_key = test1.get_sm2_private_key_in_hex()

        # 重新生成密钥
        test1.reset_key()
        test1.new_key()
        self.assertTrue(test1.get_sm2_public_key_in_hex() != '')
        self.assertTrue(test1.get_sm2_private_key_in_hex() != '')
        self.assertTrue(test1.get_sm2_public_key_in_hex() != test1_pub_key)
        self.assertTrue(test1.get_sm2_private_key_in_hex() != test1_pri_key)

    def test_key_export(self):
        test = EasySm2Key()
        self.assertTrue(test.get_sm2_public_key_in_hex() != '')
        self.assertTrue(test.get_sm2_private_key_in_hex() != '')
        pub_key = test.get_sm2_public_key_in_hex()
        pri_key = test.get_sm2_private_key_in_hex()

        # 先导出密钥对
        test.export_to_pem_file('./test_keys/tmp_test', '123456')

        # 重新导入公钥，此时私钥数据为空
        test.load_sm2_pub_key('./test_keys/tmp_test_sm2_public.pem')
        self.assertTrue(test.get_sm2_public_key_in_hex() == pub_key)
        self.assertTrue(test.get_sm2_private_key_in_hex() == '')

        # 重新导入私钥，此时公钥、私钥数据均不为空
        test.load_sm2_private_key('./test_keys/tmp_test_sm2_private.pem', '123456')
        self.assertTrue(test.get_sm2_public_key_in_hex() == pub_key)
        self.assertTrue(test.get_sm2_private_key_in_hex() == pri_key)

        test.load_sm2_pub_key('./test_keys/kms_sm2.pem')
        self.assertFalse(test.get_sm2_public_key_in_hex() == pub_key)

    def test_key_import(self):
        test = EasySm2Key()
        self.assertTrue(test.get_sm2_public_key_in_hex() != '')
        self.assertTrue(test.get_sm2_private_key_in_hex() != '')

        try:
            test.load_sm2_pub_key('./test_keys/invalid_pub_key.pem')
        except Exception as e:
            print(e)
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        try:
            # 密码为空
            print('密码为空')
            test.load_sm2_private_key('./test_keys/tmp_test_sm2_private.pem', '')
        except Exception as e:
            print(e)
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        try:
            # 密码错误
            print('密码错误')
            test.load_sm2_private_key('./test_keys/tmp_test_sm2_private.pem', '1' * 32)
        except Exception as e:
            print(e)
            self.assertTrue(True)
        else:
            self.assertTrue(False)

        try:
            # 密码过长
            print('密码过长')
            test.load_sm2_private_key('./test_keys/tmp_test_sm2_private.pem', '1' * 33)
        except Exception as e:
            print(e)
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_valid_encrypt_decrypt(self):
        test = EasySm2EncryptionKey()
        plain_valid = bytes([random.randint(1, 255) for _ in range(0, SM2_MAX_PLAINTEXT_SIZE)])
        for mode in SM2CipherMode:
            cipher = test.Encrypt(plain_data = plain_valid, cipher_mode = mode, cipher_format = SM2CipherFormat.Base64Str)
            decrypted_plain = test.Decrypt(cipher_data = base64.b64decode(cipher), cipher_mode = mode)
            self.assertTrue(decrypted_plain == plain_valid)

    def test_encrypt_too_long_plain(self):
        test = EasySm2EncryptionKey()
        plain_valid = bytes([random.randint(1, 255) for _ in range(0, SM2_MAX_PLAINTEXT_SIZE + 1)])
        try:
            test.Encrypt(plain_data = plain_valid)
        except Exception as e:
            self.assertTrue(True)
            print(e)
        else:
            self.assertTrue(False)

    def test_decrypt_too_long_cipher(self):
        test = EasySm2EncryptionKey()
        cipher_invalid = bytes([random.randint(1, 255) for _ in range(0, SM2_MAX_CIPHERTEXT_SIZE + 1)])
        try:
            test.Decrypt(cipher_data = cipher_invalid)
        except Exception as e:
            self.assertTrue(True)
            print(e)
        else:
            self.assertTrue(False)

    def test_invalid_cipher_mode(self):
        test = EasySm2EncryptionKey()
        plain_valid = bytes([random.randint(1, 255) for _ in range(0, SM2_MAX_PLAINTEXT_SIZE)])
        try:
            test.Encrypt(plain_data = plain_valid, cipher_mode = 'abc')
        except Exception as e:
            self.assertTrue(True)
            print(e)
        else:
            self.assertTrue(False)

    def test_invalid_cipher_format(self):
        test = EasySm2EncryptionKey()
        plain_valid = bytes([random.randint(1, 255) for _ in range(0, SM2_MAX_PLAINTEXT_SIZE)])
        try:
            test.Encrypt(plain_data = plain_valid, cipher_format = 'abc')
        except Exception as e:
            self.assertTrue(True)
            print(e)
        else:
            self.assertTrue(False)

    def test_has_no_private_key(self):
        test = EasySm2EncryptionKey()
        test.load_sm2_pub_key('./test_keys/tmp_test_sm2_public.pem')
        cipher_invalid = bytes([random.randint(1, 255) for _ in range(0, SM2_MAX_CIPHERTEXT_SIZE)])
        try:
            test.Decrypt(cipher_data = cipher_invalid)
        except Exception as e:
            self.assertTrue(True)
            print(e)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
