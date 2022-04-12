import CF

import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestLab3(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test1_lab(self, stdout):
        f_input = open('./test/R.in', 'r')
        f_expected = open('./test/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            CF.main()

            expected = str(expected).strip().replace("\n", ":")
            result = str(stdout.getvalue().strip()).replace("\n", ":")

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test2_lab(self, stdout):
        f_input = open('./test/Rsmall.in', 'r')
        f_expected = open('./test/Rsmall.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            CF.main()
            expected = str(expected).strip().replace("\n", ":")
            result = str(stdout.getvalue().strip()).replace("\n", ":")

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test3_lab(self, stdout):
        f_input = open('./test/Rsprut.in', 'r')
        f_expected = open('./test/Rsprut.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            CF.main()

            expected = str(expected).strip().replace("\n", ":")
            result = str(stdout.getvalue().strip()).replace("\n", ":")

            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
