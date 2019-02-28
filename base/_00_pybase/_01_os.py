'''
Created on 2018年12月6日
os和os.path模块的重要方法
'''
import os
import stat
import shutil

print("---------------------os------------------------")
# print('os.remove',os.remove('01/xx.txt'))                     #删除文件
# print('os.unlink',os.unlink('01/xx.txt'))                     #删除文件
# print('os.rename',os.rename('01/a.txt','01/b.txt'))           #重命名文件
print('os.chdir',os.chdir('01'))                                #改变当前工作目录
print('os.listdir',os.listdir('011'))                           #列出指定目录下所有文件
print('os.getcwd',os.getcwd())                                  #获取当前文件路径
# print('os.mkdir',os.mkdir('aa/'))                             #新建目录
# print('os.rmdir',os.rmdir('01/aa/bb/cc'))                     #删除空目录(删除非空目录, 使用shutil.rmtree())
# print('os.makedirs',os.makedirs('011/aa/bb/cc'))              #创建多级目录
# print('os.removedirs',os.removedirs('01/aa/bb/cc') )          #删除多级目录
print('os.stat',os.stat("xx.txt"))                              #获取文件属性
print('os.chmod',os.chmod("xx.txt",stat.S_IXOTH))               #修改文件权限 http://www.runoob.com/python/os-chmod.html
print('os.utime',os.utime("xx.txt",(1330712280, 1330712292)))   #修改文件时间戳 http://www.runoob.com/python/os-utime.html
print('os.name',os.name)            #该变量返回当前操作系统的类型，当前只注册了3个值：分别是posix , nt , java， 对应linux/windows/java虚拟机
# os.system()         #执行操作系统命令
# os.execvp()         #启动一个新进程
# os.fork()           #获取父进程ID，在子进程返回中返回0
# os.execvp()         #执行外部程序脚本（Uinx）
# os.spawn()          #执行外部程序脚本（Windows）
# os.access(path, mode) #判断文件权限(详细参考cnblogs)


print("---------------------os.path------------------------")
filename= "/aaa/bbb/ccc/dd.txt"
dirname= "/aaa/bbb/ccc"
basename= "dd.txt"
list = ["/aaa","/aaa/bbb","/aaa/bbb/ccc","/aaa/bbb/ccc/dd.txt"]
print('os.path.split:',os.path.split(filename))                 #将文件路径和文件名分割(会将最后一个目录作为文件名而分离)
print('os.path.splitext:',os.path.splitext(filename))           #将文件路径和文件扩展名分割成一个元组
print('os.path.dirname:',os.path.dirname(filename) )            #返回文件路径的目录部分
print('os.path.basename:',os.path.basename(filename))           #返回文件路径的文件名部分
print('os.path.join:',os.path.join(dirname,basename))           #将文件路径和文件名凑成完整文件路径
print('os.path.abspath:',os.path.abspath(filename) )            #获得绝对路径
print('os.path.splitunc:',os.path.splitunc(filename))           #把路径分割为挂载点和文件名
print('os.path.normpath:',os.path.normpath(filename))           #规范path字符串形式
print('os.path.exists:',os.path.exists(filename))               #判断文件或目录是否存在
print('os.path.isabs:',os.path.isabs(filename))                 #如果path是绝对路径，返回True
print('os.path.realpath:',os.path.realpath(filename))           #返回path的真实路径
print('os.path.relpath:',os.path.relpath(filename,'aaa'))       #从start开始计算相对路径,以'aaa'目录开始 
print('os.path.normcase:',os.path.normcase(filename) )          #转换path的大小写和斜杠
print('os.path.isdir:',os.path.isdir(filename))                 #判断name是不是一个目录，name不是目录就返回false
print('os.path.isfile:',os.path.isfile(filename))               #判断name是不是一个文件，不存在返回false
print('os.path.islink:',os.path.islink(filename))               #判断文件是否连接文件,返回boolean
print('os.path.ismount:',os.path.ismount(filename))             #指定路径是否存在且为一个挂载点，返回boolean
# print('os.path.samefile:',os.path.samefile(filename,filename))       #是否相同路径的文件，返回boolean
print('os.path.getatime:',os.path.getatime("xx.txt"))           #返回最近访问时间 浮点型
print('os.path.getmtime:',os.path.getmtime("xx.txt"))           #返回上一次修改时间 浮点型
print('os.path.getctime:',os.path.getctime("xx.txt"))           #返回文件创建时间 浮点型
print('os.path.getsize:',os.path.getsize("xx.txt"))             #返回文件大小 字节单位
print('os.path.commonprefix:',os.path.commonprefix(list))       #返回list(多个路径)中，所有path共有的最长的路径
print('os.path.lexists:',os.path.lexists(filename))             #路径存在则返回True,路径损坏也返回True
print('os.path.expanduser:',os.path.expanduser(filename) )      #把path中包含的""和"user"转换成用户目录
print('os.path.expandvars:',os.path.expandvars(filename))       #根据环境变量的值替换path中包含的”$name”和”${name}”
# print('os.path.sameopenfile:',os.path.sameopenfile(filename, filename))  #判断fp1和fp2是否指向同一文件
# os.path.samestat(stat1, stat2)  #判断stat tuple stat1和stat2是否指向同一个文件
print('os.path.splitdrive:',os.path.splitdrive(filename))        #一般用在windows下，返回驱动器名和路径组成的元组
# os.path.walk(path, visit, arg)  #遍历path，给每个path执行一个函数详细见手册
print('os.path.supports_unicode_filenames:',os.path.supports_unicode_filenames)     #设置是否支持unicode路径名

shutil.copyfile('cursrcpath','curtargetpath')       #复制文件