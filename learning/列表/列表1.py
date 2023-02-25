'''
创建数组
1.数据添加引号,将内容转换为字符串
2.逗号隔开
3.以中括号开头和结尾
4.赋值给一个标识符
'''
movies = ['The Hole Grail', 'The Life of Brian', 'The Meaning of Life']

#使用中括号加下标访问变量
print(movies[0])  #The Hole Grail
print(movies[1])  #The Life of Brian

#获取列表长度
print(len(movies))  #3

#append():追加元素
movies.append('movies1')

#pop():删除末尾元素
movies.pop()

#extend():追加一个数据集合
movies.extend(['movies2', 'movies3'])
print(movies)
#remove():删除特定数据
movies.remove('movies2')
movies.remove('movies3')
print(movies)

#insert(index,obj):指定位置插入数据
movies.insert(3, 'movies4')
print(movies)

#while迭代
print('-----while循环迭代-----')
count = 0
while count < len(movies):
    print(movies[count])
    count += 1

#for迭代
for each_item in movies:
    print(each_item)
'''
python列表可以做更多的事情,像是打了激素的数组
列表可以伸缩,不支持越界检查
无法访问一个不存在的元素,如若访问发生IndexError错误
使用转义字符使用特定符号
标识符赋值后才可使用
'''
#for循环只能迭代最外层列表
print('--------------------')
movies = [
    'The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
    [
        'Graham CHapman',
        [
            'Michael Palin', 'John Cleese', 'Terry Gilliam', ' Eric Idle',
            'Terry Jones'
        ]
    ]
]
for each_item in movies:
    print(each_item)

#在列表中查找列表
print('-----在列表中查找列表-----')
#isinstance()检查数据类型
print(isinstance(movies, list))  #True


#输出当前列表以及内部列表的所有元素
def is_list(list_):
    for each_item in list_:
        if isinstance(each_item, list):
            is_list(each_item)
        else:
            print(each_item)


is_list(movies)

#python3默认递归深度不能超过100
