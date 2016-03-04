
#-*- coding:utf-8 -*-

# 单行注释
print "hello world!"

print "你好，世界！" # 单行注释

# 语句块对齐
if True:
	print "true"
	print "true1"
else:
	print "false"
	print "false1"

#多行注释
sComment = '''
多行注释，使用单引号。
多行注释，使用单引号。
'''
dComment = """
多行注释，使用双引号。
多行注释，使用双引号。
多行注释，使用双引号。
"""

print sComment
print dComment

# 字符串
str = "I love python" 
print str
print str[2:6]
print str[2:]
print str[0]

print str * 2
print str + " Test"

# 运算符
a, b = 10, 3
c = a**b	#幂运算
d = a//b	#整除
print c, d

t1 = 0; t2 = 10
r1 = t1 and t2
if r1:
	print "true"
else:
	print "false"

#语句
count = 0
while count < 5:
	print count, " is less than 5"
	count += 1
else:
	print count, " is not less than 5"

#time & calendar
import time, calendar

tick = time.time()
localTime = time.localtime(tick)
localTime1 = time.asctime(localTime)
print tick
print localTime
print localTime1
print time.timezone, time.tzname

cal = calendar.month(2016, 3)
print cal

print calendar.monthcalendar(2016, 3)
print calendar.calendar(2016)


#函数
def funcSum ( arg1, arg2 ):
	"返回两个数的和"
	total = arg1 + arg2
	return total


lmdSum = lambda a1, a2: a1 + a2 #匿名函数 lambda表达式

print funcSum(11, 12)
print lmdSum(11, 12)

total = 0

def funAdd ( arg1, arg2 ):
	global total
	total = arg1 + arg2
	return total

print total
print funAdd(1, 2)
print total

