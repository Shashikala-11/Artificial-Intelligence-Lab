def dfs(graph,node,visited):
   
    if visited is None:
        visited=[]

    visited.append(node)
    print('Visited node:',node)
    
    for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(graph,neighbour,visited)   

    return set(visited)            

graph={
    '1':['3','2'],
    '2':['4','5'],
    '3':['6','7'],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
}

print(f'DFS traversal of the graph is: {dfs(graph,'1',None)}')