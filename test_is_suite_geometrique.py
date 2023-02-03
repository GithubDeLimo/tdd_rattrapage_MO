import is_suite_geometrique
import unittest


class TestEx1(unittest.TestCase):

    def test_is_suite_geometrique(self):
        self.assertEqual(is_suite_geometrique.is_suite_geometrique([2, 4, 8, 16]), True)
        self.assertEqual(is_suite_geometrique.is_suite_geometrique([1.1, 3.3, 9.9, 29.7, 89.1]), True)
        self.assertEqual(is_suite_geometrique.is_suite_geometrique([2, 6, 10, 14]), False)
        self.assertEqual(is_suite_geometrique.is_suite_geometrique([0, 0, 0, 0]), False)


if __name__ == '__main__':
    unittest.main()