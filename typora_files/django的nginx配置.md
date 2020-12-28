## 一行命令杀掉nginx进程

ps -ef | grep nginx | grep -v grep | awk '{print $2}' | xargs kill -9

grep -v 排除不带grep的信息