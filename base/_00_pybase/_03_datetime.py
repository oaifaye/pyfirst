'''
Created on 2018年12月6日

datetime模块
'''
import datetime
from calendar import monthrange

obj = datetime.datetime.strptime('2014-03-16 12:21:21',"%Y-%m-%d %H:%M:%S")
print('datetime.date.today():',datetime.date.today())           #本地日期对象,(用str函数可得到它的字面表示(2014-03-24))
print('datetime.date.isoformat():',datetime.date.isoformat(datetime.date.today()))    #当前[年-月-日]字符串表示(2014-03-24)
# print('datetime.date.fromtimestamp():',datetime.date.fromtimestamp())   #返回一个日期对象，参数是时间戳,返回 [年-月-日]
print('datetime.date.weekday():',datetime.date.weekday(datetime.date.today()))      #返回一个日期对象的星期数,周一是0
# print('datetime.date.isoweekday():',datetime.date.isoweekday(obj))   #返回一个日期对象的星期数,周一是1
# print('datetime.date.isocalendar():',datetime.date.isocalendar(obj))  #把日期对象返回一个带有年月日的元组
# print('datetime.datetime.isocalendar():',datetime.datetime.today() )      #返回一个包含本地时间(含微秒数)的datetime对象 2014-03-24 23:31:50.419000
print('datetime.datetime.now():',datetime.datetime.now())     #返回指定时区的datetime对象 2014-03-24 23:31:50.419000
# print('datetime.datetime.utcnow():',datetime.datetime.utcnow())      #返回一个零时区的datetime对象
# print('datetime.fromtimestamp():',datetime.fromtimestamp(timestamp[,tz]))      #按时间戳返回一个datetime对象，可指定时区,可用于strftime转换为日期表示
# d = datetime.datetime.fromtimestamp(datetime.datetime.now())
# str1 = d.strftime("%Y-%m-%d %H:%M:%S.%f")
# print('datetime.fromtimestamp():',str1)
#  
# print('datetime.utcfromtimestamp():',datetime.utcfromtimestamp(timestamp))        #按时间戳返回一个UTC-datetime对象
print('datetime.datetime.strptime():',datetime.datetime.strptime('2014-03-16 12:21:21',"%Y-%m-%d %H:%M:%S")) #将字符串转为datetime对象
print('datetime.datetime.strftime():',datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d %H%M%S')) #将datetime对象转换为str表示形式
# print('datetime.date.today().timetuple():',datetime.date.today().timetuple())           #转换为时间戳datetime元组对象，可用于转换时间戳
# print('datetime.datetime.now().timetuple():',datetime.datetime.now().timetuple())
# print('time.mktime():',time.mktime(timetupleobj))                   #将datetime元组对象转为时间戳
# print('time.time():',time.time())                     #当前时间戳
# print('time.localtime:',time.localtime)
# print('time.gmtime:',time.gmtime)

print('--------------------时间加减法---------------------------')
a = datetime.datetime.strptime('2018-12-1 12:21:21',"%Y-%m-%d %H:%M:%S")
b = datetime.datetime.strptime('2018-12-10 12:21:25',"%Y-%m-%d %H:%M:%S")
print('b-a天数:',(b-a).days)
print('b-a秒数（只比秒数）:',(b-a).seconds)
print('b-a秒数（总秒数）:',(b-a).total_seconds())
print('b加一周零一天',(b+datetime.timedelta(days=1) +datetime.timedelta(weeks=1) ).strftime("%Y-%m-%d %H:%M:%S"))

#增加一个月
print('b加一个月',(b + datetime.timedelta(days=monthrange(b.year,b.month)[1])*6).strftime("%Y-%m-%d %H:%M:%S"))

