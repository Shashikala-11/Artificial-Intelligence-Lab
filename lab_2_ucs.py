##### Uniform Cost Search (UCS) #####
# Example Weighted Graph
graph = {
    'R':{'A':8,'B':7},
    'A': {'R':8,'C': 9},
    'B': {'R':7,'D': 1},
    'C': {'G': 3},
    'D': {'G': 4},
    'G': {}
}


from collections import deque
def ucs(graph,start,goal):
    visited=set()
    frontier=deque([(0,start,[start])]) # (cost, node, path)

    while frontier:
        frontier=deque(sorted(frontier,key=lambda x:x[0])) # sort by cost
        cost,current_node,path=frontier.popleft()

        if current_node in visited:
            continue

        elif current_node==goal:
            return path,cost
        
        else:

            for neighbor,weight in graph.get(current_node,{}).items():
                if neighbor not in visited:
                    new_cost=cost+weight
                    new_path=path+[neighbor]
                    frontier.append((new_cost,neighbor,new_path))
    return None,float('inf')

path,total_cost=ucs(graph,'R','G')
                
print(f"Path: {path}, Total Cost: {total_cost}")