def function():
    valid_count = 0
    with open('day2_input', 'r') as f:
        for line in f:
            min = int(line.split('-')[0])
            max = int(line.split('-')[1].split(' ')[0])
            rule = line.split(' ')[1].replace(':', '')
            password = line.split(' ')[-1]
            if min <= password.count(rule) <= max:
                valid_count+= 1
    return valid_count

print(function())