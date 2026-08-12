import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from perspective_transform_solution import  perspect_transform, source, destination
from perception_step import color_thresh

# Read in the same sample image as before
image = mpimg.imread('sample.jpg')

warped = perspect_transform(image, source, destination)
colorsel = color_thresh(warped, rgb_thresh=(160, 160, 160))

# Plot the result
plt.imshow(colorsel, cmap='gray')
plt.show()

ypos, xpos = colorsel.nonzero()
plt.plot(xpos, ypos, '.')
plt.xlim(0, 320)
plt.ylim(0, 160)
plt.show()

def rover_coords(binary_img):

    # Get non-zero pixel positions
    ypos, xpos = binary_img.nonzero()

    # Convert image coordinates to rover-centric coordinates
    x_pixel = (binary_img.shape[0] - ypos).astype(float)
    y_pixel = (binary_img.shape[1] / 2 - xpos).astype(float)

    return x_pixel, y_pixel
    xpix, ypix = rover_coords(colorsel)

xpix, ypix = rover_coords(colorsel)

plt.figure(figsize=(5, 7.5))
plt.plot(xpix, ypix, '.')
plt.ylim(-160, 160)
plt.xlim(0, 160)
plt.title('Rover-centric map')
plt.show()