import cv2
import random as rn
import numpy as np

class car:
    def __init__(self,rrpm,lrpm):

        self.rrpm = rrpm
        self.lrpm = lrpm

my_car = car(0,0)

file = open("Car Reading.txt","w")
file.write("\n")
file.write("Motor Readings\n")
file.write("\n")

p = []
templates = [cv2.imread("30.png"),cv2.imread("60.png"),cv2.imread("bumper.png"),cv2.imread("green.jpeg"),cv2.imread("left.png"),cv2.imread("red.jpg"),cv2.imread("right.jpg"),cv2.imread("road.jpg"),cv2.imread("slow.jpg"),cv2.imread("stop.png"),cv2.imread("uturnleft.jpg"),cv2.imread("uturnright.jpg")]

for i in range (25):

    r = rn.random()

    if r < 0.05:
        l = cv2.imread('red2.jpg', cv2.IMREAD_COLOR)
        #l = cv2.resize(l, (600, 800))
        p.append(l)
        if r < 0.5:
            l = cv2.imread('green2.jpg', cv2.IMREAD_COLOR)
        else:
            l = cv2.imread('green3.jpeg',cv2.IMREAD_COLOR)
    elif r<0.1:
        l = cv2.imread('red3.jpg', cv2.IMREAD_COLOR)
        #l = cv2.resize(l, (600, 800))
        p.append(l)
        if r < 0.5:
            l = cv2.imread('green2.jpg', cv2.IMREAD_COLOR)
        else:
            l = cv2.imread('green3.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.15:
        l = cv2.imread('uturnleft2.jpg', cv2.IMREAD_COLOR)
    elif r < 0.2:
        l = cv2.imread('uturnright2.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.25:
        l = cv2.imread('left2.jpg', cv2.IMREAD_COLOR)
    elif r < 0.3:
        l = cv2.imread('left3.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.35:
        l = cv2.imread('right2.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.4:
        l = cv2.imread('right3.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.45:
        l = cv2.imread('slow2.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.5:
        l = cv2.imread('hump2.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.55:
        l = cv2.imread('301.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.6:
        l = cv2.imread('601.jpeg', cv2.IMREAD_COLOR)
    elif r < 0.65:
        l = cv2.imread('stop1.jpeg',cv2.IMREAD_COLOR)
    else:
        l = cv2.imread('road.jpg',cv2.IMREAD_COLOR)
    #l = cv2.resize(l,(600, 800))
    p.append(l)

cv2.namedWindow("Video",cv2.WINDOW_NORMAL)

c = 0
for i in range(0, len(p)):

    cv2.imshow("Video",p[i])
    
    for j in templates:

        j = c%10
        c = c+1
        template = templates[j]
        ##if template found

        if(j == 0):
            my_car.lrpm = my_car.rrpm = 60

        elif(j == 1):
            my_car.lrpm = my_car.rrpm = 120

        elif(j == 2):
            
            my_car.lrpm = my_car.rrpm = 40

        elif(j == 3):
            my_car.lrpm = my_car.rrpm = 100

        elif(j == 4):

            my_car.lrpm = 20
            my_car.rrpm = 60

        elif(j == 5):

            my_car.lrpm = my_car.rrpm = 0

        elif(j == 6):

            my_car.rrpm = 20
            my_car.lrpm = 60

        elif(j == 7):

            my_car.lrpm = my_car.rrpm = 100

        elif(j == 8):

            my_car.lrpm = my_car.rrpm = 40

        elif(j == 9):

            my_car.lrpm = my_car.rrpm = 0

        elif(j == 10):

            my_car.lrpm = 0
            my_car.rrpm = 50

        elif(j == 11):

            my_car.lrpm = 50
            my_car.rrpm = 0

        file.writelines(f"Left Motor rpm = {my_car.lrpm}   Right Motor rpm = {my_car.rrpm}")
        file.write("\n")

        cv2.waitKey(2000)

        break
    
        ##

file.close()
cv2.destroyAllWindows()