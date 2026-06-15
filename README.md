"# Artificial Intelligence Lab

## Overview

This repository contains Python implementations of fundamental search algorithms and problem-solving examples from an introductory artificial intelligence lab. It includes graph traversal, informed and uninformed search, and state-space exploration for classic problems.

![AI Search Algorithms Overview](readme_diagram.png)

The implemented algorithms are:

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Greedy Best-First Search (GBFS)
- Uniform Cost Search (UCS)
- 8-puzzle problem solver using BFS
- Vacuum Cleaner environment demonstration

## File Summary

- `dfsUsingRecursiveApproach.py`
  - Recursive Depth-First Search on a directed graph.

- `lab_2_bfs.py`
  - Breadth-First Search on a directed graph.

- `gbfs.py`
  - Greedy Best-First Search with a heuristic function.
  - Includes a graph visualization using `networkx` and `matplotlib`.

- `lab_04_gbfs.py`
  - A second implementation of Greedy Best-First Search using the same graph model.

- `lab_2_ucs.py` and `ucs.py`
  - Uniform Cost Search for weighted graphs.
  - `ucs.py` contains a more complete version of UCS using a priority-driven frontier.

- `lab_03_8Puzzle.py`
  - 8-puzzle solver using BFS for state-space search.

- `lab_03_vaccum_cleaner.py`
  - Vacuum cleaner environment simulation showing state cleanup.

## Algorithms and Approaches

### Depth-First Search (DFS)

`dfsUsingRecursiveApproach.py` explores a graph by recursively visiting a node and then each of its unvisited neighbors.

Key properties:
- Search order: explore as deep as possible before backtracking.
- Implementation uses recursion and a visited set.
- Output is the set of visited nodes in the DFS traversal.

Pseudo-code:

```text
DFS(node):
  mark node visited
  for each neighbor of node:
    if neighbor not visited:
      DFS(neighbor)
```

### Breadth-First Search (BFS)

`lab_2_bfs.py` and `lab_03_8Puzzle.py` use BFS to explore nodes in order of increasing distance from the start state.

BFS approach:
- Use a queue to maintain frontier nodes.
- Visit nodes level by level.
- Record visited nodes to avoid repetition.

Pseudo-code:

```text
BFS(start):
  enqueue start
  while queue is not empty:
    node = dequeue
    if node is goal: return path
    for each neighbor of node:
      if neighbor not visited:
        mark visited
        enqueue neighbor
```

### Greedy Best-First Search (GBFS)

`gbfs.py` and `lab_04_gbfs.py` implement GBFS using a heuristic function that estimates distance to the goal.

GBFS approach:
- Maintain an open list of frontier nodes.
- Select the node with the lowest heuristic value.
- Expand that node and add its unexplored neighbors.
- Continue until the destination is reached.

Pseudo-code:

```text
GBFS(start, goal):
  open = [start]
  closed = []
  while open not empty:
    current = node in open with lowest heuristic
    remove current from open
    add current to closed
    if current == goal: return path
    for each neighbor of current:
      if neighbor not in open and neighbor not in closed:
        add neighbor to open
```

### Uniform Cost Search (UCS)

`ucs.py` and `lab_2_ucs.py` implement UCS to find the lowest-cost path in a weighted graph.

UCS approach:
- Use a frontier ordered by cumulative path cost.
- Expand the node with the smallest accumulated cost first.
- Track the path and cost for each frontier entry.

Pseudo-code:

```text
UCS(start, goal):
  frontier = priority queue with (cost=0, node=start, path=[start])
  visited = set()
  while frontier not empty:
    cost, node, path = pop lowest-cost entry
    if node in visited: continue
    if node == goal: return path, cost
    add node to visited
    for each neighbor, weight of node:
      if neighbor not visited:
        push (cost+weight, neighbor, path+[neighbor])
```

### 8-Puzzle Solver

`lab_03_8Puzzle.py` solves the 8-puzzle using BFS over board states.

Approach:
- Represent the board as a tuple of tuples.
- Identify the blank (zero) position.
- Generate valid successor states by sliding adjacent tiles.
- Use BFS until the goal board configuration is reached.

State transition diagram:

```text
Initial state -> successor states -> successor states -> ... -> Goal state
```

### Vacuum Cleaner Environment

`lab_03_vaccum_cleaner.py` models a simple environment with room states labeled as `dirty` or `clean`.

Approach:
- Represent rooms as a dictionary.
- Iterate over each location.
- Clean every location marked `dirty`.

This script is a basic demonstration of environment state updates rather than a full search algorithm.

## Flowcharts

DFS flowchart:

```text
[Start] -> [Visit node] -> [For each neighbor]
       -> [Neighbor visited?] -> No -> [Recurse DFS(neighbor)]
       -> [Yes] -> [Continue]
       -> [Return visited nodes]
```

BFS flowchart:

```text
[Start] -> [Enqueue start]
       -> [Dequeue node]
       -> [Goal?] -> Yes -> [Return path]
                 -> No -> [Enqueue unvisited neighbors]
       -> [Repeat]
```

GBFS flowchart:

```text
[Start] -> [Open = {start}]
       -> [Select node with lowest heuristic]
       -> [Is node goal?] -> Yes -> [Return path]
                            -> No -> [Expand neighbors]
       -> [Add unexplored neighbors to open]
       -> [Repeat]
```

UCS flowchart:

