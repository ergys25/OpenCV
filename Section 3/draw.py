import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)

cv2.rectangle(blank_img, pt1=(384, 10), pt2=(500, 150), color=(0, 255, 0), thickness=10)
cv2.rectangle(
    blank_img, pt1=(200, 200), pt2=(300, 300), color=(0, 0, 255), thickness=10
)
cv2.circle(blank_img, center=(100, 100), radius=50, color=(255, 0, 0), thickness=8)
cv2.circle(blank_img, center=(400, 400), radius=50, color=(255, 0, 0), thickness=-1)
cv2.line(blank_img, pt1=(0, 0), pt2=(512, 512), color=(102, 255, 255), thickness=5)
cv2.putText(
    blank_img,
    text="Hello",
    org=(10, 500),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=4,
    color=(255, 255, 255),
    thickness=3,
    lineType=cv2.LINE_AA,
)


plt.imshow(blank_img)
plt.show()
