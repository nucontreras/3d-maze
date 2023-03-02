from path_finder import PathFinder3D
import numpy as np
import unittest


class TestPathFinder3D(unittest.TestCase):
    """
    Tests for PathFinder3D class using unittest.

    ...

    Methods
    -------
    test_simple_example_coordinates_out_of_bounds()
        Simple test of a matrix of shape (3,3,3) with no solution.
        Some input is out of bounds.
    test_simple_example_coordinates_obstacle()
        Simple test of a matrix of shape (3,3,3) with no solution.
        Some input is an obstacle in the maze.
    test_simple_with_solution()
        Verify if the output is a ndarray.
    test_simple_with_solution_connectivity_1()
        Verify that an optimal path cannot be found using connectivity=0.
    test_simple_with_solution_connectivity_2(self)
        Verify that an optimal path cannot be found using connectivity=1.
    test_bigger_example_with_solution()
        Verify if the output is a ndarray.
    """

    def test_simple_example_coordinates_out_of_bounds(self):
        my_path_finder = PathFinder3D()
        # Simple example with no solution: coordinate out of bounds
        field = field = np.array([[[0, 1, 0], [0, 0, 1], [1, 1, 1]],
                                  [[1, 0, 1], [0, 0, 1], [1, 0, 0]],
                                  [[0, 0, 0], [1, 1, 1], [0, 0, 1]]])
        source = [0, 0, 0]
        target = [3, 3, 3]

        # Verify the detection of a system error.
        with self.assertRaises(SystemExit) as cm:
            my_path_finder.find_path(field, start=source, stop=target, connectivity=0)  # Call function.
        self.assertEqual(cm.exception.args[0], 'The stop cell is out of bounds. Check its upper limits.')

    def test_simple_example_coordinates_obstacle(self):
        my_path_finder = PathFinder3D()
        # Simple example with no solution: coordinate is an obstacle
        field = np.array([[[0, 1, 0], [0, 0, 1], [1, 1, 1]],
                          [[1, 0, 1], [0, 0, 1], [1, 0, 0]],
                          [[0, 0, 0], [1, 1, 1], [0, 0, 1]]])
        source = [0, 0, 0]
        target = [2, 2, 2]

        # Verify the detection of a system error.
        with self.assertRaises(SystemExit) as cm:
            my_path_finder.find_path(field, start=source, stop=target, connectivity=0)  # Call function.
        self.assertEqual(cm.exception.args[0], 'The stop cell [2, 2, 2] is an obstacle. Change it for an empty cell.')

    def test_simple_with_solution(self):
        my_path_finder = PathFinder3D()
        # Simple example with solution
        field = np.array([[[0, 1, 0], [0, 0, 1], [1, 1, 1]],
                          [[1, 0, 1], [0, 0, 1], [1, 0, 0]],
                          [[0, 0, 0], [1, 1, 1], [0, 0, 1]]])
        source = [0, 0, 0]
        target = [1, 2, 2]

        # Verify if the type output is ndarray
        output = my_path_finder.find_path(field, start=source, stop=target, connectivity=0)  # Call function.
        self.assertIsInstance(output, np.ndarray)

    def test_simple_with_solution_connectivity_1(self):
        my_path_finder = PathFinder3D()
        # Simple example with solution (with connectivity=1: 'faces and edges').
        field = np.array([[[0, 1, 0], [1, 0, 1], [1, 1, 1]],
                          [[1, 0, 1], [0, 0, 1], [1, 0, 0]],
                          [[0, 0, 0], [1, 1, 1], [0, 0, 1]]])
        source = [0, 0, 0]
        target = [1, 2, 2]

        # Verify the detection of a system error.
        with self.assertRaises(SystemExit) as cm:
            my_path_finder.find_path(field, start=source, stop=target, connectivity=0)  # Call function.
        self.assertEqual(cm.exception.args[0], 'An optimal path has not been found, because there are obstacles '
                                               'blocking all possible paths.\n'
                                               'Try another value for the parameter connectivity '
                                               'to find the optimal path.\n'
                                               'You can also use these values for the connectivity parameter: '
                                               '1: faces and edges or 2: faces, edges and corners.')

    def test_simple_with_solution_connectivity_2(self):
        my_path_finder = PathFinder3D()
        # Simple example with solution (with connectivity=1: 'faces and edges').
        field = np.array([[[0, 1, 0], [1, 1, 1], [1, 1, 1]],
                          [[1, 1, 1], [1, 0, 1], [1, 0, 0]],
                          [[0, 0, 0], [1, 1, 1], [0, 0, 1]]])
        source = [0, 0, 0]
        target = [1, 2, 2]

        # Verify the detection of a system error.
        with self.assertRaises(SystemExit) as cm:
            my_path_finder.find_path(field, start=source, stop=target, connectivity=1)  # Call function.
        self.assertEqual(cm.exception.args[0], 'An optimal path has not been found, because there are obstacles '
                                               'blocking all possible paths.\n'
                                               'Try another value for the parameter connectivity '
                                               'to find the optimal path.\n'
                                               'You can also use these values for the connectivity parameter: '
                                               '0: faces or 2: faces, edges and corners.')

    def test_bigger_example_with_solution(self):
        my_path_finder = PathFinder3D()
        # Simple example with solution
        field = np.array([[[0, 1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 1],
                           [0, 0, 1, 0, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0, 1, 0, 0]],
                          [[0, 1, 1, 0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1, 0],
                           [0, 0, 0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1, 1]],
                          [[0, 1, 0, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 1, 1, 1, 0]]])
        source = [0, 0, 0]
        target = [1, 2, 2]

        # Verify if the type output is ndarray
        output = my_path_finder.find_path(field, start=source, stop=target, connectivity=0)  # Call function.
        self.assertIsInstance(output, np.ndarray)


if __name__ == '__main__':
    unittest.main()

# More examples tested

# np.random.seed(41)

# Example without solution : there is no possible path
# field = np.array([[[0, 1, 0], [1, 1, 1], [1, 1, 1]],
#                   [[1, 0, 1], [0, 1, 1], [1, 0, 0]],
#                   [[0, 0, 0], [1, 0, 1], [0, 0, 1]]])
# source = [0, 0, 0]
# target = [2, 2, 1]

# Example 2 without solution : there is no possible path
# field = np.array([[[0, 1, 0], [1, 1, 1], [1, 1, 1]],
#                   [[1, 0, 1], [1, 1, 1], [1, 0, 0]],
#                   [[0, 0, 0], [1, 0, 1], [0, 0, 1]]])
# source = [0, 0, 0]
# target = [2, 2, 1]

# Huge example with solution
# field = np.random.randint(low=0, high=2, size=(40, 50, 60))
# source = [0, 0, 0]
# target = [38, 45, 54]

# Monster example with solution
# field = np.random.randint(low=0, high=2, size=(50, 60, 70))
# source = [0, 0, 0]
# target = [49, 59, 69]
