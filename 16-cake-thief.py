#problem is
# prioritizing which when same shilling per kg

import unittest

def get_cake_shillings_per_kg(cake_tuple):
    return cake_tuple[0]

def max_duffel_bag_value(cake_tuples, weight_capacity):

    cake_tuple_list = []
    # Calculate the maximum value we can carry
    for type_of_cake in cake_tuples:
        cake_tuple_list.append((float(type_of_cake[1]) / float(type_of_cake[0]), type_of_cake[0], type_of_cake[1]))

    cake_tuple_list.sort(reverse=True, key=lambda e: (e[0], e[2] * - 1))
#    cake_tuple_list.sort(reverse=True, key=get_cake_shillings_per_kg)

    print(cake_tuple_list)

    max_monetary_value = 0
    while weight_capacity > 0 and len(cake_tuple_list) > 0:
        if weight_capacity - cake_tuple_list[0][1] >= 0:
            weight_capacity -= cake_tuple_list[0][1]
            max_monetary_value += cake_tuple_list[0][2]
        else:
            cake_tuple_list.pop(0)

    return max_monetary_value

lol = max_duffel_bag_value([(4, 4), (5, 5)], 9)
print(lol)

# Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


#unittest.main(verbosity=2)