Status: Draft
Title: Stackoverflow [scrapy] Experience: The Bad
Date: 2016-09-14
Tags: scrapy, python, stackoverflow, bad
Slug: scrapy-stackoverflow-bad
Summary: The bad bits of my experience with stackoverflow scrapy tag

_"People suck at asking questions"_

After spending over a month answering [`scrapy`](https://github.com/scrapy/scrapy) related questions I've decided to share my experience. I'll point out few things that I've learned from this little experiment and few other related comments. The quote above is a good generalization but there are a lot of good and interesting to add, for that see my previous post.

#The Bad
![scrapy stackoverflow generic question]({filename}/images/scrapy_stackoverflow2.png)  
The question quality is pretty poor, even compared to general stackoverflow quality. A lot of questions don't seem to be focused on general solutions but on individual problems which as far as I know is against the general rules of stackoverflow. However people seems to be giving it a pass since there is no other place to get answers to questions like this (shout out to #scrapy @ freenode).  

##Common Issues
###**AJAX**  
<img style="float: left;" src='{filename}/images/scrapy_stackoverflow5.png' height=100>By far the most common issue is dealing with AJAX. What a scary name for something so simple."Asynchronous JavaScript and XML" which in the scope of web-crawling just means _make request for some data_, in other words it's just a javascript made request that retrieves some data. Usually this is used for product urls in pagination or images urls stored on some other server.  
There's a huge question that [covers scrapy and AJAX here](http://stackoverflow.com/questions/8550114/can-scrapy-be-used-to-scrape-dynamic-content-from-websites-that-are-using-ajax?rq=1). However I find the answers to be pretty bad and do not fully cover the issue or cover a completely different issue(see Selenium in The Ugly part).  
However there is a great blog post by Scrapinghub called [Scraping Infinite Scrolling Pages](https://blog.scrapinghub.com/2016/06/22/scrapy-tips-from-the-pros-june-2016/) which is a must read if you're new to this! 

###**CrawlSpider**  
<a href='{filename}/images/scrapy_stackoverflow3.gif'>![Please stop using CrawlSpider]({filename}/images/scrapy_stackoverflow4.png)</a>  
I'm now sure whom to blame here, but for some magical reason everyone decided to use [`CrawlSpider`](http://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider) scrapy spider instead of base `srapy.Spider`.  
`CrawlSpider` automates a lot of crawling logic by using `Rule` objects which have a lot of bells and whistles to configure how and what a spider should crawl. I personally dislike `CrawlSpider` but even with it's benefits it hides so much from the user that I would **never recommend it to a new user**.   
I have the [documentation page](http://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider)of it bookmarked myself because of how confusing it can get.

Here's a little CrawlSpider versus Spider comparison and why I think CrawlSpider is confusing for beginners:

```python
class MySpider(CrawlSpider):
    name = 'myspider'
    start_urls = ["http://somesite.com")
    rules = [
        Rule(LinkExtractor(restrict_xpaths=['//a[@href]']),
             callback=self.parse_item),
        Rule(LinkExtractor(restrict_xpaths=['//a[@id="cat"]']),
            follow=True),
    ]
    
    def parse_item(self, response):
        ...

    def parse_category(self, response):
        ...
```
First thing rules are confusing, here you have a list of objects that constructs another object with in it's parameters. Both of these objects can have multiple parameters which makes the whole thing super hectic and implicit.  
This is how using base Spider this would look:
```python
class MySpider(Spider):
    name = 'myspider'
    start_urls = ["http://somesite.com")

    def parse(self, response):
        items = LinkExtractor(restrict_xpaths=['//a[@href]']).extract_links(response)
        categories = LinkExtractor(restrict_xpaths=['//a[@id="cat"]']).extract_links(response)
        for item in items:
            yield Request(item.url, self.parse_item)
        for cat in categories:
            yield Request(cat.url)

    def parse_item(self, response):
        ...
```
As you can see this code is completely explicit, you could really get rid of [`LinkExtractors`](http://doc.scrapy.org/en/latest/topics/link-extractors.html#module-scrapy.linkextractors.lxmlhtml) just by using `response.xpath("//a[@href]").extract()` instead. The advantages of using `LinkExtractors` though, is that it filters outs non website files (i.e. pdf, mp3) as well as converting urls to absolute ones.
To understand this all you need is basic scrapy knowledge and the whole chain is predictable, clear and easily accessible for modification.

