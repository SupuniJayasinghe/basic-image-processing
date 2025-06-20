import cv2
import numpy as np


# Function to reduce the number of intensity levels in a grayscale image
def reduce_intensity_levels(img, levels):
    factor = 256 // levels
    return (img // factor) * factor


if __name__ == "__main__":
    img = cv2.imread("../images/image_1.png", cv2.IMREAD_GRAYSCALE)

    reduced = reduce_intensity_levels(img, 4)

    cv2.imwrite("../outputs/reduced_4_levels.jpg", reduced)
    print(np.unique(reduced))
    reduced = reduce_intensity_levels(img, 8)
    cv2.imwrite("../outputs/reduced_8_levels.jpg", reduced)
    print(np.unique(reduced))
