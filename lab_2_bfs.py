#####  Breadth First Search (BFS) #####
graph={
    0:[1,2],
    1:[3,4],
    2:[5],
    3:[],
    4:[],
    5:[],
   
}


from collections import deque
def bfs(src,graph):
    visited=set()
    queue=deque()
    queue.append(src)

    while queue:
        vertex=queue.popleft()
        visited.add(vertex)

        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
            
    return visited


print("Visited nodes are: ",bfs(0,graph))