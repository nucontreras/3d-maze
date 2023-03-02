# Import of packages

import sys
import dijkstra3d
import numpy as np
import matplotlib.pyplot as plt


# Python class for the Path finder.
class PathFinder3D:
    """
    A class used to represent a 3D path finder

    ...

    Methods
    -------
    verify_input(start, stop)
        Verify that the start and stop parameters satisfy the limit
        constraints and that they are not an obstacle inside the maze.
    verify_output(output)
        Verify that the path found does not pass through obstacles.
    find_path(field, start, stop, connectivity=0)
        Apply the dijkstra algorithm using the distance to the target
        as a heuristic (A* search)
    visualize()
        Visualize the path found using a 3D map.
    """

    def __init__(self):
        # Setting hidden parameters to store temporary and permanent information.
        self._path_found = None
        self._field = None
        self._search_type = 'faces'  # Type of connectivity chosen.
        self._types_of_search = {0: 'faces', 1: 'faces and edges', 2: 'faces, edges and corners'}  # connectivity types.
        self._connectivity_dijkstra_package = {0: 6, 1: 18, 2: 26}  # Connectivity values used by the dijkstra3d package

    def verify_input(self, start, stop):
        """Verify that the start and stop parameters satisfy the limit
         constraints and that they are not an obstacle inside the maze.

        Parameters
        ----------
        start : list
            Start cell.

        stop : list
            Target cell.
        """

        field_shape = self._field.shape

        # Verification of 'start' and 'stop' coordinate boundaries.
        if any(val < 0 for val in start):  # Verification of negative values for the start cell.
            sys.exit("The start cell is out of bounds. This cell cannot have negative values.")
        elif any(val < 0 for val in stop):  # Verification of negative values for the stop cell.
            sys.exit("The stop cell is out of bounds. This cell cannot have negative values.")
        elif any(start[i] >= field_shape[i] for i in range(3)):  # Checks if the start coordinate respects the shape.
            sys.exit("The start cell is out of bounds. Check its upper limits.")
        elif any(stop[i] >= field_shape[i] for i in range(3)):  # Checks if the stop coordinate respects the shape.
            sys.exit("The stop cell is out of bounds. Check its upper limits.")
        elif self._field[start[0], start[1], start[2]] == 1:  # Checks if the start coordinate is not an obstacle.
            sys.exit(f"The start cell {start} is an obstacle. Change it for an empty cell.")
        elif self._field[stop[0], stop[1], stop[2]] == 1:  # Checks if the stop coordinate is not an obstacle.
            sys.exit(f"The stop cell {stop} is an obstacle. Change it for an empty cell.")

    def verify_output(self, output):
        """Verify that the path found does not pass through obstacles.

        Parameters
        ----------
        output : ndarray
            The path found by the dijkstra algorithm.
        """

        # Query the value of each coordinate of the optimal path found by dijkstra in the original maze.
        i = np.ravel_multi_index(output.T, self._field.shape)
        path_values = self._field.take(i)
        # Get the values that are not zeros, that is, if the algorithm encountered an obstacle as the optimal decision.
        check_zeros = path_values.nonzero()

        # Check if there are nodes that are obstacles.
        if len(check_zeros[0]) != 0:
            other_options = ' or '.join(str(i) + ': ' + self._types_of_search[i] for i in range(3) if
                                        list(self._types_of_search.values())[i] != self._search_type)
            sys.exit(f"An optimal path has not been found, because there are obstacles blocking all possible paths.\n"
                     f"Try another value for the parameter connectivity to find the optimal path.\n"
                     f"You can also use these values for the connectivity parameter: "
                     f"{other_options}.")

    def find_path(self, field, start, stop, connectivity=0):
        """Apply the dijkstra algorithm using the distance to the target
        as a heuristic (A* search)

        Parameters
        ----------
        field : ndarray
            3D matrix representing the maze

        start : list
            Star cell.

        stop : list
            Target cell.

        connectivity : int (default 0)
            0 (faces), 1 (faces + edges), and
            3 (faces + edges + corners) voxel graph connectivities
            are supported.

        Returns
        -------
        self._path_found : ndarray
            The path found by the dijkstra algorithm.
        """

        # Verifies the connectivity chosen by the user.
        connectivity_ = None
        if connectivity not in [0, 1, 2]:
            sys.exit("Only 0, 1, and 2 are the options for the attribute connectivity")
        else:
            connectivity_ = self._connectivity_dijkstra_package[connectivity]
            self._search_type = self._types_of_search[connectivity]

        self._field = field  # Save the maze
        self.verify_input(start, stop)  # Checks if the input satisfies the boundary constraints.

        # Determine the optimal path.
        # It always prioritizes the paths with the lowest value, i.e. those with value 0,
        # but if there is no other option, it takes an obstacle as a path.
        path_found = dijkstra3d.dijkstra(field, start, stop, compass=True, connectivity=connectivity_)

        self.verify_output(path_found)  # Verify if the path found did not pass through obstacles.
        self._path_found = path_found  # Save the path found.

        return self._path_found

    def visualize(self):
        """Visualize the path found using a 3D map.
        For better visualization, if the number of obstacles
        is greater than 100, they are not added to the display.
        """

        # Check if the program has found an optimal path to print.
        if self._path_found is None:
            sys.exit("First you must use the find_path() function to find an optimal path.")

        # Setting up the 3D figure
        fig = plt.figure(figsize=(16, 16))
        ax = fig.add_subplot(111, projection='3d')

        i, j, k = self._field.nonzero()  # Find the coordinates of the nodes that are obstacles.
        if len(i) < 100:  # if there are more than 100 obtacles, we don't print the points for better visualization
            ax.scatter(i, j, k, marker="x", c="red")

        # Adds the optimal path found to the 3D plot.
        for i in range(len(self._path_found) - 1):
            ax.plot([self._path_found[i, 0], self._path_found[i + 1, 0]], [self._path_found[i, 1],
                                                                           self._path_found[i + 1, 1]],
                    zs=[self._path_found[i, 2],
                        self._path_found[i + 1, 2]])

        # Set the name of the figure and its axes.
        ax.set_title("3D Maze")

        ax.set_xlabel("N")
        ax.set_ylabel("M")
        ax.set_zlabel("K")

        ax.set_xticks(range(0, len(self._field) - 1))
        ax.set_yticks(range(0, len(self._field[0]) - 1))
        ax.set_zticks(range(0, len(self._field[0][0]) - 1))

        ax.set_xlim(0, len(self._field) - 1)
        ax.set_ylim(0, len(self._field[0]) - 1)
        ax.set_zlim(0, len(self._field[0][0]) - 1)

        plt.show()
