import cv2
from collections import deque
import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self,index,parent):
        self.x = index[0]
        self.y = index[1]
        self.parent = parent 

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

def dfs(current,img):

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
    
    if i>=1:
        if img[i-1][j][0] != 0 and img[i-1][j][1] != 0 and img[i-1][j][2] != 0 and img[i-1][j][0] != 127 and img[i-1][j][1] != 127 and img[i-1][j][2] != 127:
            node=Node((i-1,j),current)
            img[i][j][0]=127
            img[i][j][1]=127
            img[i][j][2]=127
            dfs(node,img)
        
    if j>=1:
        if img[i][j-1][0] != 0 and img[i][j-1][1] != 0 and img[i][j-1][2] != 0 and img[i][j-1][0] != 127 and img[i][j-1][1] != 127 and img[i][j-1][2] != 127:
            node = Node((i,j-1),current)
            img[i][j][0]=127
            img[i][j][1]=127
            img[i][j][2]=127
            dfs(node,img)
    
    if j+1<img.shape[1]:
        if img[i][j+1][0] != 0 and img[i][j+1][1] != 0 and img[i][j+1][2] != 0 and img[i][j+1][0] != 127 and img[i][j+1][1] != 127 and img[i][j+1][2] != 127:
            img[i][j][0]=127
            img[i][j][1]=127
            img[i][j][2]=127
            node=Node((i,j+1),current)
            dfs(node,img)

    if i+1<img.shape[0]:
        if img[i+1][j][0] != 0 and img[i+1][j][1] != 0 and img[i+1][j][2] != 0 and img[i+1][j][0] != 127 and img[i+1][j][1] != 127 and img[i+1][j][2] != 127:
            img[i][j][0]=127
            img[i][j][1]=127
            img[i][j][2]=127
            node=Node((i+1,j),current)
            dfs(node,img)


img=cv2.imread("Map Task-1 Part-2.png")
cv2.namedWindow("Map",cv2.WINDOW_NORMAL)
cv2.imshow("Map",img)

start = Node((145,880),None)
stop = Node((563,359),None)

dfs_img=img.copy()
dfs_path=img.copy()
dist_dfs=0
check=0
path_dfs=deque()
dfs(start,dfs_img)
print("Distance = ",dist_dfs)

cv2.waitKey(0)
cv2.destroyAllWindows()