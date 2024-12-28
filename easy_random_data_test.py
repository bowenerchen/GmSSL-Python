import string
import unittest

from .easy_random_data import EasyRandomData, RandomMode


class MyTestCase(unittest.TestCase):
    def test_random_data(self):
        test = EasyRandomData()
        ret = test.GetRandomData(20)
        print(ret.hex())
        self.assertTrue(len(ret) == 20)

        test = EasyRandomData(mode = RandomMode.RandomStr)
        ret = test.GetRandomData(64)
        print(ret)
        for i in ret:
            self.assertTrue(i in list(string.ascii_letters + string.digits + string.printable + "'\"{}[]\\!@#$%^&*()_+|:"))

        try:
            test.GetRandomData(0)
        except Exception as e:
            print(e)
            self.assertTrue(True)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
