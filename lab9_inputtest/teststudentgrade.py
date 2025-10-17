"""
Daniel Oluwasina
Oct 8th, 2025
Lab 9, test input and output data
"""
import unittest
from unittest.mock import patch
import io
import studentsgrade

class TestMainFunction(unittest.TestCase):
    #test valid inputs
    @patch('builtins.input', side_effect = ['3','85','90','75'])
    #capture the output
    @patch('sys.stdout', new_callable=io.StringIO)

    #define function to test the input and output
    def test_valid_input(self, mock_stdout, mock_input):

        studentsgrade.main()

        
        output = mock_stdout.getvalue()

        self.assertIn("The class average is 83.33", output)

    #testing invalid input, then valid

    @patch('builtins.input', side_effect = ['-1', '0', '2', '95','110', '80'])
    @patch('sys.stdout', new_callable=io.StringIO)

    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Number of students must be greater than 0, Please try again", output)
        self.assertIn("Invalid input. Enter a grade between 0 and 100:", output)
        self.assertIn("The class average is 87.50", output)


    #Exercise
    @patch('builtins.input', side_effect = ['a', '2', 'b', '6', '7'])
    @patch('sys.stdout', new_callable=io.StringIO)

    def test_invalid_string_input(self, mock_stdout, mock_input):
        studentsgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("invalid input. Please enter a positive nunumerical value", output)
        self.assertIn("Invalid input! Enter a numerical value", output)
        self.assertIn("The class average is 6.5", output)

if __name__ == "__main__":
    unittest.main()