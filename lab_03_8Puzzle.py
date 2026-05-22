## 8 Puzzle Problem using BFS ##
from collections import deque
initial_state=((1,2,3),(4,6,0),(7,5,8))

goal=((1,2,3),(4,5,6),(7,8,0))

def find_blank_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None


def generate_moves(state):
    x,y=find_blank_space(state)
    moves=[]
    directions=[(-1,0),(1,0),(0,-1),(0,1)]

    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            newstate=[list(row) for row in state]
            newstate[x][y],newstate[nx][ny]=newstate[nx][ny],newstate[x][y]
            moves.append(tuple(tuple(row) for row in newstate))

    return moves

def bfs(initial_state):
    visited=set()
    queue=deque()
    queue.append((initial_state,[]))
    while queue:
        state,path=queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path+=[state]

        if state==goal:
            return path
        
        for nextstate in generate_moves(state):
            if nextstate not in visited:
                queue.append((nextstate,path))
    return None

puzzle_path=bfs(initial_state)
if puzzle_path:
    print('Solution found ')
    for i in puzzle_path:
        for j in i:
            print(j,end='\n')
        print()    
        print(i,end='\n\n')    

else:
    print('no solution')        

    
        
