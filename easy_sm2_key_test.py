import unittest

from easy_sm2_key import EasySm2Key


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


if __name__ == '__main__':
    unittest.main()
