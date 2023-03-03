# 3DPathFinder 

<img src="https://ipick.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3846ffed-7a76-481d-906e-0b3683edca8f%2F8_evoluzioni_labirinto_multidimensionale.jpg?id=63c27227-364b-401a-9541-082ad3e1b088&table=block&spaceId=12cd12be-4b3c-4ad4-89b4-ee3477841446&width=1960&userId=&cache=v2" align="right" width="160" height="178">

Path finder algorithm finds the shortest path from a start cell to a stop cell.

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
### Dijkstra algorithm

## dijkstra3d package


## Installation
### Installation in anaconda


```bash
conda create --name pathfinder python=3.9.16
```


```bash
conda activate pathfinder
```

### Download the code

```bash
git clone https://github.com/nucontreras/3d-maze.git
```


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


## Program use

### Parameter configuration

### Optimal path

### Visualization


## Examples of visualization
<p float="left">
  <img src="img/maze_3x3x3_faces.gif" width="266" />
  <img src="img/maze_3x3x3_faces_edges.gif" width="266" /> 
  <img src="img/maze_3x3x3_faces_edges_corners.gif" width="266" /> 
</p>

<p float="left">
  <img src="img/maze_3x5x9_faces.gif" width="266" />
  <img src="img/maze_3x5x9_faces_edges.gif" width="266" /> 
  <img src="img/maze_3x5x9_faces_edges_corners.gif" width="266" /> 
</p>


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
