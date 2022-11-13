import unittest
from rome import add

class AdditionTest(unittest.TestCase):

    def test_adding_Is(self):
        self.assertEqual(add('I', 'I'), 'II')

def test_adding_Is(self):
    self.assertEqual(add('I', 'I'), 'II')
    self.assertEqual(add('I', 'II'), 'III')

if __name__ == '__main__':
    unittest.main()

