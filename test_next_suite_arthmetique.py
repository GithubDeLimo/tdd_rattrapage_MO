import next_suite_arithmetique
import unittest


class TestEx1(unittest.TestCase):

    def test_next_suite_arithmetique(self):
        self.assertEqual(next_suite_arithmetique.next_suite_arithmetique(2, [1.5, 2, 2.5, 3]), (True, [3.5, 4]))
        self.assertEqual(next_suite_arithmetique.next_suite_arithmetique(5, [10, 15, 20, 25]), (True, [30, 35, 40, 45, 50]))
        self.assertEqual(next_suite_arithmetique.next_suite_arithmetique(7, [0, 0]), (True, [0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual(next_suite_arithmetique.next_suite_arithmetique(2, [1, 2, 2.5, 3]), False)
        self.assertEqual(next_suite_arithmetique.next_suite_arithmetique(3, [11, 12, 13, 15]), False)
        self.assertEqual(next_suite_arithmetique.next_suite_arithmetique(2, [1, 1.12, 1.24, 1.36]), (True, [1.48, 1.60]))


if __name__ == '__main__':
    unittest.main()
