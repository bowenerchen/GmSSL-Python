import unittest

from easy_gmssl.easy_zuc import EasyZuc

from easy_random_data import EasyRandomData
from gmssl import ZUC_IV_SIZE, ZUC_KEY_SIZE


class MyTestCase(unittest.TestCase):
    def test_zuc(self):
        key = EasyRandomData().GetRandomData(ZUC_KEY_SIZE)
        iv = EasyRandomData().GetRandomData(ZUC_IV_SIZE)
        test = EasyZuc(key, iv)
        plain1 = 'hello,world'.encode('utf-8')
        cipher1 = test.Update(plain1)
        plain2 = '1234567890'.encode('utf-8')
        cipher2 = test.Update(plain2)
        cipher3 = test.Finish()

        self.assertTrue(len(cipher1 + cipher2 + cipher3) == len(plain1 + plain2))

        test2 = EasyZuc(key, iv)
        ret1 = test2.Update(cipher1)
        ret2 = test2.Update(cipher2)
        ret3 = test2.Update(cipher3)
        ret4 = test2.Finish()

        self.assertTrue(ret1 + ret2 + ret3 + ret4 == plain1 + plain2)


if __name__ == '__main__':
    unittest.main()
