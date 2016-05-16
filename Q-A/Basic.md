#####自述

---

* [Python中with as的用法](#with-as)


---
<h5 id = 'with-as'>Python中with as的用法</h5>

**问题描述**

> Python中with as是怎么用的呢？

> 在课程视频和源码中，我们有这样的演示：

<pre><code>
with open('file_path','r+') as file_obj:
    do something...
</code>
</pre>

**问题解答**

其实，打开文件分为最基本的```①打开文件 -> ②进行文件操作 -> ③关闭文件 ```这三个步骤，然而在第1步，以读取方式```r```打开文件的话，如果文件本身不存在是会报错的，程序也就停止运行了；读取完数据之后，也要进行文件的关闭，如果打开很多文件都忘记关闭会造成计算机内存的消耗。

所以，Python中除了```with as```，还可以这样打开文件：

```
try:
    f = open('xxx')
    #如果异常
except:
    print 'fail to open'
    exit(-1)
try:
    do something
except:
    do something
finally:
    f.close()
```

也就是```try except finally```用法，不管文件在操作中有没有完成，一定会保证```finally f.close()```，也就是一定会保证文件会关闭。

那么问题来了，Python号称简洁优雅，于是用```with as```的语法特性代替了以上的```try except finally```，只要如以下写：
```
with open('file_path','r+') as file_obj:
    do something...
```
就不用主动去获取异常和关闭文件，极大简化了编程工作，这就是```with as```的用法。