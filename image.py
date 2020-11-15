import numpy as np
from PIL import Image

im = Image.open('puppy.jpg')  # Can be many different formats.
im2arr = np.array(im)

for h in range(im2arr.shape[0]):
    for w in range(im2arr.shape[1]):
        for c in range(im2arr.shape[2]):
            if c == 0:
                tmp = round(im2arr[h, w, c] + 75)
                tmp = tmp if tmp <= 255 else 255
                tmp = tmp if tmp >= 0 else 0
                im2arr[h, w, c] = tmp
            # if c == 1:
            #     tmp = round(im2arr[h, w, c] + 75)
            #     tmp = tmp if tmp <= 255 else 255
            #     tmp = tmp if tmp >= 0 else 0
            #     im2arr[h, w, c] = tmp
            #  if c == 2:
            #      tmp = round(im2arr[h, w, c] + 75)
            #      tmp = tmp if tmp <= 255 else 255
            #      tmp = tmp if tmp >= 0 else 0
            #      im2arr[h, w, c] = tmp

img = Image.fromarray(im2arr, 'RGB')
img.save('puppy.png')
img.show()
