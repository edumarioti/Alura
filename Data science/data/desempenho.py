import numpy as np

np_array = np.arange(1000000)
py_list = list(range(1000000))

%time for _ in range(100): np_array *= 2
