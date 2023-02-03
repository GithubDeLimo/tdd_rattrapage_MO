import sudoku
import unittest


class TestEx2(unittest.TestCase):

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

    def test_ligne_valide(self):
        grille_ligne_valide = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                               [4, 2, 6, 7, 8, 9, 1, 5, 3],
                               [7, 2, 9, 1, 8, 3, 4, 5, 6],
                               [9, 2, 1, 3, 4, 5, 6, 7, 8],
                               [3, 2, 5, 6, 7, 8, 9, 1, 4],
                               [6, 2, 8, 9, 1, 7, 3, 4, 5],
                               [8, 2, 1, 9, 3, 4, 5, 6, 7],
                               [3, 2, 4, 5, 6, 7, 8, 9, 1],
                               [5, 2, 7, 8, 9, 1, 6, 3, 4]]

        grille_ligne_non_valide = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                   [4, 4, 4, 4, 4, 4, 4, 4, 4],
                                   [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                   [9, 1, 2, 3, 4, 5, 6, 7, 8],
                                   [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                   [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                   [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                   [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                   [5, 6, 7, 8, 9, 1, 2, 3, 4]]

        self.assertTrue(sudoku.ligne_valide(grille_ligne_valide))
        self.assertFalse(sudoku.ligne_valide(grille_ligne_non_valide))

    def test_colonnne_valide(self):
        grille_conlonne_valide = [[1, 2, 3, 4, 9, 6, 7, 8, 9],
                                  [4, 6, 6, 7, 8, 9, 1, 2, 3],
                                  [7, 8, 9, 1, 2, 3, 4, 3, 6],
                                  [9, 1, 2, 3, 4, 1, 6, 7, 8],
                                  [3, 4, 7, 6, 7, 8, 9, 1, 2],
                                  [6, 7, 8, 9, 1, 2, 3, 4, 4],
                                  [8, 9, 1, 2, 3, 4, 2, 6, 7],
                                  [2, 3, 4, 8, 6, 7, 8, 9, 1],
                                  [5, 5, 5, 5, 5, 5, 5, 5, 5]]

        grille_conlonne_non_valide = [[1, 2, 3, 4, 5, 6, 1, 8, 9],
                                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                      [7, 8, 9, 1, 2, 3, 1, 5, 6],
                                      [9, 1, 2, 3, 4, 5, 1, 7, 8],
                                      [3, 4, 5, 6, 7, 8, 1, 1, 2],
                                      [6, 7, 8, 9, 1, 2, 1, 4, 5],
                                      [8, 9, 1, 2, 3, 4, 1, 6, 7],
                                      [2, 3, 4, 5, 6, 7, 1, 9, 1],
                                      [5, 6, 7, 8, 9, 1, 1, 3, 4]]

        self.assertTrue(sudoku.colonne_valide(grille_conlonne_valide))
        self.assertFalse(sudoku.colonne_valide(grille_conlonne_non_valide))


if __name__ == '__main__':
    unittest.main()
