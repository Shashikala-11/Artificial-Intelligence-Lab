from collections import deque

def uniform_cost_search(graph, start, goal):
    # Frontier stores tuples: (cumulative_cost, current_node, path)
    frontier = deque([(0, start, [start])])
    visited = set()

    while frontier:
        # 1. Sort the deque to ensure the lowest cost node is at the front
        # Note: In a true UCS, a Priority Queue (heapq) is more efficient
        frontier = deque(sorted(frontier, key=lambda x: x[0]))
        
        # 2. Pop the node with the lowest cumulative cost
        cost, current, path = frontier.popleft()

        if current in visited:
            continue
        
        # 3. Check if we reached the goal
        if current == goal:
            return path, cost
        
        visited.add(current)

        # 4. Expand neighbors
        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in visited:
                new_cost = cost + weight
                new_path = path + [neighbor]
                frontier.append((new_cost, neighbor, new_path))
                
    return None, float('inf')

# Example Weighted Graph
graph = {
    'R':{'A':8,'B':7},
    'A': {'R':8,'C': 9},
    'B': {'R':7,'D': 1},
    'C': {'G': 3},
    'D': {'G': 4},
    'G': {}
}

path, total_cost = uniform_cost_search(graph, 'R', 'G')
print(f"Path: {path}, Total Cost: {total_cost}")
