import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    singles = 0
    the_string = list(the_string)
    
    while len(the_string) != 0:
        current_letter = the_string.pop()
        if current_letter not in the_string:
            singles += 1
        else:
            the_string.pop(the_string.index(current_letter))
    
    
    if singles > 1:
        return False
    return True

















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)