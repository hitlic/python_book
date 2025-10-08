# Python编程从入门到提高

清华大学出版社《Python编程从入门到提高》源代码及课件。

## 内容

- 源代码
  - `codes`
- 课件：Jupyter notebook格式的幻灯片
  - `notebook_slides`

## 课件使用

详细说明参见`notebook_slides/课件使用说明.md`。

### 仅使用Notebook显示

- 安装Jupyter
  - 使用pip：`pip install jupyter`
  - 使用conda：`conda install jupyter`
- 运行jupyter notebook
  - 在终端进入课件所在目录
  - 运行命令`jupyter notebook .`即可

### 使用幻灯片显示

- 由于幻灯片使用了基于 notebook<7.0 的RISE插件，可按如下方式安装所需工具包的正确版本。

  ```bash
  # 1. 创建新的python环境，并激活启动（3.8-3.12都可以）
  # 2. 安装兼容的 Jupyter Notebook 核心组件
  pip install -U notebook==6.5.7 jupyter_server==1.24.0 nbclassic==0.5.6 jupyter_nbextensions_configurator==0.6.3
  
  # 3. 安装、配置 RISE 幻灯片扩展
  pip install rise==5.7.1
  jupyter-nbextension install rise --py --sys-prefix
  jupyter-nbextension enable rise --py --sys-prefix
  
  # 5.（可选）安装配置 contrib_nbextensions（jupter notebook常用插件）
  pip install jupyter_contrib_nbextensions==0.7.0
  jupyter nbextensions_configurator enable --sys-prefix
  jupyter contrib nbextension install --sys-prefix
  jupyter nbextension enable toc2/main --sys-prefix
  ```

- 运行jupyter notebook
  - 在终端进入课件所在目录
  - 运行命令`jupyter notebook .`
- 在弹出的浏览器中选择一个课件打开，点击下图所示的图标即可以幻灯片形式显示
  ![幻灯片示意图](rise.png)
