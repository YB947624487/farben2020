## sed命令

sed: Stream Editor文本流编辑器,sed是一个"非交互式的"面向字符流的编辑器.能同时处理多个文件多行的内容,可以不对原文件改动,把整个文件输入到屏幕,可以把只匹配到模式的内容输入到屏幕,还可以只对原文件改动,但不会在屏幕上返回结果.

sed 命令格式: sed [option] 'sed command' filename

sed 脚本格式: sed [option] -f 'sed script' filename

option:

-n : 只打印模式匹配的行;

-e : 直接在命令行模式上进行sed动作编辑,此为默认选项;

-f : 将sed的动作写在一个文件内,用 -f filename执行脚本内的sed动作

-i : 直接修改文件内容;

-r : 支持拓展表达式.

sed 在文件中查询文本的方式:

1) 使用行号,可以是一个简单数字,或是一个行号范围:

x - x为行号;

x,y - 表示从x行到y行;

/pattern - 查询包含模式的行;

/pattern/pattern - 查询包含两个模式的行;

pattern/,x 在给定行号上查询包含模式的行;

x,/pattern/ 通过行号和模式查询匹配的行;

x,y! 查询不包含指定行号x和y的行

常用操作:

删除某行,把剩余内容输出到终端,可重定向到新文件,原文件不变:

​	sed '1d' /etc/demo.txt

​	sed '$d' /etc/demo.txt > new.txt

​	sed '1,2d' /etc/demo.txt

​	sed '3,$d' /etc/demo.txt

显示某行(可重定向):

​	sed -n '1p' demo.txt

​	sed -n '1,3p' demo.txt > new.txt

使用模式进行查询:

​	sed -n '/woshi/p' demo.txt

​	sed -n '/\\$/p' demo.txt 查询带$符号的行

增加/代替一行或多行字符串:

​	sed '1a test    test 1344' demo.txt 在第一行之后加入一行

​	sed '1,4a test 123' demo.txt  分别在1,2,3,4行之后加入一行

​	sed '1c test123' demo.txt  代替第一行

​	sed '1,3c test123' demo.txt 将1,2,3行的内容变成1行test123

sed -i直接操作文本

删除所有匹配行

​	sed -i '/test123/d' demo.txt

替换所有的

​	sed -i 's/test123/test2345/g' demo.txt 

​	

​	