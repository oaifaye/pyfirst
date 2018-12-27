'''
Created on 2018年12月7日

'''

print('capitalize:','abcdef ghjk'.capitalize())          #把字符串的第一个字符大写
print('center:','[abcdefghjk]'.center(20,'*'))           #返回一个原字符串居中，并使用空格填充到width长度的新字符串,第一个参数要大于字符串长度
print('ljust:','[abcdefghjk]'.ljust(20,'*'))                #返回一个原字符串左对齐，用空格填充到指定长度的新字符串
print('rjust:','[abcdefghjk]'.rjust(20,'*'))    #返回一个原字符串右对齐，用空格填充到指定长度的新字符串
print('zfill:','100'.zfill(30))    #返回字符串右对齐，前面用0填充到指定长度的新字符串
print('count:','abc cde def'.count('c',0,5))    #返回子字符串在原字符串出现次数，beg,len是范围
print('encode:','abc cde def'.encode(encoding='UTF-8'))# 编码string
d = '这是中文哟'.encode(encoding='UTF-8')
print('decode:',d.decode(encoding='UTF-8'))  #解码string,出错引发ValueError异常
print('endswith:','abc cde def'.endswith('f',1,3))  #字符串是否以substr结束，beg,end是范围
print('startswith:','abc cde def'.startswith('a',1,3))  #字符串是否以substr开头，beg,end是范围
print('expandtabs:','abc    cde    def'.expandtabs(tabsize = 5))     #把字符串的tab转为空格，默认为8个
print('find:','abc cde def'.find('c',0,5))        #查找子字符串在字符串第一次出现的位置，否则返回-1
print('index:','abc cde def'.index('c',0,5))    #查找子字符串在指定字符中的位置，不存在报异常
print('isalnum:','abccdedef1'.isalnum())       #检查字符串是否以字母和数字组成，是返回true否则False
print('isalpha:','abccdedef1'.isalpha())      #检查字符串是否以纯字母组成，是返回true,否则false
# str.isdecimal()         检查字符串是否以纯十进制数字组成，返回布尔值
# str.isdigit()               检查字符串是否以纯数字组成，返回布尔值
# str.islower()               检查字符串是否全是小写，返回布尔值
# str.isupper()           检查字符串是否全是大写，返回布尔值
# 
# str.isnumeric()       检查字符串是否只包含数字字符，返回布尔值
# str.isspace()            如果str中只包含空格，则返回true,否则FALSE  
print('title:','abc cde def1 '.title())           #返回标题化的字符串（所有单词首字母大写，其余小写）
# str.istitle()               如果字符串是标题化的(参见title())则返回true,否则false
# str.join(seq)               以str作为连接符，将一个序列中的元素连接成字符串
print('title:','abc cde def1 '.split(' ',1))       #以str作为分隔符，将一个字符串分隔成一个序列，仅分隔 num+1 个子字符串
# str.splitlines(keep)         以行分隔，返回各行内容作为元素的列表,默认为 False，不包含换行符，如果为 True，则保留换行符。
# str.lower()                 将大写转为小写
# str.upper()                 转换字符串的小写为大写
# str.swapcase()              翻换字符串的大小写
# str.lstrip()                去掉字符左边的空格和回车换行符
# str.rstrip()                去掉字符右边的空格和回车换行符
# str.strip()                 去掉字符两边的空格和回车换行符
# str.partition(substr)       从substr出现的第一个位置起，将str分割成一个3元组。
# str.replace(str1,str2,num)  查找str1替换成str2，num是替换次数
# str.rfind(str[,beg,end])    从右边开始查询子字符串
# str.rindex(str,[beg,end])   从右边开始查找子字符串位置
# str.rpartition(str)         类似partition函数，不过从右边开始查找
# str.translate(str,del='')   按str给出的表转换string的字符，del是要过虑的字符

# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 转换为大写，并删除字母o和b
print(b'runoob'.translate(bytes_tabtrans, b'ob'))
