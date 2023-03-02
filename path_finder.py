import sys
import dijkstra3d
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


class PathFinder3D:

    def __init__(self):
        self.path_found = None
        self.field = None
        self.search_type = 'faces'
        self.types_of_search = {0: 'faces', 1: 'faces and edges', 2: 'faces, edges and corners'}  # connectivity

    def verify_input(self, start, stop):
        field_shape = self.field.shape

        # print(f"field_shape = {field_shape}")
        if any(val < 0 for val in start):
            print("The start cell is out of bounds. This cell cannot have negative values.")
            sys.exit()
        elif any(val < 0 for val in stop):
            print("The stop cell is out of bounds. This cell cannot have negative values.")
            sys.exit()
        elif any(val >= field_shape[0] for val in start):
            print("The start cell is out of bounds. Check its upper limits.")
            sys.exit()
        elif any(val >= field_shape[0] for val in stop):
            print("The stop cell is out of bounds. Check its upper limits.")
            sys.exit()
        if self.field[start[0], start[1], start[2]] == 1:
            print(f"The start cell {start} is an obstacle. Change it for an empty cell.")
            sys.exit()
        elif self.field[stop[0], stop[1], stop[2]] == 1:
            print(f"The stop cell {stop} is an obstacle. Change it for an empty cell.")
            sys.exit()

    def verify_output(self, output):
        i = np.ravel_multi_index(output.T, self.field.shape)
        path_values = self.field.take(i)
        print(f"path_values = {path_values}")

        check_zeros = path_values.nonzero()
        print(f"check_values = {check_zeros}")

        if len(check_zeros[0]) != 0:
            print("An optimal path has not been found, because there are obstacles blocking all possible paths.")
            print(f"Try another type of connectivity to find the optimal path: "
                  f"{' or '.join(str(i) for i in list(self.types_of_search.values()) if i != self.search_type)}")
            sys.exit()

    def find_path(self, field, start, stop):
        self.field = field
        self.verify_input(start, stop)
        # path = dijkstra3d.dijkstra(field, source, target, bidirectional=True)  # 2x memory usage, faster
        # self.path_found = dijkstra3d.dijkstra(field, start, stop, compass=True)

        # graphe to add constrains
        # graph = np.zeros(field.shape, dtype=np.uint32)
        # graph += 0xffffffff  # all directions are permissible
        # x, y, z = self.field.nonzero()
        # for i, j, k in zip(x, y, z):
        #     print(f"i, j, k = {(i, j, k)}")
        #     graph[i, j, k] = graph[i, j, k] & 0xfffffffe

        path_found = dijkstra3d.dijkstra(field, start, stop, compass=True, connectivity=6)  # , voxel_graph=graph
        self.verify_output(path_found)
        self.path_found = path_found

        return self.path_found

    def visualize(self):
        if self.path_found is None:
            print("First you must use the find_path() function to find an optimal path.")
            sys.exit()

        fig = plt.figure(figsize=(16, 16))
        ax = fig.add_subplot(111, projection='3d')

        i, j, k = self.field.nonzero()
        if len(i) < 100:  # if there are more than 100 obtacles, we don't print the points for better visualization
            ax.scatter(i, j, k, marker="x", c="red")

        for i in range(len(self.path_found) - 1):
            ax.plot([self.path_found[i, 0], self.path_found[i + 1, 0]], [self.path_found[i, 1],
                                                                         self.path_found[i + 1, 1]],
                    zs=[self.path_found[i, 2],
                        self.path_found[i + 1, 2]])

        ax.set_title("3D Maze")

        ax.set_xlabel("N")
        ax.set_ylabel("M")
        ax.set_zlabel("K")

        ax.set_xticks(range(0, len(self.field) - 1))
        ax.set_yticks(range(0, len(self.field[0]) - 1))
        ax.set_zticks(range(0, len(self.field[0][0]) - 1))

        ax.set_xlim(0, len(self.field) - 1)
        ax.set_ylim(0, len(self.field[0]) - 1)
        ax.set_zlim(0, len(self.field[0][0]) - 1)

        plt.show()