```text
[Start] -> [Frontier = {(0, start)}]
       -> [Select lowest-cost node]
       -> [Is node goal?] -> Yes -> [Return path, cost]
                            -> No -> [Expand neighbors]
       -> [Add or update frontier entries with new costs]
       -> [Repeat]
```

## Complexity Summary

| Algorithm | Time Complexity | Space Complexity | Notes |
|----------|-----------------|------------------|-------|
| DFS | O(V + E) | O(V) | Recursion depth may equal path length. |
| BFS | O(V + E) | O(V) | Uses queue and visited set. |
| GBFS | O(b^m) / O(V^2) | O(V) | Current implementation scans open list linearly. |
| UCS | O(E log V) ideally | O(V) | Current code sorts frontier, which adds overhead. |
| 8-puzzle BFS | Exponential | Exponential | State space size up to 181,440 reachable states. |

## Running the Examples

Use Python 3 to execute any script.

```bash
python dfsUsingRecursiveApproach.py
python lab_2_bfs.py
python gbfs.py
python ucs.py
python lab_03_8Puzzle.py
python lab_03_vaccum_cleaner.py
```

For the graph visualization in `gbfs.py`, install the required packages and run the script:

```bash
pip install networkx matplotlib
python gbfs.py
```

## Sample Outputs

### `dfsUsingRecursiveApproach.py`

```text
Visited node: 1
Visited node: 3
Visited node: 6
Visited node: 7
Visited node: 2
Visited node: 4
Visited node: 5
DFS traversal of the graph is: {'2', '5', '4', '6', '3', '7', '1'}
```

### `lab_2_bfs.py`

```text
Visited nodes are:  {0, 1, 2, 3, 4, 5}
```

### `gbfs.py`

```text
0 with heuristic value 20
->3 with heuristic value 10
->7 with heuristic value 5
->9 with heuristic value 0

Total cost of the path is 35
```

### `lab_2_ucs.py`

```text
Path: ['R', 'B', 'D', 'G'], Total Cost: 12
```

### `ucs.py`

```text
Path: ['R', 'B', 'D', 'G'], Total Cost: 12
```

### `lab_03_8Puzzle.py`

```text
Solution found 
(1, 2, 3)
(4, 6, 0)
(7, 5, 8)

((1, 2, 3), (4, 6, 0), (7, 5, 8))

(1, 2, 0)
(4, 6, 3)
(7, 5, 8)

((1, 2, 0), (4, 6, 3), (7, 5, 8))

(1, 2, 3)
(4, 6, 8)
(7, 5, 0)

((1, 2, 3), (4, 6, 8), (7, 5, 0))

(1, 2, 3)
(4, 0, 6)
(7, 5, 8)

((1, 2, 3), (4, 0, 6), (7, 5, 8))

(1, 0, 2)
(4, 6, 3)
(7, 5, 8)

((1, 0, 2), (4, 6, 3), (7, 5, 8))

(1, 2, 3)
(4, 6, 8)
(7, 0, 5)

((1, 2, 3), (4, 6, 8), (7, 0, 5))

(1, 0, 3)
(4, 2, 6)
(7, 5, 8)

((1, 0, 3), (4, 2, 6), (7, 5, 8))

(1, 2, 3)
(4, 5, 6)
(7, 0, 8)

((1, 2, 3), (4, 5, 6), (7, 0, 8))

(1, 2, 3)
(0, 4, 6)
(7, 5, 8)

((1, 2, 3), (0, 4, 6), (7, 5, 8))

(1, 6, 2)
(4, 0, 3)
(7, 5, 8)

((1, 6, 2), (4, 0, 3), (7, 5, 8))

(0, 1, 2)
(4, 6, 3)
(7, 5, 8)

((0, 1, 2), (4, 6, 3), (7, 5, 8))

(1, 2, 3)
(4, 0, 8)
(7, 6, 5)

((1, 2, 3), (4, 0, 8), (7, 6, 5))

(1, 2, 3)
(4, 6, 8)
(0, 7, 5)

((1, 2, 3), (4, 6, 8), (0, 7, 5))

(0, 1, 3)
(4, 2, 6)
(7, 5, 8)

((0, 1, 3), (4, 2, 6), (7, 5, 8))

(1, 3, 0)
(4, 2, 6)
(7, 5, 8)

((1, 3, 0), (4, 2, 6), (7, 5, 8))

(1, 2, 3)
(4, 5, 6)
(0, 7, 8)

((1, 2, 3), (4, 5, 6), (0, 7, 8))

(1, 2, 3)
(4, 5, 6)
(7, 8, 0)
```

### `lab_03_vaccum_cleaner.py`

```text
Initial Environment state: {'A': 'dirty', 'D': 'dirty', 'C': 'clean', 'B': 'clean'}
Cleaning the environment...
C is Already clean
B is Already clean
Final Environment state: {'A': 'clean', 'D': 'clean', 'C': 'clean', 'B': 'clean'}
```

### `lab_04_gbfs.py`

This file is currently incomplete and raises a syntax error during execution. It is a second GBFS implementation template.

## Notes

- The implemented GBFS examples use only heuristic values and do not guarantee the shortest path in terms of actual cost.
- The UCS implementation is functional, but performance can improve by replacing the sorted deque with a proper priority queue such as `heapq`.
- The vacuum cleaner example demonstrates state updates rather than full search planning.

## Conclusion

This repository demonstrates foundational AI search techniques and state-space exploration. The code emphasizes algorithm behavior and the relationship between search order, heuristics, and path cost.
" 
