import unittest

from easy_gmssl.easy_sm4_key import EasySm4CBC, EasySm4GCM

from gmssl import SM4_BLOCK_SIZE, SM4_CBC_IV_SIZE, SM4_GCM_DEFAULT_TAG_SIZE, Sm4Cbc


class MyTestCase(unittest.TestCase):
    def test_sm4_cbc(self):
        key = 'x' * SM4_BLOCK_SIZE
        iv = 'y' * SM4_CBC_IV_SIZE
        test_enc = Sm4Cbc(key.encode('utf-8'), iv.encode('utf-8'), True)
        plain1 = 'hello,world'
        plain2 = '1234567890'
        cipher1 = test_enc.update(plain1.encode('utf-8'))
        cipher2 = test_enc.update(plain2.encode('utf-8'))
        ciphers = cipher1 + cipher2 + test_enc.finish()
        self.assertTrue(len(ciphers) % SM4_BLOCK_SIZE == 0)

        test_dec = Sm4Cbc(key.encode('utf-8'), iv.encode('utf-8'), False)
        decrypted_plain1 = test_dec.update(ciphers)
        decrypted_plain = decrypted_plain1 + test_dec.finish()
        self.assertEqual(decrypted_plain, (plain1 + plain2).encode('utf-8'))

    def test_sm4_cbc_invalid_key_len(self):
        key = 'x' * (SM4_BLOCK_SIZE - 1)
        iv = 'y' * SM4_CBC_IV_SIZE
        try:
            test_enc = Sm4Cbc(key.encode('utf-8'), iv.encode('utf-8'), True)
        except Exception as e:
            print(e)
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_sm4_cbc_invalid_iv_len(self):
        key = 'x' * SM4_BLOCK_SIZE
        iv = 'y' * (SM4_CBC_IV_SIZE - 1)
        try:
            test_enc = Sm4Cbc(key.encode('utf-8'), iv.encode('utf-8'), True)
        except Exception as e:
            print(e)
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_easy_sm4_cbc(self):
        key = 'x' * SM4_BLOCK_SIZE
        iv = 'y' * SM4_CBC_IV_SIZE
        test_cbc_enc = EasySm4CBC(key.encode('utf-8'), iv.encode('utf-8'), True)
        plain1 = 'hello,world'
        plain2 = '1234567890'
        cipher1 = test_cbc_enc.Update(plain1.encode('utf-8'))
        cipher2 = test_cbc_enc.Update(plain2.encode('utf-8'))
        ciphers = cipher1 + cipher2 + test_cbc_enc.Finish()
        self.assertTrue(len(ciphers) % SM4_BLOCK_SIZE == 0)
        print('ciphers len:', len(ciphers))

        test_dec = EasySm4CBC(key.encode('utf-8'), iv.encode('utf-8'), False)
        decrypted_plain1 = test_dec.Update(ciphers)
        decrypted_plain = decrypted_plain1 + test_dec.Finish()
        self.assertEqual(decrypted_plain, (plain1 + plain2).encode('utf-8'))

    def test_easy_sm4_gcm(self):
        key = 'x' * SM4_BLOCK_SIZE
        iv = 'y' * SM4_CBC_IV_SIZE
        aad = 'a' * (SM4_BLOCK_SIZE + SM4_CBC_IV_SIZE)
        tag_len = int(SM4_GCM_DEFAULT_TAG_SIZE / 2)
        test_gcm_enc = EasySm4GCM(key.encode('utf-8'), iv.encode('utf-8'), aad, tag_len, True)
        plain1 = 'hello,world'
        plain2 = '1234567890'
        cipher1 = test_gcm_enc.Update(plain1.encode('utf-8'))
        cipher2 = test_gcm_enc.Update(plain2.encode('utf-8'))
        ciphers = cipher1 + cipher2 + test_gcm_enc.Finish()
        # GCM模式下的密文长度与明文长度等长
        # 返回的密文中包含了 tag 长度
        self.assertTrue((len(ciphers) - tag_len) == len(plain1 + plain2))
        print('ciphers len:', len(ciphers), 'tag_len=', tag_len, 'plain len:', len(plain1 + plain2))

        test_dec = EasySm4GCM(key.encode('utf-8'), iv.encode('utf-8'), aad, tag_len, False)
        decrypted_plain1 = test_dec.Update(ciphers)
        decrypted_plain = decrypted_plain1 + test_dec.Finish()
        self.assertEqual(decrypted_plain, (plain1 + plain2).encode('utf-8'))


if __name__ == '__main__':
    unittest.main()
