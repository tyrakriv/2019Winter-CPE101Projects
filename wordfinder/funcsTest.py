# Project 3 - Word Puzzle
# 
# Name: Aine Larkin and Tyra Krivonak
# Instructor: S. Einakian
# Section: 9

import unittest
from funcs import checkBackward, checkForward, checkUp, checkDown

class TestFuncs(unittest.TestCase):
    
    def test_checkBackward(self):
        self.assertEqual(checkBackward('aryt','kdhkjtyras'), 8)
        self.assertEqual(checkBackward('aine','kdhkeniajs'), 7)

    def test_checkForward(self):
        self.assertEqual(checkForward('tyra', 'kdhkjtyras'), 5)
        self.assertEqual(checkForward('aine', 'kdaineyras'), 2)

    def test_checkUp(self):
        self.assertEqual(checkUp('COMPILE','WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), ('6','8'))
        self.assertEqual(checkUp('CHICKEN','EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'), ('8','8'))

    def test_checkDown(self):
        self.assertEqual(checkDown('CALPOLY','WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'), ('1','0'))
        self.assertEqual(checkDown('RABBIT','EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'), ('1','3'))


if __name__ == '__main__':
   unittest.main()
