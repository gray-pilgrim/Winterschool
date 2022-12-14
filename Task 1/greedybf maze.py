import time
import cv2
import numpy as np
import random

img = np.full((20,20), 255, 'uint8')
for i in range (0,20) :
    for j in range (0,20) :
        r = random.random()
        if r < 0.2 :
            img[i][j] = 0
cv2.namedWindow('maze', cv2.WINDOW_NORMAL)
cv2.imshow('maze', img.astype(np.uint8))
cv2.waitKey(0)

img_cp = img.copy()

t, w = img.shape
l = input('Enter start coordinate')
start = eval(l)
l = input('Enter end coordinate')
end = eval(l)

def locked(img, p, i):
    if (i[0] == -1 & i[1] == -1):
        if (img[p[0] + i[0]][p[1]] !=0 or img[p[0]][p[1] + i[1]] !=0):
            return False
    elif (i[0] == 1 & i[1] == 1):
        if (img[p[0] + i[0]][p[1]] !=0 or img[p[0]][p[1] + i[1]] !=0):
            return False
    elif (i[0] == 1 & i[1] == -1) :
        if (img[p[0] + i[0]][p[1]] !=0 or img[p[0]][p[1] + i[1]] !=0):
            return False
    elif (i[0] == -1 & i[1] == 1):
        if (img[p[0] + i[0]][p[1]] !=0 or img[p[0]][p[1] + i[1]] !=0):
            return False
    if i == (-1,-1) or i == (1,1) or i == (1,-1) or i == (-1,1):
        return True

    return False

def inv(img, n, m):
    if n>(w-1) or n<0 or m>(t-1) or m<0:
        return True
    elif img[n][m] == 0 :
        return True
    else:
        return False

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)

beg = time.time()
print('astar called')
open = {}
par = np.full((20, 20, 2), -1)
h = np.full((20, 20), np.inf)
g = np.full((20, 20), np.inf)
n = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
p = []
g[start[0]][start[1]] = 0
h[start[0]][start[1]] = 0
open[start] = start
while (len(open) > 0):
    if img[start[0]][start[1]] == 0:
        print("start position is an obstacle")
        break
    midi = np.inf
    p = None
    for v in open:
        if (g[v[0]][v[1]] + h[v[0]][v[1]]) < midi:
            midi = g[v[0]][v[1]] + h[v[0]][v[1]]
            p = v
    c = midi
    print(open)
    open.pop(p)
    if p == end:
        print('Goal reached')
        break
    for i in n:
        con = (p[0] + i[0], p[1] + i[1])

        if not (inv(img, con[0], con[1]) or img[con[0]][con[1]] == 127):
            if not locked(img, p, i):
                img[con[0], con[1]] = 197
                if con in open:
                    if (g[p[0]][p[1]] + dist(con, (p))) < g[con[0]][con[1]]:
                        g[con[0]][con[1]] = (g[p[0]][p[1]] + dist(con, (p)))
                        par[con[0], con[1], 0] = p[0]
                        par[con[0], con[1], 1] = p[1]
                        h[con[0]][con[1]] = dist(con, end)
                else:
                    g[con[0]][con[1]] = (g[p[0]][p[1]] + dist(con, (p)))
                    par[con[0], con[1], 0] = p[0]
                    par[con[0], con[1], 1] = p[1]
                    h[con[0]][con[1]] = dist(con, end)
                    open[con] = con
    img[p[0]][p[1]] = 127

    img_cpy = img.copy()
    img_cpy = cv2.resize(img_cpy, (800, 800), interpolation=cv2.INTER_AREA)
    cv2.imshow("maze", img_cpy)
    cv2.waitKey(100)
cv2.destroyAllWindows()
stop = time.time()
print(stop-beg)
d = 0
if p == end:
    m = (par[end[0]][end[1]][0], par[end[0]][end[1]][1])
    while (True):
        img_cp[m[0]][m[1]] = 127
        d = d + dist(m, (par[m[0]][m[1]][0], par[m[0]][m[1]][1]))
        m = (par[m[0]][m[1]][0], par[m[0]][m[1]][1])
        if m == start:
            break
    print("Distance = {d}")
    cv2.namedWindow('haze', cv2.WINDOW_NORMAL)
    cv2.imshow("haze", img_cp)
    cv2.waitKey(0)
else:
    print('Path not found')

