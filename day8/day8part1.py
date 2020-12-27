f = open('day8_input', 'r').readlines()
data = [tuple(f.strip().split(' ')) for f in f]

acc = 0
i = 0
history = []
while True:
    command, value = data[i]
    print(i, command, value)
    if i in history:
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