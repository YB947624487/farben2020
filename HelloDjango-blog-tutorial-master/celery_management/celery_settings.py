import celery
import djcelery

#当djcelery.setup_loader()运行时，Celery便会去查看INSTALLD_APPS下包含的所有app目录中的tasks.py文件，找到标记为task的方法，将它们注册为celery task。
djcelery.setup_loader()

#设置不同的队列，不要只使用默认的队列，这样当任务比较多的时候任务之间会相互影响（例如将普通任务和定时任务混在一起），
CELERY_QUEUES={
    #定时任务队列
    'beat_tasks':{
        'exchange':'beat_tasks',
        'exchange_type':'direct',
        'binding_key':'beat_tasks'
        },
    'work_queue':{
        'exchange':'work_queue',
        'exchange_type':'direct',
        'binding_key':'work_queue'
        }
    #普通任务队列
    }

# 设置默认队列,若不指定队列则使用该队列
CELERY_DEFAULT_QUEUE='work_queue'

#参数配置可参考官网：http://docs.celeryproject.org/en/latest/userguide/configuration.html
CELERY_ACKS_LATE=True #允许重试
CELERYD_FORCE_EXECV=True #可以让Celery更加可靠,只有当worker执行完任务后,才会告诉MQ,消息被消费，防治死锁
CELERYD_CONCURRENCY=4 #设置并发的worker数量
CELERYD_MAX_TASKS_PRE_CHILD=100 #每个worker最多执行100个任务被销毁，可以防止内存泄露
CELERYD_TASK_TIME_LIMIT=60*6 #单个任务的最大运行时间为6分钟，超过的话就被杀掉

# 禁用pickle序列化
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
