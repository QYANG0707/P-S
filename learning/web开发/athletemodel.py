import pickle
from nester import split_line


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        # 获取最快的三组成绩
        return(sorted(set([sanitize(t) for t in self]))[0:3])

    def add_time(self, time_value):
        # 添加一组成绩
        self.times.append(time_value)

    def add_times(self, list_of_times):
        # 添加多组成绩
        self.times.extend(list_of_times)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print('IOError:' + str(ioerr))


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store):' + str(ioerr))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store):' + str(ioerr))
    return all_athletes


the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
split_line('打印所有数据')
print(data)

split_line('打印所有名字')
for each_athlete in data:
    print(data[each_athlete].name + ' ' + data[each_athlete].dob)

split_line()
data_copy = get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)
