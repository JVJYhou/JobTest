from multiplying import *
import unittest


class MultiplyingTestCase(unittest.TestCase):
    def test_multi(self):
        res=multiply(str(2131231231),str(123123123))
        self.assertEqual(res,262403844995854413)


if __name__ == '__main__':
    unittest.main()

