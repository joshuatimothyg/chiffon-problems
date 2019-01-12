import unittest


def bfs_get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users
    
    if start_node not in graph.keys() or end_node not in graph.keys():
        raise Exception

    visited = []
    queue = []
    tracking = []
    queue.append(start_node)
    
    current_node = None
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node == end_node:
            break
        elif current_node not in visited:
            visited.append(current_node)
            queue.extend(graph[current_node])
            for item in graph[current_node]:
                tracking.append((item ,current_node))
        else:
            continue

    if current_node != end_node:
        return None
    backtrack = [current_node]
    while current_node != start_node:
        for item in tracking:
            if item[0] == current_node:
                current_node = item[1]
                backtrack.append(current_node)
                break

    backtrack.reverse()
    return backtrack



#graph = {
#            'a': ['b', 'c', 'd'],
#            'b': ['a', 'd'],
#            'c': ['a', 'e'],
#            'd': ['a', 'b'],
#            'e': ['c'],
#            'f': ['g'],
#            'g': ['f'],
#        }
#print(bfs_get_path(graph, 'a', 'e'))
#expected = ['a', 'c', 'e']

# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)



#    test_end_node_not_present (__main__.Test) ... ok
#    test_no_path (__main__.Test) ... ok
#    test_one_hop_path_1 (__main__.Test) ... FAIL
#    test_one_hop_path_2 (__main__.Test) ... FAIL
#    test_one_hop_path_3 (__main__.Test) ... FAIL
#    test_start_node_not_present (__main__.Test) ... ok
#    test_two_hop_path_1 (__main__.Test) ... FAIL
#    test_two_hop_path_2 (__main__.Test) ... FAIL
#    test_zero_hop_path (__main__.Test) ... ok