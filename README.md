# pytestDemo

本项目实现接口自动化的技术选型：**Python+Requests+Pytest+YAML+Allure** ，通过 Python+Requests 来发送和处理HTTP协议的请求接口，使用 Pytest 作为测试执行器，使用 YAML 来管理测试数据，使用 Allure 来生成测试报告。

## 项目说明

本项目在实现过程中，把整个项目拆分成请求方法封装、HTTP接口封装、关键字封装、测试用例等模块。

首先利用Python把HTTP接口封装成Python接口，接着把这些Python接口组装成一个个的关键字，再把关键字组装成测试用例，而测试数据则通过YAML文件进行统一管理，然后再通过Pytest测试执行器来运行这些脚本，并结合Allure输出测试报告。

当然，如果感兴趣的话，还可以再对接口自动化进行Jenkins持续集成。

## 项目部署

首先，下载项目源码后，在根目录下找到 ```requirements.txt``` 文件，然后通过 pip 工具安装 requirements.txt 依赖，执行命令：

```
pip3 install -r requirements.txt
```

接着，修改 ```config/setting.ini``` 配置文件，在Windows环境下，安装相应依赖之后，在命令行窗口执行命令：

```
pytest
```


## 项目结构

- api ====>> 接口封装层，如封装HTTP接口为Python接口
- common ====>> 各种工具类
- config ====>> 配置文件
  - common_config ====>> 多套环境的通用配置
  - dev_config ====>> 测试环境的配置
  - uat_config ====>> 联调环境的配置
  - prod_config ====>> 生成环境的配置
  - file_path_config ====>> 文件路径
- core ====>> requests请求方法封装、关键字返回结果类
- data ====>> 测试数据文件管理
- log ====>> 日志
- operation ====>> 关键字封装层，如把多个Python接口封装为关键字
- report ====>> 测试报告
- testcases ====>> 测试用例
- utils ====>> 自定义方法
- conftest ====>> pytest的配置
  - EnvConfig  ====>> 读取指定的测试/运行环境配置
  - pytest_addoption  ====>> 添加命令行指定运行哪一个测试/运行环境
  - db  ====>> 初始化数据库连接
  - Access_token  ====>> 发送接口获取token,并且写入到/config/access_token目录下，接口读取使用
- pytest.ini ====>> pytest配置文件
  - “addopts =  --env=dev” ====>> 指定运行哪个环境，命令行的优先级大于pytest.ini文件，pytest.ini文件大于/conftest.py/EnvConfig
- requirements.txt ====>> 相关依赖包文件

## 关键字封装说明

关键字应该是具有一定业务意义的，在封装关键字的时候，可以通过调用多个接口来完成。在某些情况下，比如测试一个充值接口的时候，在充值后可能需要调用查询接口得到最新账户余额，来判断查询结果与预期结果是否一致，那么可以这样来进行测试：

- 1, 首先，可以把 **```充值-查询```** 的操作封装为一个关键字，在这个关键字中依次调用充值和查询的接口，并可以自定义关键字的返回结果。
- 2, 接着，在编写测试用例的时候，直接调用关键字来进行测试，这时就可以拿到关键字返回的结果，那么断言的时候，就可以直接对关键字返回结果进行断言。

## 测试报告效果展示

在命令行执行命令：```pytest``` 运行用例后，会得到一个测试报告的原始文件，但这个时候还不能打开成HTML的报告，还需要在项目根目录下，执行命令启动 ```allure``` 服务：

```
# 需要提前配置allure环境，才可以直接使用命令行
allure serve ./report
```

最终，可以看到测试报告的效果图如下：

![image.png](https://upload-images.jianshu.io/upload_images/16853007-248f805c82dbf99c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
