Status: Draft
Title: Stackoverflow [scrapy] Experience: The Good.
Date: 2016-09-14
Tags: scrapy, python, stackoverflow, good
Slug: scrapy-stackoverflow-good
Summary: The good bits of my experience with stackoverflow scrapy tag


After spending over a month answering [`scrapy`](https://github.com/scrapy/scrapy) related questions I've decided to share my experience. I'll point out few things that I've learned from this little experiment and few other related comments. This part will focus on the good bits of the experience!

#The Good
There are surprisingly **a lot of questions** with this scrapy tag on stackoverflow.

![scrapy stackoverflow stats 2016-09-14]({filename}/images/scrapy_stackoverflow1.png)

First things you notice in this picture is that the percentage of "unanswered" is quite high for recent questions. Even though that seems to be quite normal for stackoverflow it is still slightly higher than other related tags (e.g. python tag has 44% in the last 30 days right now). Huge issue here being that a lot of questions are actually answered in the comments so this statistic combined with bunch of things from "The Bad" section makes this heavily inflated, to the point where **I could comfortably say that majority of half-decent questions get answered**.  

This brings me back to first point: there are **a lot of new scrapy users** and majority of them are either new or intermediate python programmers. This is to be expected since web-scraping in general is on the rise, is quite easy to get into and most importantly - starting up any project when you can generate a bunch of data with script or two is extremely appealing to beginners and veterans alike.  

Last and probably the most important personal note is that **people who ask questions are generally pleasant** - willing to learn, change and work to resolve the issue. Which in turn is a good and a bad thing, helping people like this feels great but it consumes lots of time since it's so much harder to resist going the extra mile to explain something.

## Stacked Yet Diverse
Before I've started out I haven't noticed, but [scrapy] stackoverflow tag is already stacked with a bunch of scrapy devs and guys from Scrapinghub answering questions. So you really shouldn't shy away from asking difficult questions.

And yet **very diverse**:  
If you take a look at this last 30 days chart, you can see that there are just bunch of people helping out each other:

```python
$ scrapy shell "https://stackoverflow.com/tags/scrapy/topusers"
answers = response.xpath("//h2[contains(text(),'30 Days')]/following-sibling::table//tr/td[2]//a/text()").extract()
answers = [float(a) for a in answers]
import statistics  # python3
In []: statistics.mean(answers)
Out[]: 2.775
In []: statistics.median(answers)
Out[]: 1.0
```
That puts answers mean at 2.775 and median at 1.0. Of course the data provided by the topusers page is very limited and at best gives us a good hint on what's going on.
