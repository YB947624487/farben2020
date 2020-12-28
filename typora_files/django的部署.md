## django的部署

1. uwsgi

   uwsgi直接启动：

   uwsgi --http 0.0.0.0:8888 --file mysite/wsgi.py --static-map=/static=static

   --http: 启动项目的ip地址和端口

   --file： 指定项目中的wsgi文件

   --static-map： 指定静态资源存放的目录

   uwsgi --ini ./uwsgi.ini

2. gunicorn

   python -m pip install gunicorn

   gunicorn myproject.wsgi -b 0.0.0.0:8000

   gunicorn的常用配置：

   -c 指定一个配置文件；

   -b 与指定的socket进行绑定；

   -D 以守护进程形式来运行gunicorn进程，将服务放到后台去运行

   -w 工作的进程数量

   -k 工作的进程类型，sync（默认） eventlet，gevent，or tornado，gthread等