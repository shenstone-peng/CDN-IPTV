--------------------------------------------------------------------------------
-------------------------7.19----------------------------------------------------
今日总结：
1、学习《C++primer》，复习了数组和指针，动态数组的创建和内存释放，循环和判断语句，异常处理，以及函数参数（引用参数，数组参数，容器形参等），内联函数，类的成员函数和重载函数。
明日计划：
1.继续学习《C++primer》，标准IO库以及容器
---------------------------------------------------------------------------------
-------------------------7.20----------------------------------------------------
今日理解难点：
1.指向函数的指针以及指向函数指针的指针
int a; //a即是整型
int *p; //*p即是整型-->p即指向整型的指针
int (*p)(int);//(*p)(int)即是整型-->(*p)即是返回整型的函数-->p即是指向这个函数的指针
指向函数指针的指针的正确写法：
int (**p)(int);//(**p)(int)即是整型-->(**P)即是返回整型的函数-->(*p)即是指向这个函数的指针-->p即是指向函数指针的指针
指向函数指针的指针的错误写法即分析：
int *(*p)(int);//*(*p)(int)即是整型-->(*p)(int)即是指向这个整型的指针-->(*p)即是返回这个指针的函数-->p即是指向这个函数的指针
int **p(int);//**p(int)即是整型-->*p(int)即是指向这个整型的指针-->p(int)即是指向这个指针的指针-->p即是返回指针的指针的函数
----------------------如何更好的定义指向函数指针的指针-----------------
typedef int fuc(int)    //把fuc声明为返回int参数为int的函数类型
typedef fuc* fuc_ptr     //把fuc_ptr声明为指向函数fuc的指针类型
typedef fuc_ptr* fuc_ptr_ptr  //把fuc_ptr_ptr声明为指向函数指针fuc_ptr的指针类型
fuc_ptr_ptr p   //p为指向函数指针的指针


今日总结：
1.声明成员函数是必需的，而定义成员函数则是可选的。在类内部定义的函数默认为inline。
2.声明一个类但不定义它，称为不完全类型or前向声明。不完全类型的类的数据成员可以是指向自身类型的指针或引用。
3.定义类时不分配存储空间，定义类的对象时才分配存储空间。
4.初始化const或引用类型数据成员的唯一机会是在构造函数初始化列表中。
5.成员被初始化的次序就是定义成员的次序。
6.通常，除非有明显的理由想要定义隐式转换，否则，单形参构造函数应该为explicit。将构造函数设置为explicit可以避免错误，并当转换有用
时用户可以显式构造对象。
7.static成员函数不能声明为const也不能声明为虚函数。
8.复制初始化首先使用指定构造函数创建一个临时对象，然后用复制构造函数将那个临时对象复制到正在创建的对象。
---------------------------------------------------------------------------------
-------------------------7.22----------------------------------------------------
今日学习重点：
1.复制构造函数的三个使用场景：
   1）当用一个对象去初始化同类的另一个对象时，会引发复制构造函数被调用。
   2）如果函数F的参数是类A的对象，那么当F被调用时，类A 的复制构造函数将被调用。
   3）如果函数的返回值是类A的对象，则函数返回时，类A的复制构造函数被调用。
2.接受单个形参且未指定为explicit的构造函数定义了从其他类型到类类型的转换，重载操作符转换函数则定义了从类类型到其他类型的转换。
转换操作符必须为所转换类的成员，没有形参并且不定义返回值，转换操作符返回操作符所具有类型的值。
3.派生类只能通过派生类对象访问其基类的protected成员，派生类对其基类类型对象的protected成员没有特殊访问权限。




今日总结：
1.参加部门三级培训“部门整体”、“部门合规”和“敏捷之旅”
2.完成macfee杀毒软件设置和文档安全
3.学习C++ primer中基类，派生类，友元，构造函数和析构函数。

明日计划：
1.下午参加部门三级培训
2.学习CDN业务相关知识
3.学习C++和linux
---------------------------------------------------------------------------------
-------------------------7.23----------------------------------------------------
今日学习重点：
1.对象的实际类型可能不同于该对象引用或指针的静态类型，这是C++种动态绑定的关键。
e.g.  class item_base{};
      class bult_item:public item_base{};
	  void print_total(ostream &os,const item_base &item,size_t n){
	     os<<item.ne_price(n)<<endl;//ne_price()为虚函数
		 }
	item_base base;
	bult_item derived;
	print_total(cout,base,10);  //调用基类的net_price()
	print_total(cout,derived,10);//调用派生类的net_price()
	引用和指针的静态类型与动态类型可以不同,这是C++用以支持多态性的基石。
	
