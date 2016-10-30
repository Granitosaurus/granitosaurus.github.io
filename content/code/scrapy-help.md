Title: How to get scrapy help.
Date: 2016-10-30
Tags: scrapy, python, stackoverflow, web-crawling
Slug: scrapy-help
Summary: Few suggestions how to ask questions correctly and where to ask them regarding using scrapy web-crawling framework.

Scrapy is a web-scraping framework for python. It's pretty popular and at the moment of writing it has over 16000 stars [on github](https://github.com/scrapy/scrapy). In terms of codebase scrapy is pretty simple, however there are few things that are not as explicit as they could be in favor of abstraction and development simplicity.  
Not to mention millions of websites that provide their own unique scraping challenges.  

So if you do end up not understanding something or encountering some of the few scrapy's quirks, how do you go about it?

# Stackoverflow Guidelines

First thing you should do is read is [_how to ask a good question on stackoverflow_](http://stackoverflow.com/help/how-to-ask).   
It's a brilliant guide by without a doubt the biggest Q&A website on the web.

# Where To Get Help?

There are two places you can go to with your scrapy related questions and issues:  

* [Stackoverflow][soscrapy].   
The issue with Stackoverflow is that it has a general rule of questions having to be generic, that means asking how to get price on this item on amazon is not a fit question. However the user base on `scrapy` tag seems to be quite understanding of this and tend to be quite lenient with reports and down-votes, but don't be surprised if your post gets down-voted or put on hold. All you can do is to try and make your issue more generic and hope for the best!

* IRC! @ irc.freenode.org #scrapy   
Good old IRC has been there for decades and even though it dropped in popularity quite significantly, it's still a great place to get help on any subject and scrapy is not an exception. 
Feel free to join the channel and ask questions about anything scrapy related; you can find me there too!

# Providing Information

To debug an issue and get the help you need you need to provide information about your problem:  

1. Source Code of your spider, settings.py and pipelines.py files.
2. Website you are crawling - sometimes people refrain from providing the url in fear of legal issues or some judgment. Don't worry about that, scraping is very much legal and no one will judge you, it might very well be the opposite - people might be more keen to help you scrape some weird porn website than amazon.  
3. Crawl Log (see [Producing Logs](#log)) - Scrapy logs majority of the events that happen in your spider, so to debug your spider the best resources are these logs.  
4. Spider Output (see [Producing Output](#output)) - This will rarely be useful for anyone else but yourself, but it can be very useful in some cases.  

Once you have these bits you can easily formulate your question and I'm sure someone will help you out!

## Producing Logs {#log}  

To save a log of your spider run you can use UNIX output redirection syntax:

    scrapy crawl myspider 2>&1 > mylog.log
    # or
    scrapy crawl myspider &> mylog.log

Explanation:  
    1. `scrapy crawl myspider` - is a scrapy command that will start crawling spider called `myspider`  
    2. `2>&1` - is UNIX syntax for redirecting error output to standard output. In UNIX there are types of outputs and in your log you want to have both of them in one file.  
    3. `> mylog.log` - is another UNIX output redirection, but this time we redirect the output to file called `mylog.log`
   
_Tip: points 2 and 3 can be summarized as `&>` in bash version 4 and up_

For logging scrapy uses python's built-in [`logging` module][logging] which by itself is pretty awesome! If you look into it, it might appear quite daunting but you can actually just `import logging` and simply log message to root logger: `logging.warning("this page has no next page")`. To have simple logging in your spider.

## Producing Output {#output}  

Scrapy can automatically produce output in one these formats:  

    'xml', 'jsonlines', 'jl', 'json', 'csv', 'pickle', 'marshal'

To do that simply run `crawl` command with `--output` flag (`-o` for short version) and provide a name + file ending of format you want as an argument:

    scrapy crawl myspider --output output.json

_This will output all items your spider spews out to `output.json` file._  

To get help for readability purposes you probably want to use either `json` or `xml` since those are most readable and as described in section below parsing-friendly formats.

_Tip: You can actually tell scrapy to produce output to stdout directly by setting output argument to `-`:_

    scrapy crawl myspider -t json -o - output.json

## Inspecting Output

There few tools to parse `json` or `xml` content, similar like you'd use `sed` or `grep` in unix. The most popular and widely known is probably [jq][jq], which I believe translates to json query.  
I personally really dislike that jq uses it's own mini-language as opposed to xpath or css selectors we all know, love and use daily.  
So in response to this I made [**PQ**][pq]! It uses xpath and css selectors as well as support both json and xml parsing.

To put it shortly, using the tools described above you can find specific values of some fields really easily.  
Lets imagine we have a bunch of products that have these fields: name and price. Now for some reason Samsung items have weird pricing and we want to find out whether that's the case every time we update the code. 

For example using pq we can navigate the prices of items that have some keywords in their names:

    cat output.json | pq "//item[contains(@name,'samsung')]/price/text()"

Will find all items that contain "samsung" in the name and output their price values. If you change up your spider an run this command again you can easily navigate whether the values are changing.

You can combine this with scrapy spider redirection to have everything in one line:

    scrapy crawl spider --nolog -t json -o - | pq "//item[contains(@name,'samsung')]/price/text()"



# Conclusion

Scrapy is a lovely framework and web-crawling is a tricky subjects with a lot of hidden issues, quirks and complexities. Because of it being rather big subjects and every spider having it's own challenges it might be difficult to find help. However I feel if you follow the steps and ideas described in this blog post you'll have a really good chance at getting some help either on stackoverflow or irc!

Do you have any places where you go to with your scrapy or web-crawling related questions? Did I miss something important? Leave the comment below :)

[jq]: https://stedolan.github.io/jq/
[pq]: https://github.com/granitosaurus/pq/
[soscrapy]: http://stackoverflow.com/questions/tagged/scrapy
[logging]: https://docs.python.org/3/library/logging.html
