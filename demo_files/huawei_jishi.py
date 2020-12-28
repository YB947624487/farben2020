'''
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，
他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
对于其中重复的数字，只保留一个，把其余相同的数去掉，
不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，
按照排好的顺序去找同学做调查。
请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。
注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。
当没有新的输入时，说明输入结束。
'''

while True:
    try:
        num = int(input())
        s = set()
        for i in range(num):
            n = input()
            s.add(int(n))
        for i in sorted(s):
            print(i)
    except:
        break

"""
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
"""


def print_eight_str(s):
    while len(s) > 8:
        print(s[:8])
        s = s[8:]
    else:
        # print(f"{s}{'0'*(8-len(s))}")
        print(s + '0' * (8 - len(s)))


while True:
    try:
        s = input()
        print_eight_str(s)
    except:
        break

"""
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示
"""
while True:
    try:
        s = input()
        print(int(s, 16))
    except:
        break

'''
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格
'''


def decompose_factor(num):
    is_prime = 1
    # 如果一个数是合数,那么它的最小质因数肯定小于等于他的平方根
    for i in range(2, int(num ** 0.5 + 2)):
        if num % i == 0:
            num = int(num / i)
            print(str(i), end=' ')
            return decompose_factor(num)
    if is_prime == 1:
        print(str(num), end=' ')


while True:
    try:
        num = int(input())
        decompose_factor(num)
    except:
        break

"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
"""
while True:
    try:
        s = float(input())
        i = int(s)
        f = s - i
        i = i + 1 if f * 10 >= 5 else i
        print(i)
    except:
        break

'''
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
'''
while True:
    try:
        n = int(input())
        d = {}
        for i in range(n):
            index, value = input().split()
            index = int(index)
            value = int(value)
            d_v = d.get(index)
            d[int(index)] = d_v + value if d_v else value
        sort_d = sorted(d.items(), key=lambda d: d[0])
        for i in sort_d:
            print(i[0], i[1])
    except:
        break

'''
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
'''
while True:
    try:
        s = input()
        temp_list = []
        for i in s[::-1]:
            if i not in temp_list:
                temp_list.append(i)
        print(int("".join(temp_list)))

    except:
        break

'''
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，
不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串abaca而言，有a、b、c三种不同的字符，因此输出3。
'''
while True:
    try:
        s = input()
        count = 0
        temp_list = []
        for i in s:
            if i not in temp_list:
                temp_list.append(i)
            else:
                continue
            if ord(i) in range(128):
                count += 1
        print(count)
    except:
        break

'''
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
'''
while True:
    try:
        s = input()
        print(s[::-1])
    except:
        break

'''
给定n个字符串，请对n个字符串按照字典序排列。
'''
while True:
    try:
        n = int(input())
        temp_list = []
        for i in range(n):
            s = input()
            temp_list.append(s)
        sort_list = sorted(temp_list,key=str)
        print('\n'.join(sort_list))
    except:
        break

'''
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
'''
while True:
    try:
        i = int(input())
        print(bin(i).count("1"))
    except:
        break

'''
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，
从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：

起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)

结果 （10， -10）
'''
import re
while True:
    try:
        s_list = input().split(";")
        temp_dict = {}
        parms = r'[WASD]{1}\d{1,2}'
        for i in s_list:
            match = re.match(parms, i)
            if match and match.group() == i:
                if i[0] not in temp_dict:
                    temp_dict[i[0]] = int(i[1:])
                else:
                    temp_dict[i[0]] += int(i[1:])
        h = temp_dict.get('D',0) - temp_dict.get('A',0)
        v = temp_dict.get('W',0) - temp_dict.get('S',0)
        print(f"{h},{v}")
    except:
        break

'''
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

处理：
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，
但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是”相同“的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准
'''
error_dict = {}
while True:
    try:
        s = input()
        t_path = s.split()[0]
        t_no = s.split()[1]
        t_name = t_path.split('\\')[-1][-16:]

        k = f"{t_name} {t_no}"
        if k in error_dict:
            error_dict[k] += 1
        else:
            error_dict[k] = 1
    except:
        break

if len(error_dict) > 8:
    delete_list = list(error_dict.keys())[:-8]
    for i in delete_list:
        del error_dict[i]
for k, v in error_dict.items():
    print(f"{k} {v}")