id_list = []


def function():
    with open('day5_input', 'r') as f:

        for line in f:
            row = [i for i in range(128)]
            seat = [i for i in range(8)]
            for char in line:
                if char == 'B':
                    row = row[len(row) // 2:]
                if char == 'F':
                    row = row[:len(row) // 2]
                if char == 'L':
                    seat = seat[:len(seat) // 2]
                if char == 'R':
                    seat = seat[len(seat) // 2:]
            print(row, seat)
            id_list.append(row[0] * 8 + seat[0])
    return id_list


# Solution 1
print(max(function()))

# Solution 2
sorted = (sorted(id_list))
for index, item in enumerate(sorted):
    if sorted[index] + 1 != sorted[index+1]:
        print(sorted[index] +1)
        break
