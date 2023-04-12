'''
变量命名说明：
xxx_n：代表第n个xxx型数据
xxx2yyy_n：代表第n个由xxx类型数据转换为yyy类型数据，2的英文two谐音to，是程序设计中常用的谐音命名法
'''
integer_1 = 10
integer_2 = 5

float_1 = 3.1415
float_2 = 9e3

string_1 = '178'
string_2 = '2.71828'
string_3 = 'Python'
string_4 = '3e4'

complex_1 = 1+2j
complex_2 = -1-10j
complex_3 = -3j

tuple_1 = (1, 2, 3)
tuple_2 = ('Python', 'C++', 'Java')
tuple_3 = (1, float_1, tuple_1)

list_1 = [1, 2, 3]
list_2 = ['Python', 'C++', 'Java']
list_3 = [99, 7.349, list_1, tuple_2]

set_1 = {1, 6, 2, 9, 7, 0, -17}
set_2 = {9.34, 0.5, 7.38, 5.329, -18.7654}
set_3 = {'Python', 'A', 'B', 'C', 'a', 'b', 'Pyramid', '!', 'Ω', 'ß'}

dictionary_1 = {'a':3, 'b':[18, 6.6, 'Desk']}


# int()，将其它类型的数据转换为整型
# float()，将其它类型的数据转换为浮点型
# str()，将其它类型的数据转换为字符串型
# complex()，，将其它类型的数据转换为复数型
# tuple()，将其它类型的数据转换为元组型
# list()，将其它类型的数据转换为列表型
# set()，将其它类型的数据转换为集合型
# dictionary()，将其它类型的数据转换为字典型


'''将其他类型数据转换为整型'''
float2integer_1 = int(float_1)  # 浮点型转换为整型
float2integer_2 = int(float_2)
string2integer_1 = int(string_1)  # 浮点型转换为整型
# string_2不可转换为整型
# 复数型数据不可转换为整型
# 元组型数据不可转换为整型
# 列表型数据不可转换为整型
# 集合型数据不可转换为整型
# 字典型数据不可转换为整型

'''将其他类型数据转换为浮点型'''
integer2float = float(integer_1)

string2float_1 = float(string_1)
string2float_2 = float(string_2)
# string3 不可转换为浮点型
string2float_3 = float(string_4)

# 复数型数据不可转换为浮点型
# 元组型数据不可转换为浮点型
# 列表型数据不可转换为浮点型
# 集合型数据不可转换为浮点型
# 字典型数据不可转换为浮点型

'''将其他类型数据转换为字符串型'''
integer2string_1 = str(integer_1)
integer2string_2 = str(integer_2)

float2string_1 = str(float_1)
float2string_2 = str(float_2)

complex2string_1 = str(complex_1)
complex2string_2 = str(complex_2)
complex2string_3 = str(complex_3)

tuple2string_1 = str(tuple_1)
tuple2string_2 = str(tuple_2)
tuple2string_3 = str(tuple_3)

list2string_1 = str(list_1)
list2string_2 = str(list_2)
list2string_3 = str(list_3)

set2string_1 = str(set_1)
set2string_2 = str(set_2)
set2string_3 = str(set_3)
'''将其他类型数据转换为复数型'''

'''将其他类型数据转换为元组型'''

'''将其他类型数据转换为列表型'''

'''将其他类型数据转换为集合型'''

'''将其他类型数据转换为字典型'''

'''
float <- integer, float()
integer <- float, int()
'''
float_a = float(integer_1)  # 将利用float()函数将integer_1转换为浮点型数据并赋值给变量float_a
integer_a = int(float_1)
# Printing to console



'''
integer <- string
string <- integer
'''
integer_b = int(string_1)
string_a = str(integer_1)

'''
float <- string
string <- float
'''
float_b = float(string_2)
string_b = str(float_1)

'''


'''


'''
integer, float, string -> complex
'''
complex_a = complex(integer_1, integer_2)



'''
tuple <-> list
'''

'''
tuple <-> set
'''

'''
tuple <-> dictionary
'''

'''
list <-> set
'''

'''
list <-> dictionary
'''

'''
set <-> dictionary
'''
