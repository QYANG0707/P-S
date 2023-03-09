import sys


#输出当前列表以及内部列表的所有元素
def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fn)
        else:
            if indent:
                for tap_stop in range(level):
                    print('\t', end='', file=fn)
            print(each_item, file=fn)


def split_line(msg='',num=20):
    print('-' * int(num / 2) + msg + '-' * int(num / 2))
