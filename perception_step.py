import matplotlib.image as mpimg
import matplotlib.pyplot as plt

filename = 'sample.jpg'
image = mpimg.imread(filename)
# plt.imshow(image)
# plt.show()

import numpy as np

# print(image.dtype, image.shape, np.min(image), np.max(image))

red_channel = np.copy(image)
red_channel[:, :, [1, 2]] = 0
green_channel = np.copy(image)
green_channel[:, :, [0, 2]] = 0
blue_channel = np.copy(image)
blue_channel[:, :, [0, 1]] = 0


# fig = plt.figure(figsize=(12, 3))
# plt.subplot(131)
# plt.imshow(red_channel)
# plt.subplot(132)
# plt.imshow(green_channel)
# plt.subplot(133)
# plt.imshow(blue_channel)
# plt.show()

def color_thresh(img, rgb_thresh=(0, 0, 0)):
    color_select = np.zeros_like(img[:, :, 0])

    above_thresh = (img[:, :, 0] > rgb_thresh[0]) \
                   & (img[:, :, 1] > rgb_thresh[1]) \
                   & (img[:, :, 2] > rgb_thresh[2])

    color_select[above_thresh] = 1

    return color_select


red_threshold = 160
green_threshold = 160
blue_threshold = 160

rgb_threshold = (red_threshold, green_threshold, blue_threshold)

color_select = color_thresh(image, rgb_thresh=rgb_threshold)


# Відображаємо оригінал та результат
# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
# f.tight_layout()
# ax1.imshow(image)
# ax1.set_title('Original Image', fontsize=40)

# ax2.imshow(color_select, cmap='gray')
# ax2.set_title('Your Result', fontsize=40)
# plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
# plt.show()

def rotate_pix(xpix, ypix, yaw):

    # Convert yaw to radians
    yaw_rad = np.deg2rad(yaw)

    # Apply rotation
    x_rotated = xpix * np.cos(yaw_rad) - ypix * np.sin(yaw_rad)
    y_rotated = xpix * np.sin(yaw_rad) + ypix * np.cos(yaw_rad)

    return x_rotated, y_rotated


def translate_pix(xpix_rot, ypix_rot, xpos, ypos, scale):

    # Apply scaling and translation
    x_world = np.int_(xpos + (xpix_rot / scale))
    y_world = np.int_(ypos + (ypix_rot / scale))

    return x_world, y_world

