from path_finder import PathFinder3D
import numpy as np

my_path_finder = PathFinder3D()

np.random.seed(41)

# Example of a 3d map
# maze_3d = np.random.randint(low=0, high=2, size=(40, 50, 60))
# print(maze_3d)

# output = my_path_finder.find_path(maze_3d, start=[0, 0, 0], stop=[39, 48, 56])

# Test Area

# Simple example with no solution: coordinate out of bounds
# field = np.random.randint(low=0, high=2, size=(3, 3, 3))
# source = [0, 0, 0]
# target = [3, 3, 3]

# Simple example with no solution: coordinate is an obstacle
field = np.random.randint(low=0, high=2, size=(3, 3, 3))
source = [0, 0, 0]
target = [2, 2, 2]

# Simple example with solution
# field = np.random.randint(low=0, high=2, size=(3, 3, 3))
# source = [0, 0, 0]
# target = [1, 2, 2]

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

# Bigger example with solution
# field = np.random.randint(low=0, high=2, size=(3, 5, 9))
#
# source = [0, 0, 0]
# target = [0, 4, 5]

# Huge example with solution
# field = np.random.randint(low=0, high=2, size=(40, 50, 60))
# source = [0, 0, 0]
# target = [38, 45, 54]



output = my_path_finder.find_path(field, start=source, stop=target)
print(output)

my_path_finder.visualize()
