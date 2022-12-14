import cv2
import numpy as np
import time

img = cv2.imread("map.png")
cv2.namedWindow("mappie", cv2.WINDOW_NORMAL)
cv2.imshow("mappie", img)
cv2.waitKey(0)
img_cp = img.copy()


t, w = img.shape[:2]

# for i in range(t):
#     for j in range(w):
#         if(img[i][j]!=0 & img[i][j]!=255):
#             if start == (-1, -1):
#                 start = (i, j)
#                 break
#             end = (i,j)

# l = input('Enter start coordinate')
# start = eval(l)
# l = input('Enter end coordinate')
# end = eval(l)
#
start = (147, 880)
end = (564, 359)

def locked(img, p, i):
    if (i[0] == -1 & i[1] == -1):
        if (np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0]) or np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0])):
            return False
    elif (i[0] == 1 & i[1] == 1):
        if (np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0]) or np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0])):
            return False
    elif (i[0] == 1 & i[1] == -1) :
        if (np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0]) or np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0])):
            return False
    elif (i[0] == -1 & i[1] == 1):
        if (np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0]) or np.array_equal(img[[p[0] + i[1]], p[1]], [0,0, 0])):
            return False
    if i == (-1,-1) or i == (1,1) or i == (1,-1) or i == (-1,1):
        return True

    return False

def inv(img, n, m):
    if n>(t-1) or n<0 or m>(w-1) or m<0:
        return True
    elif np.array_equal(img[n][m],[0,0,0]) :
        return True
    return False

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)

beg = time.time()
print('greed called')
open = {}
par = np.full((t, w, 2), -1)
h = np.full((t, w), np.inf)
g = np.full((t, w), np.inf)
n = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
p = []
g[start[0]][start[1]] = 0
h[start[0]][start[1]] = 0
open[start] = start
while (len(open) > 0):
    if (np.array_equal(img[start[0], start[1]], [0,0,0])):
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

        if not (inv(img, con[0], con[1]) or np.array_equal(img[con[0], con[1]],[127,127,127])):
             if not locked(img, p, i):
                img[con[0], con[1]] = [197,197,197]
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
    img[p[0], p[1]] = [127, 127, 127]
    if inv(img, p[0], p[1]):
        break
    img_cpy = img.copy()
    img_cpy = cv2.resize(img_cpy, (800, 800), interpolation=cv2.INTER_AREA)
    cv2.imshow("maze", img_cpy)
    cv2.waitKey(1)
cv2.destroyAllWindows()
stop = time.time()
print(stop-beg)
d = 0
if p == end:
    m = (par[end[0]][end[1]][0], par[end[0]][end[1]][1])
    while (True):
        img_cp[m[0]][m[1]] = [0,255,0]
        d = d + dist(m, (par[m[0]][m[1]][0], par[m[0]][m[1]][1]))
        m = (par[m[0]][m[1]][0], par[m[0]][m[1]][1])
        if m == start:
            break
    print(f"Distance = {d}")
    cv2.namedWindow('haze', cv2.WINDOW_NORMAL)
    cv2.imshow("haze", img_cp)
    cv2.waitKey(0)
else:
    print('Path not found')

