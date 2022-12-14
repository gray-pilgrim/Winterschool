import cv2
import time
import random
import numpy as np
from collections import deque
import sys
sys.setrecursionlimit(100000)

def upsize(mat):
    new = np.full((160,160),255)
    for i in range(160):
        for j in range(160):
            x = (i - i%4)//4
            y = (j - j%4)//4
            new[i][j] = mat[x][y]
    return new

def maze():
    mat = np.full((40,40),255)
    for i in range(40):
        for j in range(40):
            pixel_val_probability = random.randrange(1,100)
            critical_val = random.randrange(20,30)
            if pixel_val_probability <= critical_val:
                mat[i][j]=0
    
    mat = upsize(mat)
    count=0
    grey = []
    while count<2:
        i,j = random.randrange(0,159), random.randrange(0,159)
        if (mat[i+1,j]!=0 or mat[i-1,j] !=0 or mat[i,j+1]!=0 or mat[i,j-1] !=0) and mat[i+1,j]!=127 and mat[i-1,j] !=127 and mat[i,j+1]!=127 and mat[i,j-1] !=127:
            mat[i,j]=127
            count+=1
            grey.append((i,j))

    return mat.astype(np.uint8), grey

class Node:
    def __init__(self,index,parent):
        self.x = index[0]
        self.y = index[1]
        self.parent = parent 

def show_path(path,mat):
    dist=0
    cv2.namedWindow("Path using DFS",cv2.WINDOW_NORMAL)
    while len(path)>=1:
        current=path[-1]
        dist+=1
        mat[current.x][current.y] = 50
        path.pop()
    cv2.imshow("Path using DFS",mat)
    return dist

def dfs(current,img):

    global check
    if check==1:
        return
    i,j=current.x,current.y
    path_dfs.append(current) 

    cv2.namedWindow('DFS', cv2.WINDOW_NORMAL)
    cv2.imshow('DFS', img)
    cv2.waitKey(1)

    if i==stop[0] and j==stop[1]:
        global dist_dfs
        check=1
        dist = show_path(path_dfs,path_using_dfs)
        dist_dfs = dist
        return
    
    if i>=1:
        if img[i-1][j]!=0 and img[i-1][j]!=200:
            node=Node((i-1,j),current)
            img[i][j]=200
            dfs(node,img)
        
    if j>=1:
        if img[i][j-1]!=0 and img[i][j-1]!=200:
            node = Node((i,j-1),current)
            img[i][j]=200
            dfs(node,img)
    
    if j+1<img.shape[1]:
        if img[i][j+1]!=0 and img[i][j+1]!=200:
            img[i][j]=200
            node=Node((i,j+1),current)
            dfs(node,img)

    if i+1<img.shape[0]:
        if img[i+1][j]!=0 and img[i+1][j]!=200:
            img[i][j]=200
            node=Node((i+1,j),current)
            dfs(node,img)

mat,critical = maze()
start = critical[0]
stop = critical[1]
print(start,stop)
cv2.namedWindow("Maze",cv2.WINDOW_NORMAL)
cv2.imshow("Maze",mat)

start_time = time.time()
start_node = Node((start[0],start[1]),None)
img_dfs = mat.copy()
path_using_dfs = mat.copy()
path_dfs=deque()
dist_dfs=-1
check=0
dfs(start_node,img_dfs)
time_dfs = time.time() - start_time

if dist_dfs!=-1:
    print("Time = %d sec\nDistance covered = %d"%(time_dfs,dist_dfs))
else:
    print("No path found")

cv2.waitKey(0)
cv2.destroyAllWindows()