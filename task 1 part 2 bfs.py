import cv2
import numpy as np
from collections import deque

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
        mat[current.x][current.y][0] = 255
        mat[current.x][current.y][1] = 0
        mat[current.x][current.y][2] = 0
        current = current.parent
    cv2.imshow("path using bfs",mat)
    cv2.waitKey(0)
    return dist

def bfs(img,start,end):
    q = deque()
    q.append(start)
    
    while len(q):
        current = q.popleft()
        i,j = current.x, current.y
        
        if j+1<img.shape[1] :
            if img[i][j+1][0] != 0 and img[i][j+1][1] != 0 and img[i][j+1][2] != 0 and img[i][j+1][0] != 127 and img[i][j+1][1] != 127 and img[i][j+1][2] != 127:
                if i==end.x and j==end.y:
                    break
                img[i][j+1][0]=127
                img[i][j+1][1]=127
                img[i][j+1][2]=127
                n=Node((i,j+1),current)
                q.append(n)
                cv2.imshow("path using bfs",img)
                cv2.waitKey(1)

        if i+1<img.shape[0] :
            if img[i+1][j][0] != 0 and img[i+1][j][1] != 0 and img[i+1][j][2] != 0 and img[i+1][j][0] != 127 and img[i+1][j][1] != 127 and img[i+1][j][2] != 127:
                if i==end.x and j==end.y:
                    break
                img[i+1][j][0]=127
                img[i+1][j][1]=127
                img[i+1][j][2]=127
                n=Node((i+1,j),current)
                q.append(n)
                cv2.imshow("path using bfs",img)
                cv2.waitKey(1)

        if i>=1 :
            if img[i-1][j][0] != 0 and img[i-1][j][1] != 0 and img[i-1][j][2] != 0 and img[i-1][j][0] != 127 and img[i-1][j][1] != 127 and img[i-1][j][2] != 127:
                if i==end.x and j==end.y:
                    break
                img[i-1][j][0]=127
                img[i-1][j][1]=127
                img[i-1][j][2]=127
                n=Node((i-1,j),current)
                q.append(n)
                cv2.imshow("path using bfs",img)
                cv2.waitKey(1)

        if j>=1:
            if img[i][j-1][0] != 0 and img[i][j-1][1] != 0 and img[i][j-1][2] != 0 and img[i][j-1][0] != 127 and img[i][j-1][1] != 127 and img[i][j-1][2] != 127:
                if i==end.x and j==end.y:
                    break
                img[i][j-1][0]=127
                img[i][j-1][1]=127
                img[i][j-1][2]=127
                n=Node((i,j-1),current)
                q.append(n)
                cv2.imshow("path using bfs",img)
                cv2.waitKey(1)
    dist = show_path(start,current,img)
    return dist

img=cv2.imread("Map Task-1 Part-2.png")
cv2.namedWindow("Map",cv2.WINDOW_NORMAL)
cv2.imshow("Map",img)

start = Node((145,880),None)
end = Node((563,359),None)
dist = bfs(img,start,end)
print("Distance = ",dist)

cv2.waitKey(0)
cv2.destroyAllWindows()