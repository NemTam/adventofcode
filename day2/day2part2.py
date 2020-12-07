def function():
    valid_count = 0
    with open('day2_input', 'r') as f:
        for line in f:
            min = int(line.split('-')[0])
            max = int(line.split('-')[1].split(' ')[0])
            rule = line.split(' ')[1].replace(':', '')
            password = line.split(' ')[-1]
            if (password[min - 1] == rule) != (password[max - 1] == rule):
                valid_count += 1

    return valid_count


print(function())
