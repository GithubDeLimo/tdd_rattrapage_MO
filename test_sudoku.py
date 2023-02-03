import sudoku
import unittest


class TestEx1(unittest.TestCase):

    def test_taille_valide(self):
        grille_taille_valide = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1]]

        grille_taille_non_valide1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1, 1, 1]]

        grille_taille_non_valide2 = [[1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1],
                                     [1, 1, 1]]
        self.assertTrue(sudoku.taille_valide(grille_taille_valide))
        self.assertFalse(sudoku.taille_valide(grille_taille_non_valide1))
        self.assertFalse(sudoku.taille_valide(grille_taille_non_valide2))


if __name__ == '__main__':
    unittest.main()
