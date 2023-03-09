from nester import split_line


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as err:
        print('IO Error:' + str(err))


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

# with open('james.txt') as jaf:
#     data = jaf.readline()
#     james = data.strip().split(',')
# with open('julie.txt') as juf:
#     data = juf.readline()
#     julie = data.strip().split(',')
# with open('mikey.txt') as mif:
#     data = mif.readline()
#     mikey = data.strip().split(',')
# with open('sarah.txt') as saf:
#     data = saf.readline()
#     sarah = data.strip().split(',')

split_line('输出所有时间')
print(james)
print(julie)
print(mikey)
print(sarah)


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


split_line('输出排序时间')
print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
