import cv2
import numpy as np
import math

image = cv2.imread("map.png")
cv2.namedWindow("Path Planning",cv2.WINDOW_NORMAL)

n,m,l = image.shape

yellow = [0,255,255]

####

#djikstra

closed_list = []
queue = []
min_distance = np.full((n,m),np.inf)
visited = np.full((n,m), False)
parent = np.full((n,m), None)

def dijsktra(img, start, stop):

    global parent
    queue.append(start)
    min_distance[start[0],start[1]] = 0
    visited[start[0],start[1]] = True
    parent[start[0],start[1]] = None
    node = None

    while(len(queue) != 0):

        cv2.imshow("Path Planning",img)
        cv2.waitKey(1)

        node = queue.pop(0)
        closed_list.append(node)

        if(node == stop):
            break
        (i,j) = node
        for i1 in range(i-1,i+2):
            for j1 in range(j-1,j+2):
                if(i1 < 0 or j1 < 0 or i1 >= n or j1 >= m):
                    continue
                elif (np.array_equal(img[i1,j1], [255,255,255]) == True or (i1,j1) == stop) and (i1,j1) not in closed_list:

                    dist = math.sqrt((i1-i)**2 + (j1-j)**2)

                    if(visited[i1,j1] == True):
                        if(dist + min_distance[i,j] < min_distance[i1,j1]):
                            min_distance[i1,j1] = dist + min_distance[i,j]
                            parent[i1,j1] = node

                    else:
                        queue.append((i1,j1))
                        min_distance[i1,j1] = min_distance[i,j] + dist 
                        parent[i1,j1] = node
                        visited[i1,j1] = True
                        if(np.array_equal(img[i1,j1], [255,255,255])):
                            img[i1,j1] = yellow

####

start = (145,880) 
stop = (563,359)


img_djiksktra = image.copy()
img_djiksktra_path = image.copy()
dijsktra(img_djiksktra,start,stop)

#Path for djiksktra

cv2.namedWindow("Path",cv2.WINDOW_NORMAL)

stack = []

node = stop

while(node != None):
    
    stack.append(node)
    node = parent[node[0]][node[1]]


while(len(stack) != 0):

    x = stack.pop()
    for i in range(-1,2):
        for j in range(-1,2):
            img_djiksktra_path[i + x[0], j + x[1]] = (255,0,127)

    cv2.imshow("Path",img_djiksktra_path)
    cv2.waitKey(2)


####

cv2.waitKey(0)
cv2.destroyAllWindows()