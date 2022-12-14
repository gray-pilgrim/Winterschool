import numpy as np
import cv2
from collections import deque
import sys
sys.setrecursionlimit(2000000)

class Node:
    def __init__(self,index,parent):
        self.x = index[0]
        self.y = index[1]
        self.parent = parent 

img = cv2.imread("my_map.png")
n,m,l = img.shape
#processing

for i in range(n):
    for j in range(m):
        if(sum(img[i,j]) <= 254*3):
            img[i][j] = (0,0,0)
        else:
            img[i][j] = (255,255,255)

####

start = Node((99,486),None)
stop = Node((310,629),None)

def show_path(path,mat):
    dist=0
    while len(path)>=1:
        current=path[-1]
        dist+=1
        mat[current.x][current.y][0] = 255
        mat[current.x][current.y][1] = 0
        mat[current.x][current.y][2] = 0
        path.pop()
    cv2.namedWindow("Path using DFS",cv2.WINDOW_NORMAL)
    cv2.imshow("Path using DFS",mat)
    return dist

def dfs(current):

    global check
    if check==1:
        return
    i,j=current.x,current.y
    path_dfs.append(current) 

    cv2.namedWindow('DFS', cv2.WINDOW_NORMAL)
    cv2.imshow('DFS', img)
    cv2.waitKey(1)

    if i==stop.x and j==stop.y:

        global dist_dfs
        check=1
        dist = show_path(path_dfs,dfs_path)
        dist_dfs = dist
        return
    
    img[i,j] = [127,127,127]

    if(i-1 >= 0):
        if(np.array_equal(img[i-1][j], [255,255,255]) == True):
            dfs(Node((i-1,j),current))
    if(j-1 >= 0):
        if(np.array_equal(img[i][j-1], [255,255,255]) == True):
            dfs(Node((i,j-1),current))
    if(i+1 < n):
        if(np.array_equal(img[i+1][j], [255,255,255]) == True):
            dfs(Node((i+1,j),current))
    if(j+1 < m):
        if(np.array_equal(img[i][j+1], [255,255,255]) == True):
            dfs(Node((i,j+1),current))
    if((i-1) >= 0 and (j-1)>= 0):
        if(np.array_equal(img[i-1][j-1], [255,255,255]) == True):
            dfs(Node((i-1,j-1),current))
    if((i-1) >= 0 and (j+1)< 255):
        if(np.array_equal(img[i-1][j+1], [255,255,255]) == True):
            dfs(Node((i-1,j+1),current))
    if((i+1) < 255 and (j-1)>= 0):
        if(np.array_equal(img[i+1][j-1], [255,255,255]) == True):
            dfs(Node((i+1,j-1),current))
    if((i+1) < 255 and (j+1) < 255):
        if(np.array_equal(img[i+1][j+1], [255,255,255]) == True):
            dfs(Node((i+1,j+1),current))


cv2.namedWindow("Map",cv2.WINDOW_NORMAL)
cv2.imshow("Map",img)

dfs_img=img.copy()
dfs_path=img.copy()
dist_dfs=0
check=0
path_dfs=deque()
dfs(start)
print("Distance = ",dist_dfs)

cv2.waitKey(0)
cv2.destroyAllWindows()