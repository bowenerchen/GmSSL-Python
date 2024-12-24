import random
import unittest

from easy_gmssl.easy_sm3_key import EasySM3Digest, EasySM3Hmac

from gmssl import SM3_DIGEST_SIZE, SM3_HMAC_MAX_KEY_SIZE, SM3_HMAC_MIN_KEY_SIZE, SM3_HMAC_SIZE


class MyTestCase(unittest.TestCase):
    def test_sm3_hash(self):
        test = EasySM3Digest()
        plain1 = 'hello,world'.encode('utf-8')
        plain2 = '1234567890'.encode('utf-8')
        test.UpdateData(plain1)
        test.UpdateData(plain2)
        hash_value, _, length = test.GetHash()
        print(hash_value.hex(), length)
        self.assertTrue(length == len(plain1) + len(plain2))
        self.assertTrue(len(hash_value) == SM3_DIGEST_SIZE)

        test.Reset()
        plain3 = (plain1 + plain2)
        print('plain hex:', plain3.hex())
        test.UpdateData(plain3)
        hash_value_2, hash_len, length2 = test.GetHash()
        print('hash value:', hash_value_2.hex())
        print('hash value length in bytes:', hash_len)
        self.assertTrue(length2 == len(plain1) + len(plain2))
        self.assertTrue(hash_len == SM3_DIGEST_SIZE)
        self.assertTrue(len(hash_value_2) == SM3_DIGEST_SIZE)
        self.assertTrue(hash_value_2 == hash_value)

    def test_sm3_hmac_key(self):
        lt_min_key_size = bytes([random.randint(0, 255) for _ in range(0, SM3_HMAC_MIN_KEY_SIZE - 1)])
        print('lt_min_key_size', len(lt_min_key_size))
        gt_max_key_size = bytes([random.randint(0, 255) for _ in range(0, SM3_HMAC_MAX_KEY_SIZE + 1)])
        print('gt_max_key_size', len(gt_max_key_size))
        eq_min_key_size = bytes([random.randint(0, 255) for _ in range(0, SM3_HMAC_MIN_KEY_SIZE)])
        print('eq_min_key_size', len(eq_min_key_size))
        eq_max_key_size = bytes([random.randint(0, 255) for _ in range(0, SM3_HMAC_MAX_KEY_SIZE)])
        print('eq_max_key_size', len(eq_max_key_size))

        try:
            EasySM3Hmac(lt_min_key_size)
        except Exception as e:
            self.assertTrue(True)
            print(e)

        try:
            EasySM3Hmac(gt_max_key_size)
        except Exception as e:
            self.assertTrue(True)
            print(e)

        try:
            EasySM3Hmac(eq_min_key_size)
            EasySM3Hmac(eq_max_key_size)
        except Exception:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_sm3_hmac_value(self):
        plain = 'hello,world'.encode('utf-8')
        print('plain hex:', plain.hex())
        key = bytes([random.randint(0, 255) for _ in range(0, SM3_HMAC_MAX_KEY_SIZE)])
        print('key hex:', key.hex())
        test = EasySM3Hmac(key)
        test.UpdateData(plain)
        hmac_hex, hmac_len, plain_len = test.GetHmac()
        print('hmac value:', hmac_hex.hex(), 'hmac len:', hmac_len, 'plain len:', plain_len)
        self.assertTrue(hmac_len == SM3_HMAC_SIZE)
        self.assertTrue(len(plain) == plain_len)


if __name__ == '__main__':
    unittest.main()
