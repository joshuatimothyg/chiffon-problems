import unittest


def find_repeat_unoptimized(the_list):

    # Find a number that appears more than once
    exist_list = []
    for item in the_list:
        if item in exist_list:
            return item
        else:
            exist_list.append(item)
    return None



def find_repeat(the_list):

    for outer_item in the_list:
        matches = 0
        for inner_item in the_list:
            if outer_item == inner_item:
                matches += 1
        if matches > 1:
            return outer_item
    return None














# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)