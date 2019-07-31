# C++复习
> 1.程序文件的后缀与所运行的具体编译器有关
> 2.const对象必须要初始化，且不能修改
> 3.定义符合类型，如引用、数组和指针。  
    引用为对象提供了另外一个名字。
	符合类型使用其他类型定义的类型。
> 4.C++是一种静态类型语言
> 5.整型（integral type)包括char(1B) wchar_t(2B)  short(0.5word/16bits)  int(word,32bits)  long(1~2words) bool(8bit)  
    其中short int  long 还分为signed和unsigned
> 6.  float(word)  double(2words) long double(3~4words)
> 7. 复制初始化   int ival=1000;  
     直接初始化   int ival(1000)  
	 初始化指创建变量并赋予初始值  
	 赋值则是擦除对象的当前值，并用新值代替
> 8.定义用于为变量分配存储空间，还可以为变量指定初始值。在一个程序中，变量有且仅有一个定义。  
    声明用于向程序声明变量的类型和名字。  
	定义也是一种声明
	当extern声明有初始化式也可以被当做是定义。  
	变量有三要素：存储空间、类型和名字。  
	e.g. extern double pi = 3.1314  
	同样分配并初始化了存储空间，只有当extern声明位于函数外部时，才可以有初始化式
> 9.非const对象  
