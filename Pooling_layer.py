import numpy as np

orig_list = np.random.randint(1, 6, size=(6, 14))
print('Original list: ')
print(orig_list)
pool_list = np.zeros((orig_list.shape[0]//2, orig_list.shape[1]//2), dtype=int)
for k in range(0, pool_list.shape[0]):
    for l in range(0, pool_list.shape[1]):
        max = 0
        for i in range(2):
            for j in range(2):
                if max <= orig_list[2*k+i][2*l+j]:
                    max = orig_list[2*k+i][2*l+j]
        pool_list[k][l] = max
print('Pooling list: ')
print(pool_list)
