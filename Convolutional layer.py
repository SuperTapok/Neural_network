import random

print("Generating the original list: ")
#creating a new list
orig_list = []
#generating the original list
for i in range(5):
    orig_list.append([])
    for j in range(5):
        orig_list[i].append(random.randint(0, 1))
    print(orig_list[i])


print("Expending of this list: ")
#creating a expended list
exp_list = []
for i in orig_list:
    exp_list.append(list(i))
#expending original list(every row)
for i in range(len(orig_list[1])):
    exp_list[i].insert(0, orig_list[i][0])
    exp_list[i].append(orig_list[i][len(orig_list[i])-1])

a_list = [orig_list[0][0]]#adding the first expended row
for i in range(0, len(orig_list)):
    a_list.append(orig_list[0][i])
a_list.append(orig_list[0][len(orig_list[0])-1])
exp_list.insert(0, a_list)

b_list = [orig_list[len(orig_list[0]) - 1][0]]#adding the last expended row
for i in range(0, len(orig_list[0])):
    b_list.append(orig_list[len(orig_list[0])-1][i])
b_list.append(orig_list[len(orig_list[0])-1][len(orig_list[0])-1])
exp_list.insert(len(exp_list[0]), b_list)

for i in range(0, len(exp_list[0])):#expended list
    print(exp_list[i])


print("Generating the core: ")
#creating a core
core_list = []
#generating the core
for i in range(3):
    core_list.append([])
    for j in range(3):
        core_list[i].append(random.randint(0, 1))
    print(core_list[i])


print("Convolutional list: ")
#creating a convolutional list
conv_list = []
for i in range(len(orig_list[0])):
    conv_list.append([])
    for j in range(len(orig_list[0])):
        k = 0
        for h in range(len(core_list[0])):
            for l in range(len(core_list[0])):
                k = k + exp_list[h+i][l+j]*core_list[h][l]
        conv_list[i].append(k)
    print(conv_list[i])

