import copy

f = open('day8_input', 'r').readlines()
orig_data = [f.strip().split(' ') for f in f]


def fix_it(changed_index=0):
    test_data = copy.deepcopy(orig_data)
    if changed_index == 0:
        fixed = is_it_fixed(test_data)
        if fixed:
            return True
    for index in range(len(test_data)):
        if test_data[index][0] != 'acc' and changed_index < index:
            test_data[index][0] = 'jmp' if test_data[index][0] == 'acc' else 'nop'
            changed_index = index
            print(test_data)
            fixed = is_it_fixed(test_data)
            if fixed:
                print(fixed)
                return True
            else:
                return fix_it(changed_index)


def is_it_fixed(data):
    print('---------------New Run--------------')
    acc = 0
    i = 0
    history = []
    while True:
        if i == len(data):
            return True, acc
        command, value = data[i]
        # print(i, command, value)
        if i in history:
            return False
        history.append(i)
        if command == 'nop':
            i += 1
        if command == 'acc':
            acc += int(value)
            print(acc)
            i += 1
        if command == 'jmp':
            i += int(value)


res = fix_it()
print(res)
