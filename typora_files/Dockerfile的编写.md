## Dockerfile的编写

Dockerfile的主要用途:

	1. 对当前应用的描述;
 	2. 指导Docker完成应用的容器化(创建一个包含当前应用的镜像).

example:

FROM alpine

LABEL maintainer="xxx@abc.com"

RUN apk add --update nodejs nodejs-npm

COPY . /src

WORKDIR /src

RUN npm install

EXPOSE 8080

ENTRYPOINT ["node","./app.js"]

1. 以alpine镜像作为基础,指定维护者为"xxx@abc.com";
2. 安装node.js和npm;
3. 将当前目录的文件复制到镜像的/src文件中(可以加入.dockerignore文件)
4. 设置新的工作目录,安装依赖包;
5. 记录应用的网络端口,最后将app.js设置为默认运行的应用.

每一行命令都是一个镜像层 --> from/run/copy/run

WORKDIR/EXPOSE这些指定的设置命令不会产生新的镜像层

docker image build -t node_demo:latest .  创建镜像

docker container run -d --name nodejs_demo -p 80:8080 nodejs_demo

-d的作用是让应用程序以守护线程的方式在后台运行.

每一个run指令会新增一个镜像层,因此,通过使用&&连接命令以及使用反斜杠换行的方法,将多个命令包含在一个run指令中,通常这是一种值得提倡的方式.

ADD和COPY命令都是把本地文件copy到指定目录,add命令可以直接解压缩,还可以下载(但是不推荐这么做,他会构建更多的镜像层,使包变大)



