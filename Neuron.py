import numpy as np


def func_of_act(x):
    return 1/(1+np.exp(-x))


input_values = np.random.randint(0, 10, size=3)
print("Input values: ", input_values)

f = int(input("Enter number of neurons: "))

weights = np.zeros((f, 3), dtype=int)
for i in range(f):
    weights[i] = np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2)
print("Weights: ", weights)

sum_list = np.zeros(f, dtype=int)
for i in range(input_values.shape[0]):
    for j in range(f):
        sum = 0
        for k in range(3):
            sum = sum + input_values[i]*weights[j][k]
        sum_list[j] = sum
y_list = np.zeros(f, dtype=float)
for i in range(f):
    y_list[i] = func_of_act(sum_list[i])
print("Output values:", y_list)
