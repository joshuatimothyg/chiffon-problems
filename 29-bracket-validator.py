import unittest


def is_valid(code):

    openers_tuple = ('(', '[', '{')
    closers_tuple = (')', ']', '}')
    closer_dict = { ')' : '(',
                    ']' : '[',
                    '}' : '{'
                  }
    char_stack = []


    for char in code:
        print(char_stack)

        if char in openers_tuple:
            char_stack.append(char)
        elif char in closers_tuple and len(char_stack) > 0:
            if char_stack[-1] == closer_dict[char]:
                char_stack.pop()
            else:
                return False
        else:
            return False

    print(char_stack)
    if len(char_stack) == 0:
        return True
    else:
        return False

# Tests



class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)







    
#    opened_parenthesis = 0
#    opened_braces = 0
#    opened_brackets = 0
#    
#    for character in code:
#        if character == '(':
#            opened_parenthesis += 1
#        if character == ')':
#            opened_parenthesis -= 1
#                
#        if character == '[':
#            opened_braces += 1
#        if character == ']':
#            opened_braces -= 1
#
#        if character == '{':
#            opened_brackets += 1
#        if character == '}':
#            opened_brackets -= 1
#
#    if opened_parenthesis == 0 and opened_braces == 0 and opened_brackets == 0:
#        return True
#    else:
#        return False