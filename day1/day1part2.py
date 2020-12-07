d = {}
d2 = {}
list = []
def function():
    with open('day1_input', 'r') as f:
        for line in f:
            num = int(line)
            list.append(num)
            substract = 2020-num
            d[num] = substract
        for k,v in d.items():
            d2.clear()
            for num2 in list:
                if (num2) in d2:
                    return k, d2[num2], num2
                else:
                    d2[v-num2] = num2


print(function())
