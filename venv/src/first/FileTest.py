import os,time

filepath = "D:\develop\PythonProjects\\venv\\resource\\"
filename = "hello.txt"

print("--------------")
print(os.getcwd())
'''
删除文件夹测试
'''
print("begin remove dir")
# os.rmdir(),如果要删除的目录下含有文件或文件夹，则不能删除，提示：OSError: [WinError 145] 目录不是空的
os.rmdir("D:\develop\PythonProjects\\venv\\resource\\test1\\test2")
print("end remove dir")


'''
写文件和读文件测试
'''
fo = open(filepath + filename, "w")
print("文件名：",fo.name)
print("访问模型：",fo.mode)
print("是否已关闭：",fo.closed)

fo.write("www.runoob.com!\nVery good site!\n")
# 关闭打开的文件
fo.close()

'''
读取文件里的内容
'''
# 打开一个文件
fo = open(filepath + filename, "r+")
str = fo.read(10)
str2 = fo.readline(10)
print("读取的字符串是 : ", str)
print("读取的字符串 str2 是 : ", str2)

# tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后
# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print("重新读取字符串 : ", str)

# 关闭打开的文件
fo.close()

'''
重命名文件和删除文件测试
'''
print("begin modify filename")
# time.sleep(10)
# os.rename(filepath + filename,filepath + "jay.txt")
print("end modify filename")

print("begin remove file")
# time.sleep(10)
# os.remove(filepath + "jay.txt")
print("end remove file")
