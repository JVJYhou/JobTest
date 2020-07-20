from Add import *
import unittest


class AddTestCase(unittest.TestCase):
    def test_add(self):
        res=add(21412412412412412412,2312312312321312312312)
        self.assertEqual(res,2333724724733724724724)


if __name__ == '__main__':
    unittest.main()

