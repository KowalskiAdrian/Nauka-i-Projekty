import unittest

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

class TestRPS(unittest.TestCase):
    def test_player_1_wins(self):
        self.assertEqual(rps('rock', 'scissors'), "Player 1 won!")
        self.assertEqual(rps('paper', 'rock'), "Player 1 won!")
        self.assertEqual(rps('scissors', 'paper'), "Player 1 won!")
        
    def test_player_2_wins(self):
        self.assertEqual(rps('rock', 'paper'), "Player 2 won!")
        self.assertEqual(rps('paper', 'scissors'), "Player 2 won!")
        self.assertEqual(rps('scissors', 'rock'), "Player 2 won!")
        
    def test_draw(self):
        self.assertEqual(rps('rock', 'rock'), 'Draw!')
        self.assertEqual(rps('paper', 'paper'), 'Draw!')
        self.assertEqual(rps('scissors', 'scissors'), 'Draw!')

if __name__ == '__main__':
    unittest.main()