Title: Stackoverflow [scrapy] experience.
Date: 2016-09-14
Tags: scrapy, python, stackoverflow
Slug: scrapy-stackoverflow
Summary: Starting up the blog with Python and Pelican static blog generator!

_"People suck at asking questions"_

After spending over a month answering `scrapy`\* related questions I've decided to share my experience. I'll point out few things that I've learned from this little experiment and few other related comments.

#The Good
There are surprisingly **a lot of questions** with this scrapy tag on stackoverflow.

![scrapy stackoverflow stats 2016-09-14]({filename}/images/scrapy_stackoverflow1.png)

First things you notice in this picture is that the percentage of "unanswered" is quite high for recent questions. Even though that seems to be quite normal for stackoverflow it is still slightly higher than other related tags (e.g. python tag has 44% in the last 30 days right now).   
This brings me back to first point: there are a lot of new scrapy users and majority of them are either new or intermediate python programmers. This is to be expected since web-scraping in general is on the rise. Starting up any project when you can generate a bunch of data with script or two is extremely appealing to beginners and veterans alike.  
One thing I've noticed that **people who ask questions are generally pleasant** - willing to learn, change and work to resolve the issue.

#The Bad
![scrapy stackoverflow generic question]({filename}/images/scrapy_stackoverflow2.png)  
The question quality is pretty poor, even compared to general stackoverflow quality. A lot of questions don't seem to be focused on general solutions but on individual problems which as far as I know is against the general rules of stackoverflow. However people seems to be giving it a pass since there is no other place to get answers to questions like this (shout out to #scrapy @ freenode).  

###Common Issues
**AJAX**  
<img style="float: left;" src='{filename}/images/scrapy_stackoverflow5.png' height=100>By far the most common issue is dealing with AJAX. What a scary name for something so simple."Asynchronous JavaScript and XML" which in the scope of web-crawling just means _make request for some data_, in other words it's just a javascript made request that retrieves some data. Usually this is used for product urls in pagination or images urls stored on some other server.  
There's a huge question that [covers scrapy and AJAX here](http://stackoverflow.com/questions/8550114/can-scrapy-be-used-to-scrape-dynamic-content-from-websites-that-are-using-ajax?rq=1). However I find the answers to be pretty bad and do not fully cover the issue or cover a completely different issue(see Selenium in The Ugly part).  
However there is a great blog post by Scrapinghub called [Scraping Infinite Scrolling Pages](https://blog.scrapinghub.com/2016/06/22/scrapy-tips-from-the-pros-june-2016/) which is a must read if you're new to this! 

**CrawlSpider**  
<a href='{filename}/images/scrapy_stackoverflow3.gif'>![Please stop using CrawlSpider]({filename}/images/scrapy_stackoverflow4.png)</a>  
I'm now sure whom to blame here, but for some magical reason everyone decided to use [`CrawlSpider`](http://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider) scrapy spider instead of base `srapy.Spider`.  
`CrawlSpider` automates a lot of crawling logic by using `Rule` objects which have a lot of bells and whistles to configure how and what a spider should crawl. I personally dislike `CrawlSpider` but even with it's benefits it hides so much from the user that I would **never recommend it to a new user**.   
I have the [documentation page](http://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider)of it bookmarked myself because of how confusing it can get.
