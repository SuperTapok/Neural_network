import numpy as np
from PIL import Image
import random


def conv(color, core, arr):
    exp_list = []
    for i in range(arr.shape[0]):
        exp_list.append([])
        for j in range(arr.shape[1]):
            exp_list[i].append(arr[i, j, color])

    for i in range(arr.shape[0]):
        exp_list[i].insert(0, arr[i, 0, color])
        exp_list[i].append(arr[i, arr.shape[1]-1, color])

    a_list = [arr[0, 0, color]]  #adding the first expended row
    for i in range(0, arr.shape[1]):
        a_list.append(arr[0, i, color])
    a_list.append(arr[0, arr.shape[1]-1, color])
    exp_list.insert(0, a_list)

    b_list = [arr[0, arr.shape[0]-1, color]]  #adding the last expended row
    for i in range(0, arr.shape[0]):
        b_list.append(arr[i, arr.shape[1]-1, color])
    b_list.append(arr[arr.shape[0]-1, arr.shape[1]-1])
    exp_list.insert(len(exp_list[0]), b_list)

    conv_list = []
    for i in range(0, arr.shape[0]-1):
        conv_list.append([])
        for j in range(0, arr.shape[1]-1):
            k = 0
            tmp = 0
            for h in range(len(core[0])):
                for l in range(len(core[0])):
                    k = k + exp_list[h + i][l + j] * core[h][l]
                    tmp = k
                    tmp = tmp//9
                    tmp = tmp if tmp <= 255 else 255
                    tmp = tmp if tmp >= 0 else 0
            conv_list[i].append(tmp)
        # print(conv_list[i])
    return conv_list


image = Image.open('example_image.jpg')
image.show()
im2arr = np.array(image)
print("Generating the core: ")
core_list = []
# [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
for i in range(3):
    core_list.append([])
    for j in range(3):
        core_list[i].append(random.randint(0, 1))
    print(core_list[i])
new_image = []
red_list = conv(0, core_list, im2arr)
green_list = conv(1, core_list, im2arr)
blue_list = conv(2, core_list, im2arr)
for i in range(len(red_list)):
    new_image.append([])
    for j in range(len(red_list)):
        new_image[i].append([red_list[i][j], green_list[i][j], blue_list[i][j]])
new_image_arr = np.array(new_image, "uint8")
img = Image.fromarray(new_image_arr, 'RGB')
img.save('new_example_image.png')
img.show()