今日疑问：
1.在IPTV CDN（870业务）架构中STB是什么以及什么作用？（已了解，机顶盒）
2.IPTV的架构之间的关系和区别是什么呢？

今日总结：
1.学习C++ PRIMER派生类与基类的转换与继承，虚函数的作用，友元关系的继承。
2.学习单板装系统（似乎单板或者光盘有问题，朱志文带着我们装了两次都没成功）
3.学习“cdn功能和架构.ppt” 了解cdn应用项目，IPTV的多种系统架构
4.参加部门三级培训，学习了开发流程，编码规范和软件设计原则。印象最深的是前期写代码的规范对后期的维护和修改的重要性。

明日计划：
1.继续学习C++和CDN功能和架构
2.继续参加部门三级培训
3.继续装系统

-------------------------7.24----------------------------------------------------
今日总结：
1.参加部门三级培训，学习了Linux基础，shell和nginx基础
2.学习cdn功能和架构和cdnIPTV技术架构
明日安排
1.参加部门三级培训
2继续学习cdn
3继续装系统
---------------------------------------------------------------------------------
-------------------------7.25----------------------------------------------------
今日总结：
1.参加部门三级培训，学习了pg数据库基础，lua脚本语言，Java基础和KW
2.单板装好系统，并配置了网络
3.学习了CDN整体拓扑结构.PPT

今日问题：
1.为什么在putty上远程连接成功后，使用一段时间会出现断开连接呢？而且有时候连接不上，过一会又可以连接。
明日安排：
1.继续学习cdn相关业务
2.继续学习Linux
3.参加部门三级培训 
---------------------------------------------------------------------------------
-------------------------7.26----------------------------------------------------

今日总结：
1.参加部门三级培训，学习了c语言
2.单板学习了自启动配置，并在设置了开门狗和网络配置的自启动
3.学习了Linux目录和文件权限


明日安排：
1.继续学习cdn相关业务
2.继续学习Linux

https://blog.csdn.net/liudongdong19/article/details/79774171
---------------------------------------------------------------------------------
-------------------------7.27----------------------------------------------------
今日疑问：
1.在/etc/rc.d/中存放的是不同运行级别下该选择运行的脚本，比如运行级别3就运行/etc/rc.d/rc3.d/中的脚本  
但我在里面没有找到之前自己设置的netconfig和watchdog脚本（已确定设置开机自启动），不太明白为什么没有。  
已解决：这是sysvinit系统时的流程，在systemd系统中，会在启动multi-user.target(运行级别3）后，寻找所依赖的
其他unit（包含netconfig.service和watchdog.service）
2.
---------------------------------------------------------------------------------
-------------------------7.29----------------------------------------------------

今日总结：
1.复习三级培训中Linux、NGINX和shell的ppt
2.参加部门三级培训，学习了“大视频业务整体架构及关键流程”“cdn业务整体架构及管件流程”和大视频分析整体架构“
明日计划：
1.复习其他三级培训课程
2.参加部门三级培训
---------------------------------------------------------------------------------
-------------------------7.30----------------------------------------------------
今日总结：
1.复习shell，Java和c并完成Linux和shell课程的作业
2.参加部门三级培训与部长面对面
明日计划：
1.复习其他三级培训课程
2.新人汇报

今日问题：
shell有个作业研究了一上午没做出来。。
题目：在自己姓名缩写的用户主目录下, 用自己的用户创建一个shell，执行完成以下功能  
1、从/var/log/messages中过滤存在root字符的信息存放到当前目录下，取名为testfile  
2、打开testfile逐行检测，第6个列为(root)的，则输出到testfile1,否则忽略  
3、将testfile1中的” (root)” 替换成supperuser，保存为testfile2
第一题取得的数据结构如下：
Jul 26 17:44:57 localhost kernel: pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
Jul 26 17:44:57 localhost kernel: pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
Jul 26 17:44:57 localhost kernel: pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
Jul 26 17:44:57 localhost kernel: pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000dffff window]
Jul 26 17:44:57 localhost kernel: pci_bus 0000:00: root bus resource [mem 0xf0000000-0xfed8ffff window]
第二题应该是用awk命令将第六列有root的每行保留，但是如何选择分隔符，如果只是空格，第一列时间就会表示为三列
，就是不知道时间那一列该怎么分出来，所以这题没做出来。
