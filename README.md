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
##### 分析
实际上通过libtorch的c++接口对pytorch进行扩展与通过torch.autograd.Function进行扩展类似,我们可以通过使用pytorch前端继承Function实现forward和backward函数来实现标准的pytorch算子(计算图节点),然后通过继承torch.nn.Module类封装成标准的神经网络模块.不同的是forward函数和backward函数的实现,我们不再使用pytorch前端去写,因为pytorch前端实现这些操作是低效的,一方面是多次调用cuda kernel,一方面是python解释器拖慢了代码速度.所以我们通过pybind11使用C++实现forward函数和backward函数,然后将其绑定到python函数中,因为pytorch封装的tensor和libtorch的相同,这给我们提供了合适的接口,我们可以将python的数据结构传递到c++代码中,使用c++实现forward函数和backward函数.最终在python中调用.
还有进一步的优化空间,使用cuda进行进一步优化.
