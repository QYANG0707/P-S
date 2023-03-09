import os, pickle
from nester import split_line, print_lol

print(os.getcwd())
os.chdir('../文件与异常')
print(os.getcwd())

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            print('ValueError')
    print(man)
    print(other)
except IOError:
    print('the file is missing')

split_line()
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    print(man, file=man_file)
    print(other, file=other_file)
except IOError:
    print('file error')
finally:
    other_file.close()
    man_file.close()
    data.close()

#
split_line('尝试打开不存在文件')
try:
    data = open('missing.txt')
    print(data.readline())
except IOError as err:
    print('File Error:' + str(err))
finally:
    if data in locals():
        data.close()

#使用with不必关心关闭打开的文件
split_line('使用with处理文件')
try:
    with open('man_data.txt', 'w') as man_file:
        print_lol(man, fn=man_file)
    with open('other_data.txt', 'w') as other_file:
        print_lol(other, fn=other_file)
except IOError as err:
    print('File Error:' + str(err))

#
split_line('腌制数据')
try:
    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man, man_file)
    with open('other_data.txt', 'wb') as other_file:
        pickle.dump(other, other_file)
except IOError as err:
    print('File Error:' + str(err))
except pickle.PickleError as perr:
    print('Pickle Error:' + str(perr))

new_man = []
try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle._load(man_file)
except IOError as err:
    print('Io Error:' + str(err))
except pickle.PickleError as perr:
    print('Pickle Error:' + str(perr))
print_lol(new_man)

