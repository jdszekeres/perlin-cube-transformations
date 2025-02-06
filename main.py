import PIL
from PIL import Image
import numpy as np


source_image = "render copy.png"
output_image = "output.png"

bg_color = "blue"


def main():
    image = Image.open(source_image)
    size = image.size
    print("image is of size", size)
    if size[0] != size[1]:
        print("Image is not square")
        return

    new_image = Image.new("RGB", (size[0], size[1]), bg_color)
    pixels = np.array(new_image)
    tot_pixel = size[0] * size[1]
    image_pixels = np.array(image)  # Convert image to numpy array for faster access

    for i in range(size[0]):  # each row
        cur_pixel = i * size[0]
        # print(cur_pixel / tot_pixel * 100, "%")
        for j in range(size[1]):  # Each column
            pixel = image_pixels[i, j]
            val = pixel[0]

            scale = val / 255 * size[0]  # gets the height of the perlin
            color = 255 - int(i / size[0] * 255)

            # Make each row the same color, with each row overlapping on top of each other
            x = size[0] - int(scale) - 1
            pixels[x:, size[0] - j - 1] = (
                color,
                color,
                color,
            )  # Set the entire row to the same color

        # print(pixel[0], int(scale), color)
    new_image = Image.fromarray(pixels)
    new_image.save(output_image)


main()
