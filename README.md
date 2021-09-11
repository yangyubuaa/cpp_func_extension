### 使用libtorch接口进行pytorch的算子扩展
---
##### 文件目录说明:
1. .vscode是vscode c++配置文件
2. cpu里面包含了test.h和test.cpp,分别是libtorch接口函数声明和实现
3. pybind11是c++函数绑定到python对象开源工具
4. setup.py是c++源码的python打包工具
5. test.py将打包的源码注册成pytorch标准的神经网络模块
6. new.py调用test.py中封装的标准审计网络模块进行测试
##### 环境配置说明:
1. 下载pybind11工具并编译
2. 将编译后的pybind11放在项目路径
3. 编写函数的cpp实现
4. 编写函数的h头文件
5. 编写setup.py
6. 安装setuptools
7. 安装libtorch
8. 安装python-dev
9. 运行python3 setup.py install进行打包
10. 使用pip lis查看是否已经打包进python的site-packages
