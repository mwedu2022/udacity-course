import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image = mpimg.imread('example_grid1.jpg')
plt.imshow(image)
plt.show()

import cv2
import numpy as np

def perspect_transform(img, src, dst):

    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    return warped

source = np.float32([
    [14, 140],   # A
    [301, 140],  # B
    [200, 96],   # C
    [118, 96]    # D
])
destination = np.float32([
    [50, 200],
    [250, 200],
    [250, 0],
    [50, 0]
])

warped = perspect_transform(image, source, destination)
plt.imshow(warped)
plt.show()

