from pprint import pprint

list = []


def function():
    with open('day6_input', 'r') as f:

        subset = set()
        for line in f:
            if line == "\n":
                list.append(subset.copy())
                subset.clear()
            else:
                for char in line.strip():
                    subset.add(char)


function()
print(sum(len(i) for i in list))