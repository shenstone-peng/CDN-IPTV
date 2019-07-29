# shell变量
赋值：
```
var_name="shenpeng"
```
使用变量
```
echo ${var_name}
```
> 只读变量：
 ```
   readonly variable_name
   ```
   
> 删除变量
```
unset variable_name
```
> 变量范围

local   局部变量
export 环境变量
全局变量

## shell变量单引号双引号
双引号：可以有变量，也可以出现转义字符


## shell字符串操作
```
string="abcd"
echo ${#string}    //获取字符串长度  4
echo ${string:1:3}  //提取子字符串 “bcd”
echo $(expr index "$string" c)  //查找子字符串 c
```

## shell数组
- bash只支持一维数组，并且没有限定数组的大小
- 下标可以是整数或算术表达式，且下标不需要连续
```
alist=(v0 v1 v2 v3)
alist[0]=v0
alist[n]=vn
${alist[2]} //v3
echo ${alist[@]}   //获取所有元素
length=${#alist[@]}   //获取数组长度
lengthn-${#alist[2]}   //获取alist[2]的长度
```
参数处理 |说明
---|:--:
 $#     | 传递到脚本的参数个数
 $*     | 以一个单字符串显示所有向脚本传递的参数
 $$     | 脚本运行的当前进程ID号
 $!     | 后台运行的最后一个进程的ID号
 $@     | 与$*相同，但是使用时加引号，并在引号中返回每个参数
 $-     | 显示Shell使用的当前选项，与set命令功能相同
 $?     | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误
 $n     | 第n个参数

 
 
运算符| 示例
---|:--:
\+     |  `expr $a + $b`  (( a + b ))
\-     |  `expr $a - $b`
\*     |  `expr $a \* $b`  ((a * b))
/     |  `expr $b / $a` 
%     |  `expr $b % $a` 
=     |  a=$b 
==    |  [ $a == $b ] 返回 false  [[  $a == $b ]]
!=    |  [ $a != $b ]
-eq   |  [ $a -eq $b ] [[ $a -eq $b ]]    (only number)
-ne   |  [ $a -ne $b ]                    (only number)
-gt   |  [ $a -gt $b ]                    (only number)
-lt   |  [ $a -lt $b ]                    (only number)
-ge   |  [ $a -ge $b ]                    (only number)
-le   |  [ $a -le $b ]                    (only number)
!     |  [ ! false ] 返回 true            
-o    |  |[ $a -lt 20 -o $b -gt 100 ] 返回 true
-a    |  [ $a -lt 20 -a $b -gt 100 ] 返回 false
&&    |  [[ $a -lt 100 && $b -gt 100 ]] 返回 false
||    |  [[ $a -lt 100 || $b -gt 100 ]] 返回 true
=     |  [ $a = $b ] 返回 false
!=    |  [ $a != $b ] 返回 true
-z    |  [ -z $a ] 返回 false
-n    |  [ -n $a ] 返回 true




-----------------------------------------------------
>1、在自己姓名缩写的用户主目录下, 用自己的用户创建一个shell，执行完成以下功能  
2、从/var/log/messages中过滤存在root字符的信息存放到当前目录下，取名为testfile  
3、打开testfile逐行检测，第6个列为(root)的，则输出到testfile1,否则忽略  
4、将testfile1中的” (root)” 替换成supperuser，保存为testfile2
-------------------------------------------------------------
```
grep root /var/log/messages > /home/shenpeng/shellStudy
```
