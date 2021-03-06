1. 配置虚拟环境
  * virtualenv -p python3.6 venv
  * . venv/bin/activate
  * pip3 install scrapy
  * scrapy
  
  
2. scrapy 自带css 和 xpath 两种数据提取语法
  * scrapy shell [url] 提供了一个交互式的python 环境
  * 载入线上的网页 scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html
  * <pre> 
    载入本地的html文件测试方法：
    from scrapy.http import HtmlResponse
    body=open('example.html').read()
    response=HtmlResponse(url='http://example.com',body=body.encode('utf-8'))  
   </pre>
  
  
  
  
  
  
  
3. css 选择器语法
```
    response.css('div a::text').extract() a标签里面的文本内容
    response.css('div#images a').extract() 整个a标签包括的节点内容
    response.css('div#images a::attr(href').extract() a标签的href 属性内容
    response.css('div#images a::text').extract_first() 第一个a标签下面的文本
    response.css('div#images p::text').extract_first(default='默认值')
    response.css('div#images a img::attr(src)').extract()  图片的路径
    response.css('div[class="类名1 类明2"]').extract()  多个类名的写法
   
```
    
4. xpath 的基本规则

表达式|描述
--|--
nodename|选取此节点的所以子节点
/|从根节点选取
//|	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
.	|选取当前节点。
..	|选取当前节点的父节点。

5. 
<pre>
response.xpath('/html/head/title').extract()  
# ['<title>xpath</title>']
response.xpath('//title').extract()    
# ['<title>xpath</title>']
response.xpath('//h2').extract() 
# 返回所有匹配的h2标签
response.xpath('//h2/text()').extract()
# 只返回h2节点的文本内容
response.xpath('//img/@src').extract() 
# 所有图片的src值
response.xpath('//a/@href').extract() 
# a标签的href值
response.xpath('//p[@class="location"]/text()').extract()  
# 选取所有p 标签`class`属性值为`location`的文本内容
response.xpath('//div[@class="companies"]/div[2]')
# 获取div类名为companies下面的第二个div 的内容
response.xpath('//div[@class="companies"]/div[2]').xpath('.//a/@href').extract()
# 获取div类名为companies下面的第二个div下面的a标签的href值
response.xpath('//div[contains(@class,"类名字")]/text()').extract()
# 获取div包含某个类名的文本内容
</pre>
