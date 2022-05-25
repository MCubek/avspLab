from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from lab5 import GNAlgorithm


class Test(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_a_lab_5(self, stdout):
        f_input = open('./test/t.in', 'r')
        f_expected = open('./test/t.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            GNAlgorithm.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.maxDiff = None

            self.assertEqual(expected, result)    \

    @patch('sys.stdout', new_callable=StringIO)
    def test_b_lab_5(self, stdout):
        f_input = open('./test/a.in', 'r')
        f_expected = open('./test/a.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            GNAlgorithm.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.maxDiff = None

            self.assertEqual(expected, result)
