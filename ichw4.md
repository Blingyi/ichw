# 作业4
1.解释作业、进程、线程的概念，进程和线程概念的提出分别解决了什么问题？

作业：用户向计算机提交的任务实体, 通常体现为用户运行一个程序

进程：计算机为了完成用户任务实体而设置的执行实体

线程：是系统独立调度和分派CPU的基本单位指令运行时的程序的调度单位

进程提出所解决的问题：现代计算机的 CPU 和多数 I/O 设备同一时刻只能处理一个任务，为了满足多道程序同时运行提出了进程概念

线程提出所解决的问题：解决了单个程序占据CPU或I/O设备时间过长，导致其它程序无法正常运行而造成的时间的浪费；也避免了多个进程同时运行所需要极大的设备消耗，
                    防止低优先级进程被饿死，从而出现了分时系统和线程



2.调研虚拟存储器的概念，描述其工作原理和作用

概念：虚拟内存是计算机系统内存管理的一种技术。它使得应用程序认为它拥有连续的可用的内存（一个连续完整的地址空间），而实际上，它通常是被分隔成多个物理内存
      碎片，还有部分暂时存储在外部磁盘存储器上，在需要时进行数据交换。

工作原理：

         ①中央处理器访问主存的逻辑地址分解成组号a和组内地址b，并对组号a进行地址变换，即将逻辑组号a作为索引，查地址变换表，以确定该组信息是否存放在主存内。
         
         ②如该组号已在主存内，则转而执行④；如果该组号不在主存内，则检查主存中是否有空闲区，如果没有，便将某个暂时不用的组调出送往辅存，以便将这组信息调入主存。
         ③从辅存读出所要的组，并送到主存空闲区，然后将那个空闲的物理组号a和逻辑组号a登录在地址变换表中。
         ④从地址变换表读出与逻辑组号a对应的物理组号a。
         ⑤从物理组号a和组内字节地址b得到物理地址。
         ⑥根据物理地址从主存中存取必要的信息。

作用：电脑中所运行的程序均需经由内存执行，若执行的程序占内存很大或很多，则会导致内存消耗殆尽。为解决该问题，系统匀出一部分硬盘当内存，从而扩大了计算机内
      存。虚拟内存是Windows 为作为内存使用的一部分硬盘空间。虚拟内存在硬盘上其实就是为一个硕大无比的文件，文件名是PageFile.Sys，通常状态下是看不到的。
      必须关闭资源管理器对系统文件的保护功能才能看到这个文件。
