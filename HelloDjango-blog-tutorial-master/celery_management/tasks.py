import time
from celery.task import Task

class Demo(Task):
    # 任务名,其他地方要做调用的
    name='demo'
    def run(self,*args,**kwargs):
        print('start celery task')
        time.sleep(5)
        print('args={},kwargs={}'.format(args, kwargs))
        print('end celery task')