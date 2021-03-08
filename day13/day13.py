f = open('input', 'r').readlines()
data = [str.strip() for str in f]

time_stamp = int(data[0])
schedule = [int(i) for i in data[1].split(',') if i != 'x']
print(time_stamp)
print(schedule)


def get_bus():
    local_timestamp = time_stamp
    while True:
        for bus in schedule:
            if local_timestamp % bus == 0:
                return local_timestamp, bus
        local_timestamp += 1


time, bus = get_bus()
diff = (time - time_stamp)
print(diff * bus)
