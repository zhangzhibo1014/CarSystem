from hyperlpr2 import pipline2 as pp
import cv2
#import sys
import mysql.connector as mysql
import os
import time

path = "D:\\car\\"
this_path = os.getcwd()
flag = os.path.exists(path)

list = os.listdir(path)
length = len(list)

count = 0
while (True):
    start = 0
    list = os.listdir(path)
    length = len(list)
    if length >= 1:
        for i in list:
            filename = path + list[start]
            image = cv2.imread(filename)
            res, resultEnd, img = pp.SimpleRecognizePlate(image)
            cv2.imwrite('img.jpg', img)
            new_plate = ''.join(resultEnd)
            new_plate = new_plate if (new_plate.strip() != "") else ""
            print(new_plate)
            start += 1
            os.remove(filename)
    time.sleep(2)

