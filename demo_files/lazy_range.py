def lazy_range(up_to):
    '''一个从0到变量up_to,不包括up_to的生成器'''
    i = 0
    while i < up_to:
        yield i
        i += 1

for i in lazy_range(10):
    print(i)