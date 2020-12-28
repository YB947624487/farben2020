python的7大原则,24种设计模式

七大原则:

1. 单一职责原则 - 一个类负责一项职责;
2. 里氏替换原则 - 继承与派生的规则,子类可以替换重写父类方法;
3. 依赖倒转原则 - 高层模块不要依赖底层模块;
4. 接口隔离原则 - 尽量细化接口,接口中的方法尽量少;
5. 迪米特法则 - 高内聚,低耦合;
6. 开闭原则 - 一个软件实体如类/模块/函数应该对外拓展开放,对修改关闭;
7. 组合/聚合复用原则,尽量多用组合来实现,少用继承

24种设计模式:

	1. 创建型模式 - 单例模式/工厂模式
 	2. 结构型模式 - 
 	3. 行为型模式



## 单例模式

1. python的模块就是天然的单例模式

   class Singleton(object):

   ​	def foo(self):

   ​		pass

   singleton = Singleton()

   使用: from xxx import singleton



 2. 使用装饰器

    def Singleton(cls):

    ​	_instance = {}

    ​	def _singleton(*args,**kwargs):

    ​		if cls not in _instance:

    ​			_instance[cls] = cls(*args,**kwargs)

    ​		return _instance[cls]

    ​	return _singleton

    \# 使用

    @Singleton

    class A(object):

    ​	a = 1

    ​	def \__init__(self,x=0):

    ​		self.x = x

    a1 = A(2)

    a2 = A(3)

	3.  使用类

    class Singleton(object):

    ​	def \__init__(self):

    ​		pass

    ​	@classmethod

    ​	def instance(cls,*args,**kwargs):

    ​		if not hasattr(Singleton,"_instance"):

    ​			Singleton._instance = Singleton(*args,**kwargs)

    ​		return Singleton._instance

	4.  使用\__new__方法(推荐)

    import threading

    class Singleton(object):

    ​	_instance_lock = threading.Lock()

    ​	def \__init__(self):

    ​		pass

    ​	def \__new__(cls,*args,**kwargs):

    ​		if not hasattr(Singleton,"_instance"):

    ​			with Singleton._instance_lock:

    ​				if not hasattr(Singleton,"_instance"):

    ​					Singleton._instance = object.\_\_new__(cls)

    ​		return Singleton._instance

    obj1 = Singleton()

    obj2 = Singleton()

    print(obj1, obj2)

    def task(arg):

    ​	obj = Singleton()

    ​	print(obj)

    for i in range(10):

    ​	t = threading.Thread(target=task,args=[i,])

    ​	t.start()

