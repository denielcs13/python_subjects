#####自述

---

* [pip怎么更新Python包](#update)


---
<h5 id = 'update'>pip怎么更新Python包</h5>

pip是一个可执行的脚本文件，设置了环境变量就可以在终端(CMD)里面使用pip命令，而这个命令有一个```--upgrade```或者```-U```参数，英文的意思是```升级```，用来更新包。

所以命令如下：

* ```pip install --upgrade <包的名字>```
* ```pip install -U <包的名字>```

**pip自我更新**

由于pip本身就是一个Python的包，那么用pip来自我更新也是可以的，命令如下：

* ```pip install --upgrade pip```
* ```pip install -U pip```

或者用Python命令参数```-m```选项来安装也是可以的，```-m```的意思是用Python解释器来运行pip再更新，Python更新pip命令如下：

* ```python -m pip install --upgrade pip```
* ```python -m pip install -U pip```

