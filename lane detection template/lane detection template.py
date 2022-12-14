import numpy as np
#Taking input
p = input("Enter name of file:")
#Capturing video
vid = cv2.VideoCapture(p)
#processing each scene
while (1):
    #reading each scene
    tf, sc = vid.read()
    #checking for error
    print(tf)
    #coverting to grayscale
    gr = cv2.cvtColor(sc, cv2.COLOR_BGR2GRAY)
    #initializing kernel
    ker = (1,1)
    #Blurring to denoise
    er = cv2.GaussianBlur(gr, ker, 0)
    #extracting edges
    ed = cv2.Canny(er, 100, 200)
    #dilating and making edges prominent
    dl = cv2.dilate(ed, (5, 5))
    #extracting shape
    n, m = dl.shape
    #defining region of interest
    reg = np.array([
                    [(0,n),(0,550),(m/2-50, n/2), (m/2+50, n/2), (m, 550), (m, n)]
                    ], 'int32')
    #declaring maskarray with zeroes
    mask = np.zeros_like(dl)
    #filling polygon
    mask = cv2.fillPoly(mask, reg, 255)
    #applying mask on image
    tr = cv2.bitwise_and(dl, mask)
    #doing Hough transformations
    ht = cv2.HoughLinesP(tr, 2, np.pi / 180, 200, np.array([]), minLineLength=40, maxLineGap=10)
    #Extracting desired lines
    for line in ht:
        x1, y1, x2, y2 = line[0]
        cv2.line(sc, (x1, y1), (x2, y2), (255, 0, 127), 5)
    #outputting video
    cv2.imshow("Vid",sc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
