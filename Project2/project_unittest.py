import unittest
from main import Connect4

class test_switchPlayer(unittest.TestCase):
    def setUp(self):
        self.test = Connect4()
    def test_switch(self):
        self.test.switch_player()
        self.assertEqual(self.test.current_player, 'O')
        self.test.switch_player()
        self.assertEqual(self.test.current_player, 'X')




if __name__ == '__main__':
    unittest.main()

        
