# Data Science Project Template

🧠 数据科学项目模板

> 知名炼丹师有云：**合理的「项目结构」是成功的起点！**

## 1 目录简介

```
.
├── README.md          # 简介
├── app                # 应用
│   ├── test.py
│   └── train.py
├── notebook           # 交互（可选）
├── model              # 模型（可选）
├── data               # 数据
├── util               # 辅助
│   ├── conf.py
│   ├── log.py
│   ├── data_model.py
│   ├── db.py
│   └── data.py
├── save               # 保存
├── conf               # 配置
│   ├── default.prod.yml
│   ├── default.test.yml
│   └── default.yml
├── script             # 脚本
│   ├── env.sh
│   ├── test.sh
│   └── train.sh
├── server             # 部署（可选）
│   └── app.py
├── test               # 测试（可选）
├── doc                # 文档（可选）
├── log                # 日志
├── requirements.txt   # 依赖（可选）
└── LICENSE            # 许可
```

### 1.1 README.md（文档）

**一个详尽的文档比什么都重要！** 任何人都可以通过文档快速上手。也许你会说，我的代码就我自己看，不写文档也知道。可是你能保证三个月以后，你还记得你当初写的什么吗？！

一个好的深度学习项目文档应该是怎样的？

1. 环境依赖说明
2. 快速运行脚本
3. 类似项目比较
4. 性能测试结果
5. 细致版本记录
6. 相关参考资料

参考：

1. [如何写好Github中的readme？](https://www.zhihu.com/question/29100816)
2. [如何为你的开源项目编写实用的文档](https://zhuanlan.zhihu.com/p/120399648)

### 1.2 app（应用入口）

这里是核心应用的入口，比如训练文件 `train.py` 和测试文件 `test.py`，当然也可以把一些中间过程放在此处，比如提取特征 `extract_feature.py` 等。

推荐使用 `python -m app.train` 这样的方式运行，以避免出现 package 的引用问题。

### 1.3 notebook（交互编程｜可选）

`jupyter notebook` 是一个集成了 `ipython` 的可视化交互代码工具，可以方便的查看中间变量和记录想法，特别适合做数据处理和数据可视化。

> 知名炼丹师有云：炼丹师的工作划分——「80% 清理数据，20% 调节参数」

数据科学两兄弟——`numpy` 和 `pandas` 是不可或缺的！在 notebook 中会大量使用到～

对于大规模数据，建议先读取部分数据，在 notebook 上编写数据处理管道，最后抽象成函数放到 app 目录下运行。

### 1.4 model（算法模型｜可选）

这里一般放「神经网络」或者是机器学习的算法结构。

比如包含 `torch.nn.Module` 的文件。

### 1.5 data（数据）

所有的数据的堆放处，最常见的就是「数据集」。

如果数据集比较大，建议在专门的磁盘中进行存储管理，通过软链接的方式映射到 ./data 目录下面。

```shell
ln -s /path/to/dataset ./data/dataset
```

> ⚠️ 注意：
> 删除软链接是 `rm -rf ./data/dataset`，
> 而不是 `rm -rf ./data/dataset/`，
> 第二命令做法会把源数据删掉！切记！切记！

### 1.6 util（辅助工具）

一些常见的辅助函数，比如：

1. conf 配置
2. data 数据
3. data_model 数据模型
4. log 日志
5. db 数据库

### 1.7 save（结果保存）

模型参数、性能测试结果等...

### 1.8 conf（配置中心）

所有的配置都是用 `YAML`，它比 `json` 更好用，可以在配置中添加注释，并且呈现方式也更为直观！

配置文件的中间名称是「环境变量」，比如 ENV 为 `test` 时，就会读取 `default.test.yml` 文件（ENV 默认为 `dev`，会读取 `default.yml`）。

如何使用环境变量 ENV 呢？只需要在执行时，把 `ENV=test` 添加到命令的最前面。

```
ENV=test python -m app.train
```

### 1.9 script（实用脚本）

对于一些常见的连续命令，我们可以把它整理出来，写成一个脚本，以便快速执行！

比如 `init.sh` 可以让你快速创建 conda 虚拟环境！

### 1.10 server（部署｜可选）

使用 Web 服务部署到线上环境，推荐使用 [Sanic](https://sanic.dev/zh/)。

### 1.11 test（测试｜可选）

与模型的测试不同，这里主要为代码的单元测试 `UnitTest`。

### 1.12 doc（文档｜可选）

如果项目比较复杂，可以将文档整理归纳到这里。

### 1.13 log（日志）

`util/log.py` 会将文件按天记录到这里。

### 1.14 requirements.txt （依赖）

项目所需要的依赖，方便一键安装。

```shell
pip install -r requirements.txt
```

### 1.15 LICENSE（许可｜可选）

如果是开源项目，需要添加许可证。

参考：

1. [一文看懂开源许可证丨开源知识科普](https://pingcap.com/zh/blog/introduction-of-open-source-license)
2. [如何选择开源许可证？](https://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html)

## 2 环境准备

- Ubuntu 18.04 LTS+
- Python 3.7+
- Anaconda 3

> 人生苦短，快用 `*NIX` ！

推荐为每个项目创建单独的虚拟环境。

```shell
conda create -n replace_this_name python==3.7.13 -y
conda activate replace_this_name
```

## 3 TODO

- [ ] dspt init 脚本
- [ ] script 中添加一些常用脚本

## 4 参考

- [Ubuntu 系统镜像下载](https://cn.ubuntu.com/download)
- [Anaconda 个人版](https://www.anaconda.com/products/individual#)
- [TUNA 清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)

## 5 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
