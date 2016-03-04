#coding=utf-8

import os

cfName = raw_input("please input code file: ")

try:
	codeFile = open(cfName, "r")
except:
	print "打开文件失败，请检查文件名和路径后重新开始"
else:
	codeHFile = open("chamaCode.h", "wb")
	codeMFile = open("chamaCode.m", "wb")

	print "start processing content of file: " + cfName
	str = codeFile.readline()
	while(len(str) > 0):
		pstr = str[0:len(str)-1]
		print pstr
		hStr = "extern NSString * const " + pstr + ";\n"
		mStr =  "NSString * const " + pstr + " = @\"" + pstr + "\";\n"

		codeHFile.write(hStr)
		codeMFile.write(mStr)

		str = codeFile.readline()

	print "prcess finished"
	codeFile.close()
	codeHFile.close()
	codeMFile.close()
