from pprint import pprint

list = []


def function():
    with open('day6_input', 'r') as f:

        sublist = []
        for line in f:
            s = set()
            if line == "\n":
                print(sublist)
                list.append(set.intersection(*sublist))
                sublist.clear()
                pass
                # subset.clear()
            else:
                for char in line.strip():
                    s.add(char)
                sublist.append(s)


function()
print(sum(len(i) for i in list))