import SimHash
import SimHashBuckets

import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


# noinspection DuplicatedCode
class TestLab1(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_partA(self, stdout):
        f_input = open('./test/SimHash/R.in', 'r')
        f_expected = open('./test/SimHash/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)) as stdin:
            SimHash.main()

            expected = str(expected).replace("\n", ":")
            result = str(stdout.getvalue()).replace("\n", ":")

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_partB1(self, stdout):
        f_input = open('./test/LSH/test1/R.in', 'r')
        f_expected = open('./test/LSH/test1/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)) as stdin:
            SimHashBuckets.main()

            expected = str(expected).replace("\n", ":")
            result = str(stdout.getvalue()).replace("\n", ":")

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_partB2(self, stdout):
        f_input = open('./test/LSH/test2/R.in', 'r')
        f_expected = open('./test/LSH/test2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)) as stdin:
            SimHashBuckets.main()

            expected = str(expected).replace("\n", ":")
            result = str(stdout.getvalue()).replace("\n", ":")

            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
