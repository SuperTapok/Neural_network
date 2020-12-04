import numpy as np
from PIL import Image


def pool(orig_list, color):
    color_list = np.zeros((orig_list.shape[0], orig_list.shape[1]), dtype=int)
    for i in range(orig_list.shape[0]):
        for j in range(orig_list.shape[1]):
            color_list[i][j] = orig_list[i][j][color]
    pool_list = np.zeros((orig_list.shape[0] // 2, orig_list.shape[1] // 2), dtype=int)
    for k in range(0, pool_list.shape[0]):
        for l in range(0, pool_list.shape[1]):
            max = 0
            for i in range(2):
                for j in range(2):
                    if max <= color_list[2 * k + i][2 * l + j]:
                        max = color_list[2 * k + i][2 * l + j]
            pool_list[k][l] = max
    return pool_list


image = Image.open('example_image.jpg')
image.show()
im2arr = np.array(image)
new_image = np.zeros((im2arr.shape[0]//2, im2arr.shape[1]//2, 3), dtype=int)
red_list = np.zeros((im2arr.shape[0], im2arr.shape[1]), dtype=int)
green_list = np.zeros((im2arr.shape[0], im2arr.shape[1]), dtype=int)
blue_list = np.zeros((im2arr.shape[0], im2arr.shape[1]), dtype=int)
red_list = pool(im2arr, 0)
green_list = pool(im2arr, 1)
blue_list = pool(im2arr, 2)
for i in range(red_list.shape[0]):
    for j in range(red_list.shape[1]):
        new_image[i][j] = red_list[i][j], green_list[i][j], blue_list[i][j]
new_image_arr = np.array(new_image, "uint8")
img = Image.fromarray(new_image_arr, 'RGB')
img.save('new_example_image_pooling.jpg')
img.show()
