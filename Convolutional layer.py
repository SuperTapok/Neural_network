import numpy as np

print("Generating the original list: ")
#creating a new list
orig_list = np.random.randint(0, 2, size=(5, 5))
#generating the original list
print(orig_list)

print("Expending of this list: ")
#creating a expended list
exp_list = np.zeros((orig_list.shape[0]+2, orig_list.shape[1]+2), dtype=int)
for i in range(1, orig_list.shape[1]+1):
    for j in range(1, orig_list.shape[0]+1):
        exp_list[i][j] = orig_list[i-1][j-1]
#expending original list(every row)
for i in range(1, orig_list.shape[1]+1):
    exp_list[i][0] = orig_list[i-1][0]
    exp_list[i][exp_list.shape[1]-1] = orig_list[i-1][orig_list.shape[1]-1]
#adding the first expended row
a_list = np.zeros((orig_list.shape[0]+2), dtype=int)
a_list[0] = orig_list[0][0]
for i in range(1, orig_list.shape[0]+1):
    a_list[i] = orig_list[0][i-1]
a_list[a_list.shape[0]-1] = orig_list[0][orig_list.shape[0]-1]
exp_list[0] = a_list
#adding the last expended row
b_list = np.zeros((orig_list.shape[0]+2), dtype=int)
b_list[0] = orig_list[orig_list.shape[0] - 1][0]
for i in range(1, orig_list.shape[0]+1):
    b_list[i] = orig_list[orig_list.shape[0]-1][i-1]
b_list[b_list.shape[0]-1] = orig_list[orig_list.shape[0]-1][orig_list.shape[1]-1]
exp_list[exp_list.shape[0]-1] = b_list
print(exp_list)

print("Generating the core: ")
#creating a core
core_list = np.random.randint(0, 2, size=(3, 3))
print(core_list)

print("Convolutional list: ")
#creating a convolutional list
conv_list = np.zeros((orig_list.shape[0], orig_list.shape[1]), dtype=int)
for i in range(orig_list.shape[0]):
    for j in range(orig_list.shape[1]):
        k = 0
        for h in range(core_list.shape[0]):
            for l in range(core_list.shape[1]):
                k = k + exp_list[h+i][l+j]*core_list[h][l]
        conv_list[i][j] = k
print(conv_list)

print("Convolutional list: ")
#creating a convolutional list
conv_list = np.zeros((orig_list.shape[0], orig_list.shape[1]), dtype=int)
for i in range(orig_list.shape[0]):
    for j in range(orig_list.shape[1]):
        k = 0
        for h in range(core_list.shape[0]):
            for l in range(core_list.shape[1]):
                k = k + exp_list[h+i][l+j]*core_list[h][l]
        conv_list[i][j] = k
print(conv_list)

