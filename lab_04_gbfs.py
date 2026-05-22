##### Greedy Best First Search Algorithm Implementation #####

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

hf={
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

def gbfs(src,dest,graph,hf):
    openList=[]
    closeList=[]
    openList.append(src)
    while openList:
        currNode=openList[0]
        currIndex=0

        for i in range(len(openList)):
            if hf[openList[i]]