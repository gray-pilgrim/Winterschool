import cv2
import numpy as np
import random
import time
from collections import deque

#making a mini maze

maze = np.full((25,25),255)

rand1 = random.uniform(0.2,0.3)
for i in range(25):
    for j in range(25):
        rand2 = random.uniform(0,1)
        if rand2>rand1:
            maze[i,j] = 255
        else:
            maze[i,j] = 0

img = np.full((75,75),255)

m,n = img.shape

for i in range(25):
    for j in range(25):
        for x in range(0,3):
            for y in range(0,3):
                img[x + 3*i][y + 3*j] = maze[i,j]

stop = (74,0)
start = (0,74)

cv2.namedWindow("Maze",cv2.WINDOW_NORMAL)

img[stop] = 127
img[start] = 127

####

#dijsktra

cv2.namedWindow("Path Dijsktra",cv2.WINDOW_NORMAL)

queue = []
min_distance = np.full((n,m),np.inf)
visited = np.full((n,m), False)
parent = np.full((n,m), None)
closed_list = []

def Dijsktra(image, start, stop):

    global parent
    queue.append(start)
    min_distance[start[0],start[1]] = 0
    visited[start[0],start[1]] = True
    parent[start[0],start[1]] = None
    node = None

    while(len(queue) != 0):

        cv2.imshow("Maze",image.astype(np.uint8))
        cv2.waitKey(1)

        node = queue.pop(0)
        closed_list.append(node)
        if(node == stop):
            break
        (i,j) = node
        for i1 in range(i-1,i+2):
            for j1 in range(j-1,j+2):
                if((i1,j1) == (i-1,j-1) or (i1,j1) == (i-1,j+1) or (i1,j1) == (i+1,j-1) or (i1,j1) == (i+1,j+1)):
                    continue
                if(i1 < 0 or j1 < 0 or i1 >= n or j1 >= m):
                    continue
                elif(image[i1,j1] == 255 or (image[i1,j1] == 127 and (i1,j1) not in closed_list)):

                    #dist = math.sqrt((i1-i)**2 + (j1-j)**2)
                    dist = 1

                    if(visited[i1,j1] == True):
                        if(dist + min_distance[i,j] < min_distance[i1,j1]):
                            min_distance[i1,j1] = dist + min_distance[i,j]
                            parent[i1,j1] = node

                    else:
                        queue.append((i1,j1))
                        min_distance[i1,j1] = min_distance[i,j] + dist 
                        parent[i1,j1] = node
                        visited[i1,j1] = True
                        image[i1,j1] = 127

####

print("Dijsktra Algorithm")
img_dijkstra = img.copy()
img_dijkstra_path = img.copy()
begin = time.time()
Dijsktra(img_dijkstra,start,stop)
end = time.time()

print(f"Dijsktra algorithm time = {end-begin}")

cv2.waitKey(1000)

####

#Path for djikstra

stack = []

node = stop

while(node != None):
    
    stack.append(node)
    node = parent[node[0]][node[1]]


while(len(stack) != 0):

    x = stack.pop()
    img_dijkstra_path[x[0],x[1]] = 127

    cv2.imshow("Path Dijsktra",img_dijkstra_path.astype(np.uint8))
    cv2.waitKey(2)

print(f"Djisktra Path Distance : {min_distance[stop[0],stop[1]]}")

####
print()
#BFS

cv2.namedWindow("Path BFS",cv2.WINDOW_NORMAL)

class Node:
    def __init__(self,index,parent):
        self.x = index[0]
        self.y = index[1]
        self.parent = parent 

def show_path(end,mat):

    d = 0
    current = end

    while current != None:

        mat[current.x][current.y] = 127
        d += 1
        current = current.parent
        cv2.imshow("Path BFS",mat.astype(np.uint8))
        cv2.waitKey(2)

    return d


def bfs(mat,start,mat_copy):

    q = deque()
    q.append(start)
    
    while (len(q) != 0):

        current = q.popleft()
        i,j = current.x, current.y
        
        cv2.imshow("Maze",mat.astype(np.uint8))
        cv2.waitKey(1)

        if j+1 < m :
            if mat[i][j+1] != 0 and mat[i][j+1] != 200:
                if mat[i][j+1]==127 and (i!= start.x) and (j+1!= start.y):
                    break
                mat[i][j+1]=200
                N=Node((i,j+1),current)
                q.append(N)

        if i+1< n :
            if mat[i+1][j] != 0 and mat[i+1][j] != 200:
                if mat[i+1][j]==127 and (i+1!= start.x)  and (j!= start.y):
                    break
                mat[i+1][j]=200
                N=Node((i+1,j),current)
                q.append(N)

        if i>=1 :
            if mat[i-1][j] != 0 and mat[i-1][j] != 200:
                if mat[i-1][j]==127 and (i-1!= start.x) and (j!= start.y):
                    break
                mat[i-1][j]=200
                mat[i-1][j]=200
                N=Node((i-1,j),current)
                q.append(N)

        if j>=1:
            if mat[i][j-1] != 0 and mat[i][j-1] != 200:
                if mat[i][j-1]==127 and (i!= start.x ) and (j-1!= start.y):
                    break
                mat[i][j-1]=200
                N=Node((i,j-1),current)
                q.append(N)

    global distance
    distance = show_path(current,mat_copy)

###
print("BFS Algorithm")

img_bfs = img.copy()
img_bfs_path = img.copy()
begin = time.time()
s = Node(start,None)
bfs(img_bfs,s,img_bfs_path)
end = time.time()

print(f"BFS Algorithm time = {end-begin}")

print(f"BFS Path Distance : {distance}")

###
print()

cv2.waitKey(0)
cv2.destroyAllWindows()