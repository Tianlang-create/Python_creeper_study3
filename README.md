# 第3 节：动态网页抓取

*Date in 21/11/2024 Made by Tianlang*

声明：仅供个人学习使用  参考资料来源于 **Python网络爬虫从入门到实践**

## 3.1 动态抓取的实例

### 1>针对AJAX技术加载的网页的爬取办法

​		**AJAX*(Asynchronous Java-script And XML)***  是一种异步更新技术，价值在于通过后台与服务器进行少量数据交换可以使网页实现异步更新 

* 通过浏览器审查元素解析地址
* 通过Selenium模拟浏览器抓取 

### 2>AJAX技术实践

​	    打开一个网页的不同按钮，界面跳动但总体URL不变，评论等如一个容器（示例略）



## 3.2 解析真实地址抓取

**步骤一：**打开“检查”功能。用Chrome浏览器打开“Hello World”文章。右键页面任意位置，在弹出的对话框中，点击“检查”选项。得到如下图所示的对话框。

**步骤二：**找到真实的数据地址。点击对话框中的Network，然后刷新网页。此时，Network 会显示浏览器从网页服务器中得到的所有文件，一般这个过程称之为“抓包”。因为所有文件已经显示出来，所以我们需要的评论数据一定在其中。

**步骤三：**爬取真实评论数据地址。既然找到了真实的地址，我们就可以直接用requests请求这个地址，获取数据。

```python
import requests

link ="https://api-zero.livere.com/v1/comments/list?callback=jQuery112407916776725405603_1732201378464&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1732201378466"
headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
}

r=requests.get(link,headers=headers)
print(r.text)

```

**步骤四：**从 json数据中提取评论。上述的结果比较杂乱，但是它其实是 json 数据，我们可以使用 json 库解析数据，从中提取我们想要的数据。

```python
import json
# 获取 json 的 string
json_string = r.text
json_string = json_string[json_string.find('{'):-2]
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']
for eachone in comment_list:
    message = eachone['content']
    print (message)
```



### 简化

网页 URL地址的规律，并用for循环爬取，就会非常轻松<u>只需在URL中改变 offset 的值，便可以实现换页</u> 

```python
for page in range(1,4):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963316"
    page_str = str(page)
    link = link1 + page_str + link2
    print (link)
    single_page_comment(link)
```



## 3.3通过Selenium模拟浏览器抓取

​		在之前的实践中，我们是使用浏览器的<u>检查</u>功能查找源地址（*在页面中可以看到json格式中的超链接） **这种方法显然比较笨拙**

​		于是有另一种方法——**使用浏览器渲染引擎** 过程为：1>打开一个浏览器自动加载网页 2>自动操作浏览器浏览各个网页，抓取数据  **或者认为变成爬取静态网页**



### 1>Selenium的安装

```powershell
pip install selenium
```

​     <u>新版需要再安装geckodriver（Pycharm里直接下载）</u>

```python
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.github.com/Tianlang-create/")
```

​      此时直接打开了页面说明安装完成