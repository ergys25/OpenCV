import cv2
import numpy as np
import matplotlib.pyplot as plt

################
### FUNCTION ###
################


def draw_circle(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


def draw_rectangle(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x + 100, y + 100), (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, (x, y), (x + 100, y + 100), (255, 0, 0), -1)


cv2.namedWindow(winname="my_img")
cv2.setMouseCallback("my_img", draw_circle)


################################################
####### SHOWING IMAGES WITH MATPLOTLIB #########
################################################


img = np.zeros(shape=(512, 512, 3), dtype=np.int8)

while True:
    cv2.imshow("my_img", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break
