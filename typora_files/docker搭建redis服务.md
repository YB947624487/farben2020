## Docker案例：搭建Redis服务

使用官方的redis镜像搭建数据库服务，目前的latest版本对应5.0.8版。挂载本地数据目录、配置目录、日志目录，便于数据备份和迁移。

1. 创建挂在目录和文件

   在宿主机创建配置目录`~/docker/redis/conf`、数据目录`~/docker/redis/data`和日志目录`~/docker/redis/log`，并在配置目录中创建文件`~/docker/redis/conf/redis.conf`，配置文件内容如下 --- logfile /log/redis.log

   2. 拉取最新redis镜像 -- docker pull redis

   3. 创建容器并启动 -- 挂在本地的配置/数据/日志目录到容器内部.

      *# --name redis 容器名称为redis* *# -p 6379:6379 绑定本机6379端口到容器的6379端口（redis服务端口）* *# -v ~/docker/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf 挂载本地配置文件* *# -v ~/docker/redis/log/:/log/ 挂载本地日志目录* *# -v ~/docker/redis/data:/data 挂载数据文件* *# -d 后台运行* *# redis-server /usr/local/etc/redis/redis.conf --appendonly yes 使用自定义的配置文件，并启用磁盘数据持久化* 

      docker run --name redis -p 6379:6379 -v ~/docker/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf -v ~/docker/redis/log/:/log/ -v ~/docker/redis/data:/data -d  redis redis-server /usr/local/etc/redis/redis.conf --appendonly yes

   容器启动后可通过本地的`~/docker/redis/log/redis.log`，查看redis运行情况

2. 使用本地redis-cli客户端连接redis，并添加key值`v=1`，执行几次操作后，此时`~/docker/redis/data`目录下`appendonly.aof`文件已有相关数据内容。



如果此时停止redis容器，再启动一个新的redis容器挂载相同的目录，则新的容器中的redis已经包含上一个容器中的数据。



访问: docker exec -it  a136 redis-cli



docker run -p 6379:6379 --name redis01 -v ~/docker/redis/redis.conf:/etc/redis/redis.conf -v ~/docker/redis/data:/data -d redis redis-server /etc/redis/redis.conf --appendonly yes

