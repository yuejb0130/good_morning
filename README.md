# morning
微信公众号天气预报推送
最近微信公众平台每日的天气预报推送刷屏了

我也要给自己的好兄弟/好姐妹安排上。

详细步骤如下：

### 注册微信平台测试号

- 首先搜索微信平台测试号



![](https://secure2.wostatic.cn/static/7euPioZw1fCxDDApo3u8ZT/image.png)

- 进入测试号，微信扫码登录，进入后大致页面如下(为了保证完整一样，我特地用了别人的微信号新注册了一个），切记此处进入后要刷新一下

![](https://secure2.wostatic.cn/static/rqW8Cb5hiujksDvkBqxKd3/image.png)

- 下拉找到创建消息模板接口

![](https://secure2.wostatic.cn/static/5nnX1dhhmw8zai4a6UGXwP/image.png)

- 填写如下内容

![](https://secure2.wostatic.cn/static/mmqTK7qrUkaZKm1Q9nzn9j/image.png)

我知道有人懒得自己打字，所以我特地复制出来了，hhh

```PowerShell
今日天气：{{weather.DATA}}
当前温度：{{temperature.DATA}}
今天是我们相识的第：{{love_days.DATA}}天
距离你的生日还有{{birthday_left.DATA}}天{{words.DATA}}

```



中文部分按自己需求修改英文和符号要完全—致

- 点击提交
- 接下来让你的好兄弟扫描你的测试账号二维码关注这个公众号，刷新一下出来了用户名称和微信号。

![](https://secure2.wostatic.cn/static/fQUfTv3D7FDJ9xP1qWtttH/image.png)

以上操作如果有一个公众号会更加方便，这里仅作测试使用。

### 打开GitHub进行接下来的操作

国内访问有些慢，这个解决办法我明天更新，有条件的先冲

这个是我的个人复制别人的GitHub

[https://github.com/99memory/goodmorning_my_brother](https://github.com/99memory/goodmorning_my_brother)

别人的原来的github地址为：（由于这个教程写的比较笼统所以我自己更新了一下下）

[https://github.com/wyz8883/morning](https://github.com/wyz8883/morning)

- 复制别人的github代码，点击这里的fork进行一个复制的操作

![](https://secure2.wostatic.cn/static/8pp1C7SudPvDzGGzyRCBvi/image.png)

- 进入复制的仓库，点击action(为了保证完全一样我又特地搞了一个新的GitHub账号演示）

![](https://secure2.wostatic.cn/static/sQZVRpiPFEjoPyTqprsGv2/image.png)



- 接下来点击settings→ Secrets → Actions 。

![](https://secure2.wostatic.cn/static/99QGL3YNgaKpAKVubsqxMd/image.png)

- 点击New repository secret

![](https://secure2.wostatic.cn/static/sV6HjF6SgpsxksjPqwAGsQ/image.png)

- 接下来我们刚才在微信公众号中的一串奇怪的代码就有了用途了，这里添加一个APPID和value

![](https://secure2.wostatic.cn/static/5nCJBLdfJs4niqDZgHi7Z5/image.png)

- 接下来依次添加APP_SECRET 、BIRTHDAY 、CITY 、START_DATE 、TEMPLATE_ID 、USER_ID
- 下面我将依次解释这些值的意义以及在哪里
1. APP_ID  微信测试号的ＩＤ
2. APP_SECRET 微信测试号的secret
这两个在测试平台最上面获取

![](https://secure2.wostatic.cn/static/GubRvSiZ9iCFkLc9mXHrF/image.png)

  3.  BIRTHDAY  生日  格式:   05-20

  4.  CITY  城市     格式: 开封 城市请写到地级市，比如：`北京`，`上海`，郑州

  5. START_DATE  纪念日   格式: `2022-09-09`   请注意区分

  6.TEMPLATE_ID 模板ID(用于接口调用)	在刚才新建测试模板那里获取

![](https://secure2.wostatic.cn/static/5bvJ4hz3VMBEfayRG5RdBD/image.png)

  7.USER_ID 用户ID  在关注用户那里获取

![](https://secure2.wostatic.cn/static/41cKDG46ppswsWTyUFW2hY/image.png)

最后浅浅汇总以下所有参数

```PowerShell
APP_ID
APP_SECRET
BIRTHDAY
CITY
START_DATE
TEMPLATE_ID
USER_ID

```

![](https://secure2.wostatic.cn/static/ejGQhpspcytaQDrZsEPRet/image.png)

- 接下来进行action的操作,点击action→morning 如下

![](https://secure2.wostatic.cn/static/d9jQEjMhWWVWCUdwjtZVwp/image.png)

- 运行开始了

![](https://secure2.wostatic.cn/static/vkL4QxJzaS3heTb8rZxaqX/image.png)

绿色表示运行成功,黄色表示正在运行,红色表示错误,有问题的话可以私信发我,或者issue

![](https://secure2.wostatic.cn/static/5ejDcgjtAH4xvgKkrMaUwp/image.png)

一般错误的话就是自己的一些参数填错了哦(记得公众号测试平台一定要刷新一遍再使用里面的参数)

大家可以先自己好好看看,再私信我.qaq.

### 最后就是展示效果了啊

![](https://secure2.wostatic.cn/static/a5TJ3rBUMZvyupBJjzQSNX/image.png)

这个是每天早上8点会自动发送的哦

以上参考自

[https://github.com/wyz8883/morning](https://github.com/wyz8883/morning)

我个人只是提供整合教程,方便大家实验.
