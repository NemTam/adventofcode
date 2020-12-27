import itertools
import numpy as np

f = open('day11_input', 'r').readlines()
data = [str.strip().replace('L', '0').replace('.', '7').replace('#', '1') for str in f]
cleaned_data = [list(map(int, l)) for l in data]

OCCUPIED = 1
EMPTY = 0
FLOOR = 8

DELTAS = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x or y)]

def compare_neighbors(arr):
    comp_arr = np.copy(arr)
    for (x, y), item in np.ndenumerate(arr):
        if item == FLOOR:
            continue
        occupied_neighbours = 0
        # Check Around
        for x_offset, y_offset in DELTAS:
            try:
                if arr[x + x_offset, y + y_offset] == OCCUPIED and (x + x_offset >= 0 and y + y_offset >= 0):
                    occupied_neighbours += 1
            except IndexError:
                continue
        if occupied_neighbours >= 4 and item == OCCUPIED:
            comp_arr[x, y] = EMPTY
        if occupied_neighbours == 0 and item == EMPTY:
            comp_arr[x, y] = OCCUPIED

    return comp_arr


data1 = np.array(cleaned_data)
while True:
    data2 = compare_neighbors(data1)
    data1 = compare_neighbors(data2)
    if (data1 == data2).all():
        print(np.count_nonzero(data1 == 1))
        break
