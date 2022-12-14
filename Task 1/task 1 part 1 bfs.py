import cv2
import time
import random
import numpy as np
from collections import deque

def upsize(mat):
    new = np.full((800,800),255)
    for i in range(800):
        for j in range(800):
            x = (i - i%10)//10
            y = (j - j%10)//10
            new[i][j] = mat[x][y]
    return new

def maze():
    mat = np.full((80,80),255)
    for i in range(80):
        for j in range(80):
            pixel_val_probability = random.randrange(1,100)
            critical_val = random.randrange(20,30)
            if pixel_val_probability <= critical_val:
                mat[i][j]=0
    
    mat = upsize(mat)
    count=0
    grey = []
    while count<2:
        i,j = random.randrange(0,799), random.randrange(0,799)
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

def show_path(start,end,mat):
    dist=0
    current = end
    while current!=start:
        dist+=1
        mat[current.x][current.y] = 50
        current = current.parent
    return dist

def bfs(mat,start):
    q = deque()
    q.append(start)
    
    while len(q):

        current = q.popleft()
        i,j = current.x, current.y
        
        if j+1<mat.shape[1] :
            if mat[i][j+1] != 0 and mat[i][j+1] != 200:
                if mat[i][j+1]==127 and (i!= start.x) and (i!= start.x):
                    break
                mat[i][j+1]=200
                n=Node((i,j+1),current)
                q.append(n)
                cv2.imshow("path using bfs",mat)
                cv2.waitKey(1)

        if i+1<mat.shape[0] :
            if mat[i+1][j] != 0 and mat[i+1][j] != 200:
                if mat[i+1][j]==127 and (i!= start.x)  and (i!= start.x):
                    break
                mat[i+1][j]=200
                n=Node((i+1,j),current)
                q.append(n)
                cv2.imshow("path using bfs",mat)
                cv2.waitKey(1)

        if i>=1 :
            if mat[i-1][j] != 0 and mat[i-1][j] != 200:
                if mat[i-1][j]==127 and (i!= start.x ) and (i != start.x ):
                    break
                mat[i-1][j]=200
                n=Node((i-1,j),current)
                q.append(n)
                cv2.imshow("path using bfs",mat)
                cv2.waitKey(1)

        if j>=1:
            if mat[i][j-1] != 0 and mat[i][j-1] != 200:
                if mat[i][j-1]==127 and (i!= start.x ) and (i!= start.x):
                    break
                mat[i][j-1]=200
                n=Node((i,j-1),current)
                q.append(n)
                cv2.imshow("path using bfs",mat)
                cv2.waitKey(1)
    dist = show_path(start,current,mat)
    return dist

def restore(img,start,stop):
    for i in range(800):
        for j in range(800):
            if (i==start[0] and j==start[1]) or (i==stop[0] and j==stop[1]):
                img[i][j]=127
            elif img[i][j]==200 or img[i][j]==50:
                img[i][j]=255
    return img

mat,critical = maze()
start = critical[0]
stop = critical[1]
cv2.namedWindow("Maze",cv2.WINDOW_NORMAL)
cv2.imshow("Maze",mat)

cv2.namedWindow("Maze",cv2.WINDOW_NORMAL)
cv2.imshow("Maze",mat)

start_time = time.time()
start_node = Node((start[0],start[1]),None)
dist = bfs(mat,start_node)
time_bfs = time.time() - start_time
 
print("Time = %d sec\nDistance covered = %d"%(time_bfs,dist))

cv2.namedWindow("path using bfs",cv2.WINDOW_NORMAL)
cv2.imshow("path using bfs",mat)

mat = restore(mat,start,stop)

cv2.waitKey(0)
cv2.destroyAllWindows()