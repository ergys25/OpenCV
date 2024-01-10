import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"Section 4//bear.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
plt.imshow(img)
plt.show()
