import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
pic = Image.open(r"Section 2\\bear.jpg")

# Convert the image to a numpy array
pic_arr = np.asarray(pic)

# Display the shape of the array
print(f"Array shape: {pic_arr.shape}")

# Create a copy of the array for modifying the channels
pic_red = pic_arr.copy()
print((pic_arr))

# Create subplots for displaying the channels
fig, axes = plt.subplots(2, 3)

# Display the red, green, and blue channels
axes[0, 0].imshow(pic_red[:, :, 0], cmap="gray")
axes[0, 0].set_title("Red Channel")
axes[0, 1].imshow(pic_red[:, :, 1], cmap="gray")
axes[0, 1].set_title("Green Channel")
axes[0, 2].imshow(pic_red[:, :, 2], cmap="gray")
axes[0, 2].set_title("Blue Channel")

# Modify the red channel
pic_red_modified = pic_red.copy()
pic_red_modified[:, :, 0] = 0
axes[1, 0].imshow(pic_red_modified)
axes[1, 0].set_title("Modified Red Channel")

# Modify the green channel
pic_green_modified = pic_red.copy()
pic_green_modified[:, :, 1] = 0
axes[1, 1].imshow(pic_green_modified)
axes[1, 1].set_title("Modified Green Channel")

# Modify the blue channel
pic_blue_modified = pic_red.copy()
pic_blue_modified[:, :, 2] = 0
axes[1, 2].imshow(pic_blue_modified)
axes[1, 2].set_title("Modified Blue Channel")

# Adjust the layout and display the subplots
plt.tight_layout()
plt.show()

# Create subplots for displaying the modified channels
fig, axes = plt.subplots(1, 3)
