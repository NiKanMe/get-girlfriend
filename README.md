# 微信自动推送模板

#### 介绍
微信自动推送天气等API模板  

微信公众号测试号平台 https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login  
腾讯云函数 https://cloud.tencent.com/product/scf  
#### 需要什么？
1.云函数或者服务器  
2.耐心  
3.一个微信公众号，或者微信公众号测试号  

#### 安装教程

1.  下载wechat-auto-push-template.zip到本地  
2.  上传到腾讯云函数（新用户免费使用三个月）
    2.1    登录腾讯云函数  
    2.2    点击函数服务  
    2.3    点击新建  
    2.4    点击从头开始配置函数名称 运行环境Python3.7 选择本地上传zip包 在函数代码那一栏中上传wechat-auto-push-template.zip 点击完成
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823215626a.png)
3.  登录微信测试平台 获取appID等参数 同时扫码获取用户ID  
4.  填入云函数中（云函数-管理控制台-函数服务-点击函数名称-函数管理-函数代码点击src-点击index.py）
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823220629.png)
红色框中全部配置成自己的参数 以下是示例：
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823221028.png)
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823221005.png)
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823220944.png)
分别按照index.py文件中注释填写即可
最后效果
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823221340.png)
点击部署 部署完成以后点击测试
下方提示发送成功
代表消息已经发送 快查看一下吧~
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823221603.png)
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823221652.jpg)
最后设置定时触发 填写好朋友的用户ID就可以每天定时发消息啦
5.  定时触发设置方法(云函数-管理控制台-函数服务-点击函数名称-函数管理-触发管理-创建触发器）
![输入图片说明](png%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220823221959.png)
如上图 就表示每天上午10点发送消息
具体时间设置参考[https://cloud.tencent.com/document/product/583/9708#cron](http://)

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
