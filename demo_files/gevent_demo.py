'''
gevent可以轻松通过gevent实现并发同步或异步编程,在gevent中用到的主要模式
是greenlet,它是以c扩展模块形式接入python的轻量级协程,greenlet全部运行在
主程序操作系统进程的内部,但它们被协作式调度
'''
# import gevent
# def eat(name):
#     print(f"{name} eat 1")
#     gevent.sleep(2)
#     print(f"{name} eat 2")
#
# def play(name):
#     print(f"{name} play 1")
#     gevent.sleep(1)
#     print(f"{name} play 2")
#
# g1 = gevent.spawn(eat,'egon')
# g2 = gevent.spawn(play,name='egon')
# g1.join()
# g2.join()
# # 或者使用gevent.joinall([g1,g2])
# print('主')
'''
上例gevent.sleep(2)模拟的是gevent可以识别的io阻塞,而time.sleep(2)或其他
的阻塞,gevent是不能直接识别的,需要用下面的一行代码打补丁后,才能识别,
from gevent import monkey;monkey.patch_all()必须放到被打补丁者的前面,
如time,socket模块之前;或者我们干脆记忆成：要用gevent，需要将
from gevent import monkey;monkey.patch_all()放到文件的开头
'''
from gevent import monkey;monkey.patch_all()
import gevent
import time
def eat():
    print('eat food 1')
    time.sleep(2.5)
    print('eat food 2')

def play():
    print('play 1')
    time.sleep(1)
    print('play 2')

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)
gevent.joinall([g1,g2])
print('主')