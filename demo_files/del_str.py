'''
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
'''
from collections import Counter

while True:
    try:
        s_list = input().strip().split()
        for i in s_list:
            d1 = Counter(i)
            sort_d1 = sorted(d1.items(), key=lambda x: x[1])
            min_v = sort_d1[0][1]
            exclude_list = [i[0] for i in sort_d1 if i[1] == min_v]
            for j in exclude_list:
                i = i.replace(j, "")
            print(i)
    except:
        break
