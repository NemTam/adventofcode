d = {}

def function():
    with open('day1_input', 'r') as f:
        for line in f:
            num = int(line)
            substract = 2020-num
            if (num) in d:
                return d[num] * num
            else:
                d[substract] = num

print(function())