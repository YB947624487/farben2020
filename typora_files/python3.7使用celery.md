## python3.7使用celery,修改文件

将async这个关键字修改为asynchronous

 /kombu/async 　

/celery/utils/timer2.py 　

/concurrency/asynpool.py 　

/kombu/transport/redis.py /celery/worker/auto_scale.py,components.py,consumer.py,strategy.py

批量替换命令

sed -i "s/oldString/newString/g" `grep oldString -rl /path`

例子: 

sed -i "s/大小多少/日月水火/g" `grep 大小多少 -rl /usr/aa` 

sed -i "s/大小多少/日月水火/g" `grep 大小多少 -rl ./`

mv /usr/local/python3/lib/python3.7/site-packages/kombu/async /usr/local/python3/lib/python3.7/site-packages/kombu/asynchronous

sed -i "s/async/asynchronous/g" `grep "async" -rl /usr/local/python3/lib/python3.7/site-packages/kombu/transport/redis.py `

sed -i "s/async/asynchronous/g" `grep "async" -rl /usr/local/python3/lib/python3.7/site-packages/celery/concurrency/asynpool.py`

sed -i "s/async/asynchronous/g" `grep "async" -rl /usr/local/python3/lib/python3.7/site-packages/celery/worker/components.py`

sed -i "s/async/asynchronous/g" `grep "async" -rl /usr/local/python3/lib/python3.7/site-packages/celery/worker/autoscale.py`

sed -i "s/async/asynchronous/g" `grep "async" -rl /usr/local/python3/lib/python3.7/site-packages/celery/worker/consumer.py`

sed -i "s/async/asynchronous/g" `grep "async" -rl /usr/local/python3/lib/python3.7/site-packages/celery/worker/strategy.py`