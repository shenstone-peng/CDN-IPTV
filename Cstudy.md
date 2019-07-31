# C++复习
> 1.程序文件的后缀与所运行的具体编译器有关

> 2.const对象必须要初始化，且不能修改

> 3.定义符合类型，如引用、数组和指针。  
    引用为对象提供了另外一个名字。
	符合类型使用其他类型定义的类型。
> 4.C++是一种静态类型语言

> 5.整型（integral type)包括  
    char(1B) wchar_t(2B)  
    short(0.5word/16bits)  int(word,32bits)  long(1~2words) 
    bool(8bit)  
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
	
> 9.  

      ```
    //file_1.cc  非const对象
	int counter;
	//file_2.cc
	extern int counter;
	++counter;
	
	//file_1.cc  const对象，当const对象未用extern声明时不可以在别的文件中使用
	extern const int bufsize=fun();
	//file_2.cc
	extern const int bufsize
	for(int index=0;index~=bufsize;++index)
	```

> 10. a reference must be initialized  
      initializer must be an object  
	  nonconst reference to a const object is wrong

> 11.非const引用只能绑定到与该引用同类型对象。const引用则可以绑定到不同但相关的类型的对象或绑定到右值。 **原因**：因为const只读

> 12.数据抽象和封装的好处。  
   - 避免内部出现无意的可能破坏对象状态的用户级错误
   - 随时间推移可以根据需求改变或bug报告来完善类实现，而无需改变用户级代码
   
> 14.**vector**：必须是已存在的元素才能用下标操作符进行索引，通过下标操作进行赋值时，不会添加任何元素。

> 15.合法指针定义或赋值  
  ```
  int ival=1024;
  int *pi=0;     //pi initialized to address no object
  int *pi2=&ival; // pi2 initialized to address of ival
  int *pi3;      //ok but dangerous,pi3 is uninitialized
  pi = pi2;     //pi and pi2 address the same object
  pi2=0;      //pi2 now address no object
  ```
> 16.C++定义了算数类型之间的内置转换以尽可能防止精度损失。  
     何时发生隐式类型转换
	 - 在混合类型的表达式中，其操作数被转换为相同的类型
	  ```
	 int ival;
	 double dval;
	 (ival>=dval) //ival converted to double
	 
	 - 用作条件的表达式被转换为bool类型：
	  ```
	 int ival;
	 if(ival);  //ival converted to bool
	 
	 - 用一表达式初始化某个变量，或将一表达式赋值给某个变量，则该表达式被转换成该变量的类型
	 ```
	 int ival=3.14  //3.14 converted to int
	 int *p;
	 p=0;   // the **int** 0 converted to a null pointer of type int.
	 
> 17.删除指针所指向的对象之后，将指针置为0，则比较容易发现读写已删除的对象。

> 18.应该将不修改相应实参的形参定义为const引用。如果将这样的形参定义为非const引用，则毫无必要的限制了该函数的使用。

> 19.在函数中，倾向于通过传递指向容器中需要处理的元素的迭代器来传递容器。

> 20.在函数中，千万不要返回局部对象的引用

> 21.内联函数避免函数调用的开销。 **原理** ：普通函数调用前要先将之前的位置保存寄存器，并在返回时恢复，需要复制实参，程序还必须转向一个新位置执行

> 22.每个版本的重载函数都应在同一个作用域中声明。


> 23.指向函数的指针以及指向函数指针的指针
int a; //a即是整型
int *p; //*p即是整型-->p即指向整型的指针
int (*p)(int);//(*p)(int)即是整型-->(*p)即是返回整型的函数-->p即是指向这个函数的指针
指向函数指针的指针的正确写法：
int (**p)(int);//(**p)(int)即是整型-->(**P)即是返回整型的函数-->(*p)即是指向这个函数的指针-->p即是指向函数指针的指针
指向函数指针的指针的错误写法即分析：
int *(*p)(int);//*(*p)(int)即是整型-->(*p)(int)即是指向这个整型的指针-->(*p)即是返回这个指针的函数-->p即是指向这个函数的指针
int **p(int);//**p(int)即是整型-->*p(int)即是指向这个整型的指针-->p(int)即是指向这个指针的指针-->p即是返回指针的指针的函数
int (*ff(int)(int*,int);//(*ff(int)(int*,int）)即是整型---->（*ff(int))即是返回整型的函数-->ff(int)是指向函数的指针-->ff是返回指针的函数
----------------------如何更好的定义指向函数指针的指针-----------------
typedef int fuc(int)    //把fuc声明为返回int参数为int的函数类型
typedef fuc* fuc_ptr     //把fuc_ptr声明为指向函数fuc的指针类型
typedef fuc_ptr* fuc_ptr_ptr  //把fuc_ptr_ptr声明为指向函数指针fuc_ptr的指针类型
fuc_ptr_ptr p   //p为指向函数指针的指针

> 24.  typedef int PARA   //int PARA是个整体
      e.g. typedef int a[10]    即表示 a为具有10个int元素的数组的别名
	  e.g. typedef void(*p)(void)  即表示p为指向函数指针的别名

> 25.构造函数分两个阶段执行（1）：初始化阶段；（2）普通的计算阶段 。计算阶段则由构造函数体中的所有语句组成。

> 26.如果没有为类成员提供初始化式，则编译器会隐式的使用成员类型的默认构造函数。如果那个类没有默认构造函数，则编译器尝试使用默认构造函数将会失败。

> 27.构造函数初始化列表不决定初始化的顺序，成员被初始化的次序就是定义成员的次序。

> 28.抑制由构造函数定义的隐式转换

```
class Sale_item{
public: 
     Sale_item(const std::string &book=' ');
     {}
     Sale_item(std::istream &is);
     bool same_isbn(Sale_item new){}
     };
 string null_book ="9-999-9999-9";
 item.same_isbn(null_book);      //这段程序使用一个string类型对象作为实参传给Sales_item的same_isbn函数。该函数期待
 //一个Sale_item对象作为实参。所以编译器会通过隐式转换，使用一个接受string的Sale_item构造函数从null_book生成一个新的
 //sale_item对象。新生成的（临时的）Sale_item被传递给same_isbn。这个Sale_item对象是一个临时对象。一旦same_isbn函数结束，
 //就不能再访问它，实际上，我们构造了一个测试完就会被丢弃的对象。
 //正确做法：
 class Sale_item{
public: 
     explicit Sale_item(const std::string &book=' ');
     {}
     explicit Sale_item(std::istream &is);
     bool same_isbn(Sale_item new){}
     };
 ```
> 29.友元可以是普通的非成员函数，或前面定义的其他类的成员函数，或整个类。将一个类设为友元，友元类的所有成员函数都可以访问授予友元关系的那个类的非公有成员。
```
class Screen{
    friend class Window_Mgr;
    friend Window_Mgr&
       Window_Mgr::relocate(Window_Mgr::index,Window_Mgr::index,Screen&);
       };
       ```
       
