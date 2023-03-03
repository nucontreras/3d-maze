# 3DPathFinder 

<img src="https://ipick.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3846ffed-7a76-481d-906e-0b3683edca8f%2F8_evoluzioni_labirinto_multidimensionale.jpg?id=63c27227-364b-401a-9541-082ad3e1b088&table=block&spaceId=12cd12be-4b3c-4ad4-89b4-ee3477841446&width=1960&userId=&cache=v2" align="right" width="160" height="178">

Path finder algorithm finds the shortest path from a start cell to a stop cell.

This program uses the [dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) algorithm to traverse the 3D matrix in search of the shortest path. To do this, it uses the [dijkstra3d](https://pypi.org/project/dijkstra3d/) package which, by using the distance from target as a heuristic (A* search), returns the best option. 

The program has the ability to check the validity of the inputs and return an answer only if it is possible to find an optimal path without passing through obstacles in the maze.

## Table Of Content

- [Problem Description](#problem-description)
    - [Challenge](#challenge)
    - [Dijkstra algorithm](#dijkstra-algorithm)
- [dijkstra3d package](#dijkstra3d-package)
- [Installation](#installation)
    - [Installation in anaconda](#installation-in-anaconda)
    - [Package requirements](#package-requirements)
    - [Download the code](#download-the-code)
- [Program use](#program-use)
    - [Parameter configuration](#parameter-configuration)
    - [Optimal path](#optimal-path)
    - [Visualization](#visualization)
 - [Examples of visualization](#examples-of-visualization)
- [License](#license)
- [Links](#links)


## Problem Description 

### Challenge


<img src="https://ipick.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa8a31844-44f0-40f5-a3d2-3850fc3f761d%2FUntitled.png?id=150520a9-aa46-406a-b7a4-84a37a86d48b&table=block&spaceId=12cd12be-4b3c-4ad4-89b4-ee3477841446&width=2000&userId=&cache=v2" align="right" width="260" height="160">

The problem consists of a 3D grid of size (N x M x K).

Within the grid each node can be either an empty cell, noted as 0 or an obstacle, noted as 1.

The objective is to find the shortest possible path from the start cell to the stop cell in the grid given its coordinates (e. g., start = [0, 0, 0], end = [N-1, M-1, K-1]).

### Dijkstra algorithm



## dijkstra3d package

To find the most optimal path, 3DPathFinder uses the package [dijkstra3d](https://pypi.org/project/dijkstra3d/). 3DPathFinder implements the A* search algorithm to find the optimal answer. It uses the distance to the target as a heuristic. In Figure 1 it can be seen that its performance is much better compared to the other resolution methods that can be used with this package.


<img src="https://warehouse-camo.ingress.cmh1.psfhosted.org/5e9118a193e6cb4b675a6b5e329f0b6dc60b8cb2/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7365756e672d6c61622f64696a6b7374726133642f6d61737465722f64696a6b7374726133642e706e67" width="600" height="350">
Fig. 1: A benchmark of dijkstra.dijkstra run on a 5123 voxel field of ones from bottom left source to top right target. (black) unidirectional search (blue) bidirectional search (red) A* search aka compass=True.

</br>
</br>

On the other hand, image 2 shows that this type of heuristic works very well when the grid is larger.

<img src="https://warehouse-camo.ingress.cmh1.psfhosted.org/55884be22e4c2a87229220d1ddbcddb3d9a28884/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7365756e672d6c61622f64696a6b7374726133642f6d61737465722f6d756c74696d6574686f642e706e67" width="600" height="350">
Fig. 2: A benchmark of dijkstra.dijkstra run on a 503 voxel field of random integers of increasing variation from random source to random target. (blue/squares) unidirectional search (yellow/triangles) bidirectional search (red/diamonds) A* search aka compass=True.

</br>
</br>

The *dijkstra3d* package uses *cython* to store the value of program variables using the *C* language. For this reason, by saving values using a compiled language, the access to the variables is much faster, thus increasing the performance considerably compared to a program written only in *python*.

## Installation

3DPathFinder has been tested in an [anaconda](https://www.anaconda.com/) environment with *python 3.9.16*.

### Installation in anaconda

Create a new environment in anaconda with *python=3.9.16*:

```bash
conda create --name pathfinder python=3.9.16
```

Activate the new environment:

```bash
conda activate pathfinder
```

### Download the code

To install 3DPathFinder you can download the program from its GitHub repository as follows:

```bash
git clone https://github.com/nucontreras/3d-maze.git
```

Open the 3DPathFinder folder from the terminal 

```bash
cd 3d-maze
```

### Package requirements

To use the program it is necessary to install the following packages using pip : 

```txt
matplotlib==3.5.3
numpy==1.23.5
dijkstra3d==1.12.0
```

Execute the following line of code in the command line:

```bash
pip install -r requirements.txt
```

You have everything installed to be able to use the program.

## Program use

To use the program you have to open the *3dpathfinder/* folder in the command line:

```bash
cd 3dpathfinder
```

### Parameter configuration

The execution of the program is performed with the following command:

```bash
python main.py
```

However, you must choose or write certain parameters inside the **main.py** file to test with different types of grids and input and stop cells.

First of all you must create a 3D grid and define start and entry coordinates. Make sure that the coordinates correspond to the size of the grid, otherwise the program will warn you to change the input.

In the following image there is an example of use:

<img src="img/main.JPG" width="600" height="250">


### Optimal path

To find the optimal path, the function *find_path(grid, start=start_cell, stop=stop_cell)* must be used into de *main.py* file.

Example:

```python
output = my_path_finder.find_path(maze_3d, start=[0, 0, 0], stop=[35, 45, 51])
```
To the *find_path()* function you can add the *connectivity* parameter to define the type of moves you want to make to find the solution. The options are **0: faces, 1: faces and edges, 2: faces, edges and corners**.

Example:

```python
output = my_path_finder.find_path(maze_3d, start=[0, 0, 0], stop=[35, 45, 51], connectivity=1)  # search a path by moving along the faces and edges.
```

### Visualization

To visualize the path within a 3D grid you can add the following line of code to the *main.py* file

```python
my_path_finder.visualize()
```
If the grid has more than 100 obstacle type cells, the display will not show the obstacles for a better visualization of the path found. In another case, the obstacle cells are represented by a red x. In section [Examples of visualization](#examples-of-visualization) you can see some animations of the viewer.

## Examples of visualization

For the following three cases, the first image of each example uses the algorithm looking for possible paths considering only the faces of a voxel in the 3D matrix. The second image considers a connectivity of type faces and edges, i.e. diagonal movements within the same face. Finally, the third one considers faces, edges and corners, i.e. all diagonal movements from a node, including diagonal movements in 3D.

### Maze 3x3x3
<p float="left">
  <img src="img/maze_3x3x3_faces.gif" width="266"/>
  <img src="img/maze_3x3x3_faces_edges.gif" width="266" /> 
  <img src="img/maze_3x3x3_faces_edges_corners.gif" width="266" /> 
</p>

### Maze 3x5x9
<p float="left">
  <img src="img/maze_3x5x9_faces.gif" width="266" />
  <img src="img/maze_3x5x9_faces_edges.gif" width="266" /> 
  <img src="img/maze_3x5x9_faces_edges_corners.gif" width="266" /> 
</p>

### Maze 40x50x60
<p float="left">
  <img src="img/maze_40x50x60_faces.gif" width="266" />
  <img src="img/maze_40x50x60_faces_edges.gif" width="266" /> 
  <img src="img/maze_40x50x60_faces_edges_corners.gif" width="266" /> 
</p>


## License

The 3DPathFinder is licensed under the terms of the GNU General Public License
license and is available for free.

## Links
* [Challenge description](https://ipick.notion.site/Multidimensional-Maze-751dd3ef642748d38606af0add166319)
* [dijkstra3d](https://pypi.org/project/dijkstra3d/)
