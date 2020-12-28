## centos7 下使用virtualenv

1. 安装virtualenv包

   - pip3 install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com virtualenv

   - pip3 install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com virtualenvwrapper

     在/root/.bashrc后面加入4行

   - ```
     #设置virtualenv的统一管理目录，以后自动下载的虚拟环境都放在这
     WORKON_HOME=~/Envs   
     
     #添加virtualenvwrapper的参数，生成干净隔绝的环境
     VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages' 
     
     #指定python解释器的本体
     VIRTUALENVWRAPPER_PYTHON=/opt/python3/bin/python3
     
     #执行virtualenvwrapper安装脚本
     source /opt/python3/bin/virtualenvwrapper.sh
     ```

2. 创建virtualenv

   ```
   virtualenv --no-site-packages --python=python3 env_1
   ```

   --no-site-packages：表示使用一个只有Python3的环境，而不导入原来Python3中安装模块。

   --python=python3：指定要被虚拟的解释器环境。

   env_1：表示虚拟的Python环境目录。

3. 使用

   - 物理机下:

     创建并激活虚拟环境

     mkvirtualenv

     切换虚拟环境

     workon

     退出虚拟环境

     deactivate

     删除虚拟环境

     rmvirtualenv

     查看所有的虚拟环境

     lsvirtualenv

4. .bash_profile’只在会话开始时被读取一次，而’.bashrc’则每次打开新的终端时，都要被读取

