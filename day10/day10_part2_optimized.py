import functools
import math

f = open('day10_input', 'r').readlines()
data = [int(str.strip()) for str in f]
sorted_data = sorted(data)

START = 0
END = max(sorted_data) + 3

sorted_data.insert(0, START)
sorted_data.append(END)
print(sorted_data)


def recursive(list):
    if len(list) == 1 or len(list) == 2:
        return 1
    else:
        if len(list) >= 4 and list[-4] == list[-1] - 3:
            return recursive(list[:-1]) + recursive(list[:-2]) + recursive(list[:-3])
        if len(list) >= 3 and list[-3] >= list[-1] - 3:
            return recursive(list[:-1]) + recursive(list[:-2])
        else:
            return recursive(list[:-1])


@functools.lru_cache()
def recursive_optimized(pos):
    if pos == 0 or pos == 1:
        return 1
    else:
        if pos >= 3 and sorted_data[pos - 3] == sorted_data[pos] - 3:
            return recursive_optimized(pos - 1) + recursive_optimized(pos - 2) + recursive_optimized(pos - 3)
        if pos >= 2 and sorted_data[pos - 2] >= sorted_data[pos] - 3:
            return recursive_optimized(pos - 1) + recursive_optimized(pos - 2)
        else:
            return recursive_optimized(pos - 1)


last_item_index = len(sorted_data) - 1
print(recursive_optimized(last_item_index))
