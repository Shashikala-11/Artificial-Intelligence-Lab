graph={
    0:[1,2,3],
    1:[4,5],
    2:[6],
    3:[7,8],
    4:[],
    5:[],
    6:[],
    7:[9],
    8:[],
    9:[]

}


heuristicFunction={
    0:20,
    1:22,
    2:21,
    3:10,
    4:25,
    5:24,
    6:30,
    7:5,
    8:12,
    9:0
}
 
#########  Greedy Best First Search Algorithm  #########
def gbfs(src,dest,graph,heuristicFunction):
    # print("Hello, GBFS!")
    openList=[]
    closeList=[]
    openList.append(src)

    while(openList):

        currNode=openList[0]
        currIndex=0

        for i in range(len(openList)):
            if heuristicFunction[openList[i]]<heuristicFunction[currNode]:
                currNode=openList[i]
                currIndex=i
        openList.pop(currIndex)
        closeList.append(currNode)
        if currNode==dest:
            return closeList
        for neighbor in graph[currNode]:
            if neighbor not in closeList and neighbor not in openList:
                openList.append(neighbor)


    return None
result=gbfs(0,9,graph,heuristicFunction)


#displaying path from source to destination
for i in range(len(result)):
    if i==len(result)-1:
        print(f'{result[i]} with heuristic value {heuristicFunction[result[i]]}\n')
    else:
        print(f'{result[i]} with heuristic value {heuristicFunction[result[i]]}\n', end="->")

## Totl cost of the path
print(f'Total cost of the path is {sum(heuristicFunction[result[i]] for i in range(len(result)))}')


#######   Visualization of the graph using networkx and matplotlib  ######## 

import networkx as nx
import matplotlib.pyplot as plt

# 1. Create the graph object
G = nx.Graph()

# 2. Add connections (edges)
edges = [(0, 1), (1, 4), (1, 5), (0, 2), (2, 6),(0, 3) ,(3, 7), (3, 8), (7, 9)]
G.add_edges_from(edges)


# 3. Draw and display the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
plt.show()