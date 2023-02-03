import next_suite_geometrique
import unittest


class TestEx1(unittest.TestCase):

    def test_next_suite_geometrique(self):
        self.assertEqual(next_suite_geometrique.next_suite_geometrique(3, [1, 1, 4, 8, 16]), False)
        self.assertEqual(next_suite_geometrique.next_suite_geometrique(2, [1.1, 3.3, 9.9]), (True, [29.7, 89.1]))
        self.assertEqual(next_suite_geometrique.next_suite_geometrique(3, [1, 1, 1, 1]), (True, [1, 1, 1]))
        self.assertEqual(next_suite_geometrique.next_suite_geometrique(3, [0, 0, 0, 0]), False)


if __name__ == '__main__':
    unittest.main()
