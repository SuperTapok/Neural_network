import random
import numpy as np

print("Generating the original list: ")
#creating a new list
orig_list = np.random.randint(0, 2, size = (5, 5))
#generating the original list
print(orig_list)

print("Expending of this list: ")
#creating a expended list
exp_list = orig_list
#expending original list(every row)
for i in range(orig_list.shape[1]):
    np.insert(exp_list[i], 0, orig_list[i][0])
    np.append(exp_list[i], orig_list[i][orig_list.shape[1]-1])
print(exp_list)
# a_list = [orig_list[0][0]]#adding the first expended row
# for i in range(0, len(orig_list)):
#     a_list.append(orig_list[0][i])
# a_list.append(orig_list[0][len(orig_list[0])-1])
# exp_list.insert(0, a_list)
#
# b_list = [orig_list[len(orig_list[0]) - 1][0]]#adding the last expended row
# for i in range(0, len(orig_list[0])):
#     b_list.append(orig_list[len(orig_list[0])-1][i])
# b_list.append(orig_list[len(orig_list[0])-1][len(orig_list[0])-1])
# exp_list.insert(len(exp_list[0]), b_list)
#
# for i in range(0, len(exp_list[0])):#expended list
#     print(exp_list[i])


# print("Generating the core: ")
# #creating a core
# core_list = np.random.randint(0, 2, size = (3, 3))
# #generating the core
#
#
#
# print("Convolutional list: ")
# #creating a convolutional list
# conv_list = []
# for i in range(len(orig_list[0])):
#     conv_list.append([])
#     for j in range(len(orig_list[0])):
#         k = 0
#         for h in range(len(core_list[0])):
#             for l in range(len(core_list[0])):
#                 k = k + exp_list[h+i][l+j]*core_list[h][l]
#         conv_list[i].append(k)
#     print(conv_list[i])

