## docker 常用命令

docker image ls  =  docker images

docker image ls --format "{{.Repository}}: {{.Tag}}: {{.Size}}" 可以按照格式查看仓库,标签,大小

docker search alpine --filter "is-automated=true" | wc -l 查看自动创建的alpine镜像,并返回查询结果行数

docker image ls --digests alpine 查看摘要id(散列值)

docker images -q  获取docker镜像的散列值

docker image rm $(docker image ls -q) -f 删除本地系统的全部镜像

docker image pull alpine:latest  -- 拉取最新的镜像

docker image inspect 742e    查看742e容器的细节

docker image rm alpine:latest 命令的含义是删除 alpine:latest 镜像。当镜像存在关联的容器，并且容器处于运行（Up）或者停止（Exited）状态时，不允许删除该镜像

docker container run -it ubuntu /bin/bash 会启动某个 Ubuntu Linux 容器，并运行 Bash Shell 作为其应用

docker contain run --name xxx -d mysql:5.7 -v local_path:virtual_path -e env 启动一个容器

docker container stop xxx/container_id 停止一个容器

docker container ls 列出全部处于运行中的容器, -a全部的容器

docker container start xxx/container_id 重启一个停止的容器,container可以省略

docker logs container_id/name 查看容器运行的log

docker cp 96f7:/www /tmp    将容器/www目录拷贝到主机的/tmp目录

docker cp /www/temp 96f7:/www 将主机/www/temp目录的文件拷贝到容器/www目录

docker container exec -it name/container_id /bin/bash 重新进入正在运行的容器shell环境

docker container stop xxx   --> docker container rm xxx 或者 docker container rm xxx -f

docker container run --name xxx -it --restart always /bin/bash优雅地进入shell,退出后让他自己重启,不推荐

强制删除所有的容器 docker container rm $(docker container ls -aq) -f

docker的容器化步骤: 

	1. 编写应用代码;
 	2. 创建一个Dockerfile,其中包括当前应用的描述/依赖以及该如何运行这个应用;
 	3. 对该Dockerfile执行 docker image build命令;
 	4. 等待Docker将应用程序构建到Docker镜像中.

一旦应用容器化完成(即应用被打包为一个Docker镜像),就能以镜像的形式交付并以容器的方式运行了.