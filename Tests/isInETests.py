import unittest
from src.funtion_file import isInE

class MyTestCase(unittest.TestCase):
    def test_Empty_String(self):
        # Assume
        string = ''

        # Action
        result = isInE(string)

        # Assert
        self.assertTrue(result)

    def test_Balanced_Round_Bracket(self):
        # Assume
        string = '((()()())())'

        # Action
        result = isInE(string)

        # Assert
        self.assertTrue(result)

    def test_Not_Balanced_Round_Bracket(self):
        # Assume
        string = '()())('

        # Action
        result = isInE(string)

        # Assert
        self.assertFalse(result)

    def test_a_b_In_E(self):
        # Assume
        string = '(a)(b)'

        # Action
        result = isInE(string)

        # Assert
        self.assertTrue(result)

    def test_a_b_Not_In_E(self):
        # Assume
        string = '(a(b))'

        # Action
        result = isInE(string)

        # Assert
        self.assertFalse(result)

    def test_a_In_E(self):
        # Assume
        string = '(a)'

        # Action
        result = isInE(string)

        # Assert
        self.assertTrue(result)

    def test_a_Not_In_E(self):
        # Assume
        string = 'a)'

        # Action
        result = isInE(string)

        # Assert
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
