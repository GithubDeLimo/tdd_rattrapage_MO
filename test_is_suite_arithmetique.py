import is_suite_arithmetique
import unittest


class TestEx1(unittest.TestCase):

    def test_is_suite_arithmetique(self):
        self.assertEqual(is_suite_arithmetique.is_suite_arithmetique([2, 4, 6, 8]), True)
        self.assertEqual(is_suite_arithmetique.is_suite_arithmetique([5, 5, 5, 5]), True)
        self.assertEqual(is_suite_arithmetique.is_suite_arithmetique([3, 1, -1, -3]), True)
        self.assertEqual(is_suite_arithmetique.is_suite_arithmetique([0, 6, 3, 9]), False)
        self.assertEqual(is_suite_arithmetique.is_suite_arithmetique([1, 1.12, 1.24, 1.36]), True)
        self.assertEqual(is_suite_arithmetique.is_suite_arithmetique([1, 2, 2.5, 3]), False)


if __name__ == '__main__':
    unittest.main()