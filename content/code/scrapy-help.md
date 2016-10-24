Status: Draft
Title: How to get scrapy help.
Date: 2016-10-09
Tags: scrapy, python
Slug: scrapy-help
Summary: Few suggestions how to ask questions correctly to get help for using scrapy framework.

Scrapy is a web-scraping framework for python. It's pretty popular and at the moment of writing it has over 16000 stars [on github](https://github.com/scrapy/scrapy). In terms of codebase scrapy is pretty simple, however there are few things that are not explicit as they could be in favor of abstraction and development simplicity.
So if you do end up not understanding something or encountering some of the few scrapy's quirks, how do you go about it?

First thing you should do is read [how to ask a good question on stackoverflow](http://stackoverflow.com/help/how-to-ask).   
The second bit you should do is learn how to produce a `log`. Scrapy logs majority of the events that happen in your spider, so to debug your spider the best resources are these logs.  
To save a log of your spider run you can use UNIX output redirection syntax:

    scrapy crawl myspider 2>&1 > mylog.log

Explanation:
    `scrapy crawl myspider` - is a scrapy command that will start crawling spider called `myspider`  
    `2>&1` - is UNIX syntax for redirecting error output to standard output. In UNIX there are types of outputs and in your log you want to have both of them in one file.  
    `> mylog.log` - is another UNIX output redirection, but this time we redirect the output to file called `mylog.log`
   


