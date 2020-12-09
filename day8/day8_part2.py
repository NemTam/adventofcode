f = open('day8_input_test', 'r').readlines()
orig_data = [(f.strip().split(' ')) for f in f]

finish = False


def flip_code(data, i):
    if data[i][0] == 'jmp':
        data[i][0] = 'nop'
    else:
        data[i][0] = 'jmp'

changed_index = -1
while finish is not True:
    data = orig_data.copy()
    acc = 0
    changed = False
    history = []
    i = 0
    changed_index += 1
    while True:
        print(f'{i}, {data[i][0]}, {data[i][1]} history: {history}, changed_index: {changed_index}')
        if changed is False and data[i][0] != 'acc' and changed_index < i:
            print('flippin')
            flip_code(data, i)
            changed_index = i
            changed = True
        command, value = data[i]

        if i in history:
            print('nem jo')
            print(data)
            break
        if i == len(data) - 1:
            print('vege')
            finish = True
            print(data)
            break
        history.append(i)
        if command == 'nop':
            i += 1
        if command == 'acc':
            acc += int(value)
            i += 1
        if command == 'jmp':
            i += int(value)

print(history)
print(acc)
