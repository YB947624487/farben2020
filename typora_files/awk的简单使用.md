## awk的简单使用

awk是一种处理文本文件的语言,是一个强大的文本分析工具,之所以叫awk,是因为其取了3位创始人的首字符.

awk/sed/grep更适合的方向,

1. grep更适合单纯的查找或匹配文本;
2. sed更适合编辑到匹配的文本;
3. awk 更适合格式化文本,对文本进行较复杂格式处理.

awk工作原理

awk工作流程可分为3个部分:

	1. 读输入文件之前执行的代码段(由BEGIN关键字标识);
 	2. 主循环执行输入文件的代码段;
 	3. 读输入文件之后的代码段(由END关键字标识).

命令结构:

awk 'BEGIN{ commands } pattern{ commands } END{ commands }'

查找第4列的内容:

cat test.txt | awk '{print $4}'

