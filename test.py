import unittest

from calc import calc, calc_line


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calc_line('+ 5 4'), 9)

    def test_sub(self):
        self.assertEqual(calc_line('- 5 1'), 4)

    def test_mul(self):
        self.assertEqual(calc_line('* 3 3'), 9)

    def test_div(self):
        self.assertEqual(calc_line('/ 12 3'), 4)

    def test_invalid(self):
        self.assertRaises(ValueError, calc_line, 'invalid')

    def test_invalid(self):
        self.assertRaises(KeyError, calc_line, '= 1 2')

    def test_extra_spaces(self):
        self.assertEqual(calc_line('    +  1   2  '), 3)

if __name__ == '__main__':
    unittest.main()
