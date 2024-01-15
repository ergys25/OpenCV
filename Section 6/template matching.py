import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the full image and the face image
full = cv2.imread(r"DATA/sammy.jpg")
full = cv2.cvtColor(full, cv2.COLOR_BGR2RGB)
face = cv2.imread(r"DATA/sammy_face.jpg")
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

# Define the template matching methods
methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED,
]

# Create subplots to display the results
fig, axs = plt.subplots(2, len(methods), figsize=(20, 10))

# Perform template matching for each method
for i, method in enumerate(methods):
    full_copy = full.copy()
    res = cv2.matchTemplate(full_copy, face, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Determine the top left and bottom right coordinates of the detected template
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    height, width, channels = face.shape
    bottom_right = (top_left[0] + width, top_left[1] + height)

    # Draw a rectangle around the detected template on the full image
    cv2.rectangle(full_copy, top_left, bottom_right, 255, 10)

    # Display the heatmap of template matching and the detection of the template
    axs[0, i].imshow(res)
    axs[0, i].set_title("Heatmap of template matching")
    axs[1, i].imshow(full_copy)
    axs[1, i].set_title("Detection of template")
    axs[0, i].set_xticks([])
    axs[0, i].set_yticks([])
    axs[1, i].set_xticks([])
    axs[1, i].set_yticks([])


# Adjust the layout and display the plot
plt.tight_layout()
plt.show()
