import unittest
from rome import add

class AdditionTest(unittest.TestCase):

    def test_adding_Is(self):
        self.assertEqual(add('I', 'I'), 'II')
        self.assertEqual(add('I', 'II'), 'III')


    def test_inputs_out_of_scope_raise_exceptions(self):
        for bad_input in (2, None, 'Z', 'V', 'X', 'L', 'C', 'D', 'M'):
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


if __name__ == '__main__':
    unittest.main()