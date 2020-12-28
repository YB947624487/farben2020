'''
协程(coroutine),又称微线程,协程的作用:在执行A函数的时候,可以随时中断,
去执行B函数,然后中断继续执行A函数(可以自动切换),单这一过程并不是函数调用
(没有调用语句),过程很像多线程,然而协程只是一个线程在执行.
协程可以很完美的处理IO密集型问题
1. 执行效率高,因为子程序切换函数,而不是线程,没有线程切换的开销,由程序自身
控制切换,于多线程相比,线程数量越多,切换开销越大,协程的优势越明显;
2. 不需要锁的机制,只有一个线程,也不存在同时写变量冲突,在控制共享资源时也
不需要加锁
'''
# 并发的本质 -- 切换 + 保存状态
'''
yiled可以保存状态，yield的状态保存与操作系统的保存线程状态很像，
但是yield是代码级别控制的，更轻量级，而非操作系统级别的2 send可以把
一个函数的结果传给另外一个函数，以此实现单线程内程序之间的切换
'''
# greenlet
# from greenlet import greenlet
#
# def eat(name):
#     print('%s eat 1' %name)
#     g2.switch('egon')
#     print('%s eat 2' %name)
#     g2.switch()
# def play(name):
#     print('%s play 1' %name)
#     g1.switch()
#     print('%s play 2' %name)
#
# g1=greenlet(eat)
# g2=greenlet(play)
#
# #可以在第一次switch时传入参数，以后都不需要
# g1.switch('egon')

#顺序执行
import time
def f1():
    res=1
    for i in range(10000000):
        res+=i

def f2():
    res=1
    for i in range(10000000):
        res*=i

start=time.time()
f1()
f2()
stop=time.time()
print('run time is %s' %(stop-start)) #3.985628366470337

#切换
from greenlet import greenlet
import time
def f1():
    res=1
    for i in range(10000000):
        res+=i
        g2.switch()

def f2():
    res=1
    for i in range(10000000):
        res*=i
        g1.switch()

start=time.time()
g1=greenlet(f1)
g2=greenlet(f2)
g1.switch()
stop=time.time()
print('run time is %s' %(stop-start)) # 19.763017892837524

'''
greenlet只是提供了一种比generator更加便捷的切换方式,当切到一个任务执行
时如果遇到io,那就原地阻塞,仍然是没有解决遇到IO自动切换来提升效率的问题
'''