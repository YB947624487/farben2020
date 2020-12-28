## docker 问题汇总

1. 运行容器提示权限问题:

   python: can't open file 'manage.py': [Errno 13] Permission denied

   这时候需要关闭selinux;  -- setenforce 0

