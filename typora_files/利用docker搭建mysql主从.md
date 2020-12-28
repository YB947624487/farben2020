## docker搭建mysql主从

1. 首先拉取mysql的docker镜像，然后使用此镜像启动主从2个容器：

   docker pull mysql：5.7

   主： docker run -p 3316:3306 -v ~/temp/mysql01:/temp --name mysql01 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7

   从：docker run -p 3326:3306 -v ~/temp/mysql02:/temp --name mysql02 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7

2. 配置master（主）

   docker exec -it mysql01 /bin/bash

   vim /etc/mysql/my.cnf

   此时vim命令找不到，安装vim

   apt-get update

   apt-get install vim

   1. 在my.cnf中添加如下配置：

      echo 'xxx' >> my.cnf

   [mysqld]

   \## 同一局域网内注意要唯一

   server-id=100

   \## 开启二进制日志功能,可以随意取(关键)

   log-bin=mysql-bin

   #replicate-do-db=configerdata    #指定同步的数据库（若需将所有数据库同步，则不需加此配置项）
   #replicate-do-db=userdata     #指定同步的数据库
   #replicate-ignore-db=mysql    此配置为指定不同步的数据库

   2. 配置完成后,需重启mysql服务才会使配置生效,重启mysql会使容器停止,我们还要重启容器

   service mysql restart

   docker start mysql01

    3. master数据库创建数据同步用户,授予用户 slave REPLICATION SLAVE权限和REPLICATION CLIENT权限，用于在主从库之间同步数据

       mysql -uroot -p123456

       CREATE USER 'slave'@'%' IDENTIFIED BY '123456';

       GRANT REPLICATION SLAVE,REPLICATION CLIENT ON \*.* TO 'slave'@'%';

       进入容器,show master status; 可以看到mysql-bin.000001文件,说明开启日志复制成功

       记住position的值 154 后面slave要用

   3. 配置slave

      \## 设置server_id,注意要唯一 server-id=101   ## 开启二进制日志功能，以备Slave作为其它Slave的Master时使用 log-bin=mysql-slave-bin    ## relay_log配置中继日志 relay_log=edu-mysql-relay-bin 

      重启 service mysql restart

      docker start mysql02

   4. 链接master和slave

      获取容器ip:

      docker inspect --format='{{.NetworkSettings.IPAddress}}' mysql01

      172.18.0.3

      连接: mysql -h172.18.0.3 -uslave -p123456

      change master to master_host='172.18.0.3', master_user='slave', master_password='123456', master_port=3306, master_log_file='mysql-bin.000001', master_log_pos=154, master_connect_retry=30;

      **master_port**：Master的端口号，指的是容器的端口号

      **master_user**：用于数据同步的用户

      **master_password**：用于同步的用户的密码

      **master_log_file**：指定 Slave 从哪个日志文件开始复制数据，即上文中提到的 File 字段的值

      **master_log_pos**：从哪个 Position 开始读，即上文中提到的 Position 字段的值

      **master_connect_retry**：如果连接失败，重试的时间间隔，单位是秒，默认是60秒

      在Slave 中的mysql终端执行`show slave status \G;`用于查看主从同步状态。

   使用start slave打开主从复制 -- Slave_IO_Running会变成Yes

   