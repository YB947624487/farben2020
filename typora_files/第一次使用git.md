## 从0开始关联git仓库

1.选择一个目录,git clone  https://github.com/YB947624487/xxx.git 就可以正常使用了



git remote add origin https://xxx.com/xxx.git

git push -u origin master # 我们把本地的master内容推送到远程新的master分支,还会把本地的master分支和远程分支关联起来



## 先有本地库,后有远程库

关联一个远程库,使用命令 git remote add origin git@server_name:user_name/path.git

关联后,使用git push -u origin master第一次推送master分支的所有内容;

此后,每次本地提交后,只要有必要,就可以使用git push origin master推送最新修改



## 从远程库克隆(先有远程库)

git clone git@github.com:xxx/gitskills.git





