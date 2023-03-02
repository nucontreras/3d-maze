from path_finder import PathFinder3D
import numpy as np

my_path_finder = PathFinder3D()

np.random.seed(41)

# Example of a 3d map
maze_3d = np.random.randint(low=0, high=2, size=(40, 50, 60))

output = my_path_finder.find_path(maze_3d, start=[0, 0, 0], stop=[35, 45, 51])
print(output)

my_path_finder.visualize()
