import random
import math

previous_layer_list = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
print("Previous layer: ", previous_layer_list)
x = int(input("Enter number of neurons:"))
weights_list = []
for i in range(x):
    weights_list.append([random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)])
print("Weights: ", weights_list)
sum_list = []
for i in range(len(previous_layer_list)):
    for j in range(x):
        sum = 0
        for k in range(3):
            sum = sum + previous_layer_list[i]*weights_list[j][k]
        sum_list.append(sum)
y_list = []
for i in range(x):
    y_list.append(1/(1+math.exp(-sum_list[i])))
print("Output values:", y_list)
