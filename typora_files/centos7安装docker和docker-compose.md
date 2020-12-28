## centos 7 安装docker和docker-compose

1. 安装docker

   yum -y install docker

   启动: systemctl start docker.service

   设置开机启动: systemctl enable docker.service

2. 安装docker-compose

   sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

   sudo chmod +x /usr/local/bin/docker-compose

   ```
   ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
   ```

   docker-compose --version