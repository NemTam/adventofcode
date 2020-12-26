f = open('day10_input', 'r').readlines()
data = [int(str.strip()) for str in f]
sorted_data = sorted(data)

START = 0
END = max(sorted_data)
print(sorted_data, '\n')
list_of_sets = []
accumulator = 0


def super_bad_recursive(current_set, index):
    try:
        for i, j in [(x, y) for x in [1, 2, 3] for y in [1, 2, 3]]:
            if sorted_data[index + i] == max(current_set) + j:
                local_set = current_set.copy()
                local_set.add(sorted_data[index + i])
                index += i
                super_bad_recursive(local_set, index)
    except IndexError:
        if max(current_set) == max(sorted_data):
            list_of_sets.append(current_set)
            global accumulator
            accumulator += 1


def super_bad_recursive_optimized(current_val, index):
    try:
        for i, j in [(x, y) for x in [1, 2, 3] for y in [1, 2, 3]]:
            if sorted_data[index + i] == current_val + j:
                local_val = sorted_data[index + i]
                index += i
                super_bad_recursive_optimized(local_val, index)
    except IndexError:
        if current_val == max(sorted_data):
            global accumulator
            accumulator += 1


super_bad_recursive_optimized(START, -1)
print(accumulator)

# accumulator = 0
# recursive({START}, -1)
# print(accumulator)
