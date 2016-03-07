# coding=utf-8

class HelloClass (object):
	"hello python class"
	totalCount = 0

	def __init__(self, name):
		print "parent init"
		self.name = name
		HelloClass.totalCount += 1

	def  display(self):
		print "name:", self.name, "totalCount: ", HelloClass.totalCount
	
	def __del__(self):
		className = self.__class__.__name__
		print "dealloc:", className


class SubHelloClass (HelloClass):
	def __init__(self, name, value):
		print "subclass init"
		# 两种调用父类的方法
		#1 调用未绑定的父类方法
		HelloClass.__init__(self, name)
		#2 要使下面的代码生效，需要时父类继承object，如此才能使用super函数
		#super(SubHelloClass, self).__init__(name)
		self.value = value



hc1 = HelloClass("jack")
hc2 = HelloClass("mark")
hc1.display()
hc2.display()

hc1.age = 10
print hc1.age
del hc1.age

if hasattr(hc1, 'age'):
	print "age:", hc1.age
else:
	print "instance not has attribute 'age'"

#inner class attrs
print "HelloClass.__doc__:", HelloClass.__doc__
print "HelloClass.__name__", HelloClass.__name__
print "HelloClass.__module__:", HelloClass.__module__
print "HelloClass.__bases__", HelloClass.__bases__
print "HelloClass.__dict__:", HelloClass.__dict__

subHc1 = SubHelloClass("jeff", 18)
print subHc1
