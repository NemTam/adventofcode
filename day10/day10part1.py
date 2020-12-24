import itertools

f = open('day10_input', 'r').readlines()
data = [int(str.strip()) for str in f]

sorted_data = sorted(data)
print(sorted_data)

one_adapter = 0
three_adapter = 0
for index, value in enumerate(sorted_data):
    try:
        print(sorted_data[index + 1], value)
        if sorted_data[index + 1] == value + 1:
            one_adapter += 1
        elif sorted_data[index + 1] == value + 2:
            print('kettes adapter')
        elif sorted_data[index + 1] == value + 3:
            three_adapter += 1
        else:
            print('shieeeeeet')
    except IndexError:
        print('vege')
        pass

print(one_adapter + 1)
print(three_adapter + 1)
