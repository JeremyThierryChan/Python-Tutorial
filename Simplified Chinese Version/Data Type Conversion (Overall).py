'''
变量命名说明：
xxx_n：代表第n个xxx型数据
xxx2yyy_n：代表第n个由xxx类型数据转换为yyy类型数据，2的英文two谐音to，是程序设计中常用的谐音命名法
'''
integer_1 = 10
integer_2 = -5

float_1 = 3.1415
float_2 = 9e3
float_3 = -0.76

string_1 = '178'
string_2 = '2.71828'
string_3 = 'Python'
string_4 = '3e4'
string_5 = '5+8j'

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

dictionary_1 = {'a':3, 'b':4}
dictionary_2 = {'a':'abc', 'b':'Python', 'c':'Tutorial'}
dictionary_3 = {integer_1:'hahdfha', float_1:'17827'}

bool_1 = True
bool_2 = False
bool_3 = 1
bool_4 = 0

# int()，将其它类型的数据转换为整型
# float()，将其它类型的数据转换为浮点型
# str()，将其它类型的数据转换为字符串型
# complex()，，将其它类型的数据转换为复数型
# tuple()，将其它类型的数据转换为元组型
# list()，将其它类型的数据转换为列表型
# set()，将其它类型的数据转换为集合型
# dictionary()，将其它类型的数据转换为字典型
# bool()，将其他类型的数据转换为布尔型


'''使用int()函数将其他类型数据转换为整型'''
float2integer_1 = int(float_1)
float2integer_2 = int(float_2)
float2integer_3 = int(float_3)
string2integer_1 = int(string_1)
# string_2, string_3, string_4不可转换为整型
# 复数型数据不可转换为整型
# 元组型数据不可转换为整型
# 列表型数据不可转换为整型
# 集合型数据不可转换为整型
# 字典型数据不可转换为整型
bool2integer_1 = int(bool_1)
bool2integer_2 = int(bool_2)
bool2integer_3 = int(bool_3)
bool2integer_4 = int(bool_4)

'''使用float()函数将其他类型数据转换为浮点型'''
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
bool2float_1 = float(bool_1)
bool2float_2 = float(bool_2)
bool2float_3 = float(bool_3)
bool2float_4 = float(bool_4)

'''使用string()函数将其他类型数据转换为字符串型'''
integer2string_1 = str(integer_1)
integer2string_2 = str(integer_2)

float2string_1 = str(float_1)
float2string_2 = str(float_2)
float2string_ = str(float_3)

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

dictionary2string_1 = str(dictionary_1)
dictionary2string_2 = str(dictionary_2)
dictionary2string_3 = str(dictionary_3)

'''使用complex()函数将其他类型数据转换为复数型'''
integer2complex_1 = complex(integer_1, integer_2)
integer2complex_2 = complex(integer_1)
integer2complex_3 = complex(0, integer_1)
float2complex_1 = complex(float_1, float_2)
float2complex_2 = complex(float_1)
float2complex_3 = complex(0, float_1)
string2complex_1 = complex(string_5)
# 元组型数据不可转换为复数型数据
# 列表型数据不可转换为复数型数据
# 集合型数据不可转换为复数型数据
# 字典型数据不可转换为复数型数据
bool2complex_1 = complex(bool_1, bool_2)
bool2complex_1 = complex(bool_1, bool_3)

'''使用tuple()函数将其他类型数据转换为元组型'''
integer2tuple_1 = (integer_1, integer_2)
float2tuple_1 = (float_1, float_2, float_3)
string2tuple_1 = (string_1, string_2, string_3, string_4, string_5)
complex2tuple_1 = (complex_1, complex_2, complex_3)
list2tuple_1 = tuple(list_1)
list2tuple_2 = tuple(list_2)
list2tuple_3 = tuple(list_3)
set2tuple_1 = tuple(set_1)
set2tuple_2 = tuple(set_2)
set2tuple_3 = tuple(set_3)
dictionary2tuple_1 = tuple(dictionary_1)
dictionary2tuple_2 = tuple(dictionary_2)
dictionary2tuple_3 = tuple(dictionary_3)
bool2tuple_1 = (bool_1, bool_2, bool_3)

'''使用list()函数将其他类型数据转换为列表型'''
integer2list_1 = [integer_1, integer_2]
float2list_1 = [float_1, float_2, float_3]
string2list_1 = [string_1, string_2, string_3, string_4, string_5]
complex2list_1 = [complex_1, complex_2, complex_3]
tuple2list_1 = list(tuple_1)
tuple2list_2 = list(tuple_2)
tuple2list_3 = list(tuple_3)
set2list_1 = list(set_1)
set2list_2 = list(set_2)
set2list_3 = list(set_3)
dictionary2list_1 = list(dictionary_1)
dictionary2list_2 = list(dictionary_2)
dictionary2list_3 = list(dictionary_3)
bool2list_1 = [bool_1, bool_2, bool_3]

'''使用set()函数将其他类型数据转换为集合型'''
integer2set_1 = {integer_1, integer_2}
float2set_1 = {float_1, float_2, float_3}
string2set_1 = {string_1, string_2, string_3, string_4, string_5}
complex2set_1 = {complex_1, complex_2, complex_3}
tuple2set_1 = set(tuple_1)
tuple2set_2 = set(tuple_2)
tuple2set_3 = set(tuple_3)
list2set_1 = set(list_1)
list2set_2 = set(list_2)
list2set_3 = set(list_3)
dictionary2set_1 = set(dictionary_1)
dictionary2set_2 = set(dictionary_2)
dictionary2set_3 = set(dictionary_3)
bool2set_1 = {bool_1, bool_2, bool_3}

'''将其他类型数据转换为字典型'''
# 字典型数据不可直接转换，详见专属介绍  

'''使用bool()函数将其他类型数据转换为布尔型'''
integer_a = 1
integer_b = 0
float_a = 1.0
float_2 = 0.0
string_a = 'True'
string_b = 'False'
string_c = '1'
string_d = '0'

integer2bool_1 = bool(integer_a)
integer2bool_2 = bool(integer_b)
float2bool_1 = bool(float_1)
float2bool_2 = bool(float_2)
string2bool_1 = bool(string_1)
string2bool_2 = bool(string_2)
string2bool_3 = bool(string_3)
string2bool_4 = bool(string_4)
