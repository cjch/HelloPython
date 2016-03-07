# HelloPython

##chama.py
iOS中插码时，将字符串定义成变量。将所有的事件定义集中到文件中，然后批量进行处理。

```
// @"EventCode"
extern NSString * const EventCode;			// .h
NSString * const EventCode = @"EventCode";	// .m
```

##中文编码
Python默认使用ASCII格式，要正确解析中文需要在文件头添加`#coding=utf-8` 或 `#-*- coding:utf-8 -*-`

##基础语法
Python区分大小写，关键字只包含小写字母

以下划线开头的标识符有特殊意义，单下划线开头表示不能直接访问的类属性`_foo`，需通过接口进行访问； 以双下划线开头的代表类的私有成员，`__foo`； 以双下划线开头和结尾的代表python特殊方法专用的标识，`__init__()` 代表类的构造函数

**python不使用大括号来控制代码块，而是使用缩进，同一个代码块中的语句必须包括相同的缩进空白数量，并且不能混合使用空格和Tab**

通常以新行作为语句的结束符，使用**`\`**将一行语句分成多行显示，如果语句包含[],{},()等括号就不需要多行连接符

以单引号，双引号，三引号`''', """`表示字符串。三引号可由多行组成。

单行注释使用`#`开头

等待用户输入使用`raw_input(...)`

同一行可以使用多条语句，使用分号隔开

缩进相同的一组语句构成一个代码块(代码组)，通常以关键字开头，以冒号结尾。

##变量类型

数字Number：int, long, float, 复数complex（a+bj）；字符串String，列表List，元组Tuple，字典Dictionary

使用del删除对象的引用

字符串有两种取值顺序：从左到右默认0开始，从右往左默认-1开始

截取字符串使用`[头下标:尾下标]`

`+`为字符串连接操作符，`*`为重复操作

列表用`[]`标识，截取操作和字符串类似

元组用`()`标识，是只读类型

##运算符

幂运算符`**`，取整除运算符，返回商的整数部分`//`

不等于运算符：`!= 或 <>`

逻辑运算符： `and, or, not`

成员运算符：`in, not in` 在指定序列中是否存在指定值

身份运算符：`is, is not` 判断两个标识符是否引用同一个对象

##语句

python不支持switch，只能使用多个elif来实现

```
if condition:
	state1
elif condition1:
	state2
else:
	state3

```

`pass`语句是空语句，只是为了保持程序结构的完整性。

循环语句可使用else语句，该语句在循环正常完成后执行。


##日期和时间

```
#import time;		#时间
#import calendar;	#日期
```

##函数

```
def functionName ( parameters ):
	"函数第一行可以使用文档字符串，存放函数说明"
	function body
	return [expression] #选择性的返回值

def printParam ( str ):
	"打印任何传入的字符串"
	print str
	return

```

函数的所有参数是按引用传递

命名参数可乱序传入

不定参数，即函数的参数数目不定，添加`*`号的变量名存放所有的未命名参数。声明如下：

``` 
def functionname ( [formal_args,] *var_args_tuple ):
//其他类似
return [expr]
```

匿名函数 使用lambda创建，lambda只是一个表达式，拥有自己的名字空间，不能访问参数列表之外或全局空间中的参数。

```
lambda [arg1 [,arg2, /// argn]]: expression

#示例
sum = lambda a, b: a + b

print sum(1, 5)
print sum (11, 9)
```

##模块

模块名对应一个.py源文件(moduleName <--> moduleName.py)。

`from`可以从模块中导入指定的部分

```
import moduleName [, module2, ...]

from moduleName import name1 [, name2 ...]
from moduleName import * 	#导入所有内容

```

python自动假设在函数内赋值的变量都是局部的，否则需要使用`global`语句

`dir()` 返回一个模块里定义的名字列表

`globals() locals()` 返回全局或局部空间中的名字

由于一个模块被导入时只会执行一次，重新执行模块顶层部分的代码需使用`reload() `

##文件IO

打印： `print`

读取键盘输入：   
`raw_input`: 从标准输入中读取一行并返回字符串(去掉结尾的换行符)  
`input`: 和`raw_input`类似，但还可接收表达式作为输入并返回运算结果

###文件
```
open(fileName [, accessMode] [, buffering])
close()
write(string) 	#写入的字符串可以是二进制数据，该方法不再字符串结尾添加换行符
read([count]) 	#参数为可选，传入要读取得字节数
tell() 			#文件当前位置
seek( offset [, from] )

# os模块 
rename(current_file_name, new_file_name)
remove(file_name)
mkdir("newDir")
chdir("newDir")		#改变当前目录
getcwd()				#获取当前目录
rmdir("dirname")
```

##异常处理
```
try:
	statement		#运行代码
except name1:
	statement1		#如果try部分引发了name1异常时执行
except name1, data1:
	statement2		#如果try部分引发了name1异常，获得了附加的数据
else:
	statement3		#如果try部分没有异常发生
	

try:
	statement1
finally:
	statement2		#退出try时总会执行
	

raise	[exception]	#主动触发异常
```

##面向对象

类方法的第一个参数必须为self

```
class Object:
	'类的帮助信息'   				#类文档字符串
	classProperty = 0 			#类变量
	
	def __init__(self, v1):		#初始化方法
		self.property1 = v1		
		Object.classProperty = 1
		
	def display(self):
		print "instance: " + self.value1
		print "Object: %d" Object.classProperty
	
	def __del__(self):			#析构函数
		class_name = self.__class__.__name__
		print class_name, "销毁"
		

class SubObject(Object):		#继承语法	
...

#子类和实例判断
issubclass()
isinstance(Obj, Class)
```

访问属性使用`.`语法，也可使用：

```
getattr(obj, name[, default])
hasattr(obj, name)
setattr(obj, name, value)
delattr(obj, name)
```
不允许实例访问私有数据，但可以借助`instance._className__attrName`访问私有属性。

使用引用计数追踪内存中的对象，管理对象的销毁。跟oc不同，python有循环垃圾收集器，用来清理未引用的循环。