import numpy as np
from PIL import Image


def conv(color, core, arr):
    exp_list = np.zeros((arr.shape[0] + 2, arr.shape[1] + 2), dtype=int)
    for i in range(1, arr.shape[0] + 1):
        for j in range(1, arr.shape[1] + 1):
            exp_list[i][j] = arr[i - 1][j - 1][color]


    for i in range(1, arr.shape[0] + 1):#expending original list(every row)
        exp_list[i][0] = arr[i - 1][0][color]
        exp_list[i][exp_list.shape[1] - 1] = arr[i - 1][arr.shape[1] - 1][color]

    # adding the first expended row
    a_list = np.zeros((arr.shape[1] + 2), dtype=int)
    a_list[0] = arr[0][0][color]
    for i in range(1, arr.shape[1] + 1):
        a_list[i] = arr[0][i - 1][color]
    a_list[a_list.shape[0] - 1] = arr[0][arr.shape[1] - 1][color]
    exp_list[0] = a_list

    # adding the last expended row
    b_list = np.zeros((arr.shape[1] + 2), dtype=int)
    b_list[0] = arr[arr.shape[0] - 1][0][color]
    for i in range(1, arr.shape[1] + 1):
        b_list[i] = arr[arr.shape[0] - 1][i - 1][color]
    b_list[b_list.shape[0] - 1] = arr[arr.shape[0] - 1][arr.shape[1] - 1][color]
    exp_list[exp_list.shape[0] - 1] = b_list

    conv_list = np.zeros((arr.shape[0], arr.shape[1]), dtype=int)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            summa = 0
            tmp = 0
            for h in range(core.shape[0]):
                for l in range(core.shape[1]):
                    summa = summa + exp_list[h + i][l + j] * core[h][l]
                    tmp = summa
                    tmp = tmp // 9
                    tmp = tmp if tmp <= 255 else 255
                    tmp = tmp if tmp >= 0 else 0
            conv_list[i][j] = tmp
    return conv_list


image = Image.open('puppy.jpg')
image.show()
im2arr = np.array(image)
print("Generating the core: ")
core_list = np.random.randint(0, 2, size=(3, 3))
print(core_list)

new_image = np.zeros((im2arr.shape[0], im2arr.shape[1], 3), dtype=int)
red_list = conv(0, core_list, im2arr)
green_list = conv(1, core_list, im2arr)
blue_list = conv(2, core_list, im2arr)
for i in range(red_list.shape[0]):
    for j in range(red_list.shape[1]):
        new_image[i][j] = red_list[i][j], green_list[i][j], blue_list[i][j]
new_image_arr = np.array(new_image, "uint8")
img = Image.fromarray(new_image_arr, 'RGB')
img.save('new_example_image.png')
img.show()

