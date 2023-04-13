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

