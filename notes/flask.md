##### flask开发环境搭建

1. 安装python环境（python3.x）

2. 检查python和pip是否安装好（Python2.x需要手动安装pip；python3.x默认安装）

3. 新建项目文件

4. 配置虚拟环境（使用虚拟环境的好处？兼容多个python版本）

   - 使用virtualenv（widows环境上涉及到一些权限问题）
   - 使用pipevn

   pipenv是一个工具，使用pipenv创建虚拟环境，创建的虚拟环境和项目之间的关系？虚拟环境和项目绑定，给每个项目创建一个单独的虚拟环境

   1、pipevn安装：

   pip install pipenv

   2、在项目目录下安装虚拟

   pipenv install

   ![](D:\github\flask_project\images\pipenv_install.png)

   3、进入pipenv创建的虚拟环境

   pipenv shell

   ![](D:\github\flask_project\images\pipenv_shell.png)

   4、在虚拟环境中安装flask

   pipenv install flask

   ![](D:\github\flask_project\images\pipenv_install_flask.png)

   5、退出虚拟环境

   exit

   6、在虚拟环境中卸载

   pipenv uninstall flask

   7、在虚拟环境中查看依赖包关系

   pipenv graph

   8、pipenv更详细的命令查看官方文档

   [pipenv官方文档](https://github.com/pypa/pipenv)

   



