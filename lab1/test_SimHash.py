import SimHash

import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestSimHash(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, stdout):
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


if __name__ == '__main__':
    unittest.main()
