import unittest
from rome import add

class AdditionTest(unittest.TestCase):
    # I ran following tests using a command 'python3 -m unittest discover
    def test_adding_Is(self):
        self.assertEqual(add('I', 'I'), 'II')
        self.assertEqual(add('I', 'II'), 'III')


    def test_inputs_out_of_scope_raise_exceptions(self):
        for bad_input in (2, None, 'Z', 'L', 'C', 'D', 'M'):
            with self.assertRaises(ValueError) as m:
                add('I', bad_input)
                if not hasattr(m, 'exception'):
                    self.fail('%s as augend did not raise exception' % bad_input)

            with self.assertRaises(ValueError) as m:
                add(bad_input, 'I')
                if not hasattr(m, 'exception'):
                    self.fail('%s as addend did not raise exception' % bad_input)

    def test_IV_and_V(self):
        self.assertEqual(add('II', 'II'), 'IV')
        self.assertEqual(add('III', 'II'), 'V')
        self.assertEqual(add('IV', 'I'), 'V')
        self.assertEqual(add('V', 'I'), 'VI')
        self.assertEqual(add('I', 'V'), 'VI')


    def test_IX_and_X(self):
        self.assertEqual(add('V', 'V'), 'X')
        self.assertEqual(add('V', 'IV'), 'IX')
        self.assertEqual(add('VIII', 'I'), 'IX')
        self.assertEqual(add('IX', 'I'), 'X')
        self.assertEqual(add('X', 'I'), 'XI')
        self.assertEqual(add('I', 'X'), 'XI')
        self.assertEqual(add('X', 'V'), 'XV')
        self.assertEqual(add('V', 'X'), 'XV')
        self.assertEqual(add('X', 'X'), 'XX')

# After writing the last test I typed 'python3 -m coverage report' into the terminal and received following data:
# Name       Stmts   Miss  Cover
# ------------------------------
# rome.py       12      0   100%
# tests.py      34     10    71%
# ------------------------------
# TOTAL         46     10    78%
# (jagodajeczmien-lazur) jagodajeczmien-lazur@iMac-Radoslaw roman_converter % '


if __name__ == '__main__':
    unittest.main()