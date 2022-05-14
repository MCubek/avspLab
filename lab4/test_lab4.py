import ClosestBlackNode, NodeRank

import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestLab4(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_a_lab_1(self, stdout):
        f_input = open('./test/a/btest2/R.in', 'r')
        f_expected = open('./test/a/btest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            NodeRank.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.maxDiff = None

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_a_lab_2(self, stdout):
        f_input = open('./test/a/mtest2/R.in', 'r')
        f_expected = open('./test/a/mtest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            NodeRank.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_a_lab_3(self, stdout):
        f_input = open('./test/a/stest2/R.in', 'r')
        f_expected = open('./test/a/stest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            NodeRank.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_a_lab_4(self, stdout):
        f_input = open('./test/a/ttest2/R.in', 'r')
        f_expected = open('./test/a/ttest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            NodeRank.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_b_lab_1(self, stdout):
        f_input = open('./test/b/btest2/R.in', 'r')
        f_expected = open('./test/b/btest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            ClosestBlackNode.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_b_lab_2(self, stdout):
        f_input = open('./test/b/mtest2/R.in', 'r')
        f_expected = open('./test/b/mtest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            ClosestBlackNode.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_b_lab_3(self, stdout):
        f_input = open('./test/b/stest2/R.in', 'r')
        f_expected = open('./test/b/stest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            ClosestBlackNode.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_b_lab_4(self, stdout):
        f_input = open('./test/b/ttest2/R.in', 'r')
        f_expected = open('./test/b/ttest2/R.out', 'r')

        input_string = f_input.read()
        expected = f_expected.read()

        f_input.close()
        f_expected.close()

        with patch('sys.stdin', StringIO(input_string)):
            ClosestBlackNode.main()

            expected = str(expected).strip()
            result = str(stdout.getvalue().strip())

            self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
