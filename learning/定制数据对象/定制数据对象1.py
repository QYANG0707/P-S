from nester import split_line
split_line()

split_line('将代码及其数据打包在类中')
class AthleteList(list):
	def __init__(self,a_name,a_dob=None,a_times=[]):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
	def top3(self):
		# 获取最快的三组成绩
		return(sorted(set([sanitize(t) for t in self]))[0:3])

	def add_time(self,time_value):
		# 添加一组成绩
		self.times.append(time_value)

	def add_times(slef,list_of_times):
		# 添加多组成绩
		self.times.extend(list_of_times)


def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
			templ = data.strip().split(',')
			return AthleteList(templ.pop(0),templ.pop(0),templ)
	except IOError as ioerr:
		print('IOError:'+str(ioerr))

sarah = get_coach_data('sarah2.txt')
# (sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
# print(sarah_name+"'s fastest times are:"+str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

split_line('使用字典关联数据')
# sarah_data = {}
# sarah_data['Name'] = sarah.pop(0)
# sarah_data['Dob'] = sarah.pop(0)
# sarah_data['Times'] = sarah
# print(sarah_data['Name']+"'s fastest times are"+str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
print(sarah.name+"'s fastest times are"+str(sarah.top3()))
vera = AthleteList('Vera Vi')
vera.append('1.31')
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())







