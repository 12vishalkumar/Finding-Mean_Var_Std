import numpy as np
N, M = map(int, input().split())
arr = np.array([input().split() for i in range(N)], dtype = float)
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.round(arr.std(), decimals=11))


