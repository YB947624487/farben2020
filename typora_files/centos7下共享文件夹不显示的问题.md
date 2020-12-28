## centos 7 下共享文件夹不显示的问题

我们vmware设置了共享文件夹,单/mnt/hgfs下没有文件,这个时候是挂在格式不对:

安装工具:

yum -y install open-vm-tools

vmhgfs-fuse .host:/ /mnt/hgfs 完成设置