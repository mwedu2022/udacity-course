import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Load the example grid image
image = mpimg.imread('example_grid1.jpg')

# Convert image to BGR format (OpenCV uses BGR, not RGB)
image_cv = cv2.cvtColor((image * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)

def perspect_transform(img, src, dst):
    """
    Apply perspective transform to an image
    
    Args:
        img: Input image
        src: Source points (4 corners)
        dst: Destination points (4 corners)
    
    Returns:
        warped: Transformed image
    """
    # Get transform matrix using cv2.getPerspectiveTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    # Return the result
    return warped

# Define calibration box in source (actual) and destination (desired) coordinates
# These source and destination points are defined to warp the image
# to a grid where each 10x10 pixel square represents 1 square meter
dst_size = 5 
# Set a bottom offset to account for the fact that the bottom of the image 
# is not the position of the rover but a bit in front of it
bottom_offset = 6

# Source points - the 4 corners of a grid cell in the original image
source = np.float32([[14, 140], [301, 140], [200, 96], [118, 96]])

# Destination points - create a square at the bottom center of the output image
destination = np.float32([
    [image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
    [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
    [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset], 
    [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset]
])

# Apply the perspective transform
warped = perspect_transform(image, source, destination)

# Make copies for drawing (so we don't modify original)
image_marked = image.copy()
warped_marked = warped.copy()

# Draw Source and destination points on images (in blue) before plotting
# OpenCV uses BGR format, so blue is (255, 0, 0)
# cv2.polylines(image_marked, np.int32([source]), True, (0, 0, 255), 3)
# cv2.polylines(warped_marked, np.int32([destination]), True, (0, 0, 255), 3)

# Display the original image and the transformed result
# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 6), sharey=True)
# f.tight_layout()
# ax1.imshow(image_marked)
# ax1.set_title('Original Image with Source Points', fontsize=40)

# ax2.imshow(warped_marked, cmap='gray')
# ax2.set_title('Perspective Transform Result (Top-Down View)', fontsize=40)
# plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
# plt.show()

