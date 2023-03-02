import os
from nester import split_line
#打开文件
the_file = open('sketch.txt')

#处理
#处理

#关闭文件
the_file.close()

#当前工作目录
print(os.getcwdb())

data = open('sketch.txt')

#readline()获取一个数据行
print(data.readline(), end='')
print(data.readline(), end='')
print(end='\n')
split_line()

#seek(0)回到文件初始位置
data.seek(0)
for each_line in data:
    print(each_line, end='')
print(end='\n')
split_line()

data.seek(0)
for each_line in data:
    if not each_line.find(':') == -1:
        (msg1, msg2) = each_line.split(':', 1)
        print(msg1 + ' said: ' + msg2, end='')
print(end='\n')
split_line()

data.seek(0)
for each_line in data:
    try:
        (msg1, msg2) = each_line.split(':', 1)
        print(msg1 + ' said: ' + msg2, end='')
    except ValueError:
        print("exception:ValueError")
print(end='\n')
split_line(20, 'try except')
data.close()
