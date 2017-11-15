Title: wisdom.cat
Date: 2017-04-01
Tags: python, linux, flask, webdev
Slug: wisdom-cat
Summary: Recently I made small website in flask for aggregating educational youtube videos and I'd like to share my experience.

I've always wanted to make a webapp and flask always looked appealing but deployment and production hassle really turned me off. A week ago I tried to force myself through it and I have to say, it's really not that bad!

_This is not a guide and you most likely won't learn anything - it's more of a condense story of how wisdom.cat was developed and doesn't really serve any other purpose_

![wisdom.cat](https://i.imgur.com/JppvDUZ.png)

## Wisdom.cat   
> $ cat wisdom  
> =( ^ >w< ^ )=   
> wisdom.cat - is a video aggregator website that aggregates bite size videos   
> which are in some way educational. The intention of this website is  
> to have something beneficial to watch during short down-time periods;   
> https://github.com/Granitosaurus/wisdom.cat  

I work remotely and I tend to eat at home so I usually watch a video or two during my lunch break. However I wanted to make sure I don't completely waste this time and don't let my brain fall a sleep or lose track so I've been watching education videos to compensate.  
So the goal of [wisdom.cat](http://wisdom.cat) is to solve this issue and provide me and others who are stuck in a similar position something to watch.  


### Alternatives and Inspirations

![looking around](https://i.redd.it/1h2rkgvxzv6y.gif)  

For quite a while a brilliant website (that wisdom.cat is more or less a clone of) performed this function - it's called http://unplugthetv.com. However as time went on the feed slowed down to the point where it has been completely dead since October of 2016.  
I didn't like few things on that website; first that the feed was fairly slow and the second, much more important one, that there was no way to customize it. So a lot of unwanted things ended up in the feed, my personal example being the  TED channel, it used to be brilliant - 4 years ago, now it's utter garbage that if anything makes people more dumb instead of educating them.

So in hindsight you could say wisdom cat was born from a dead cool website and my hatred for TED (TED-ED is really lovely though!).

Some alternatives I came across while doing my research that are worth mentioning:  
http://reddit.com/r/mealtimevideos - similar purpose, however it's not focused on education.  
Curiousity app - I've never used it but heard one person on irc.#flask say that wisdom.cat is similar.  

## Databases  
![wisdomcat database story]({filename}/images/wisdomcat-db.png)  

I didn't know much about designing webapp data storage at the time and just went with sqlite3, which didn't play well with pythonanywhere hosting that I was trying to use at the time. So I made a switch to mysql, which was a miserable  mistake. Mysql is dreadful to work with and I've spent more time working on the database and such than on the web app itself.   
Frankly it was extremely unenjoyable experience and since this project was my spare time thing I came to a brilliant conclusion to try something different.   

I got Redis! And honestly, it's been a complete pleasure starting the very moment I ran `pacman -S redis`.  
So what's so great about it? Well it might sound clichè but It Just Works™, no really after I installed it via pacman, started the daemon via systemctl and got a python api (python-redis or flask-redis) I had to add pretty much 2 lines to my youtube scraper to store the data and 4 lines to my flask views to display it - it was liberating!  

One important thing I learned when it comes to Redis is to "store data the same way you will query it". Since redis doesn't really have a full query mechanism behind it, you might end up stuck without being able to get your data without a bunch of python code to help you out.  
My first attempt was to write every video to `video_<id>` but since I wanted wisdom.cat to have filters for channels that didn't end up being as efficient. Nowhere near of being a huge performance hit but in short time it might become noticeable.  
Then I just wrote video data to Redis lists named after channels, i.e. "channel_CGP Grey" will contain a list of videos, that can be updated and modified - which solved this non-issue completely!  

## Flask  

Flask was an easy choice for wisdom.cat; it was popular(read a lot of learning resources), light-weight and in python!  
I'm not sure if I have much to add other than few struggles I had as a newb.  
The circular imports got me a time or two, because for some reason I decided to keep `app` object in `__init__.py` and ended up kinda liking it.  

The biggest issue I had was the sessions. Initially wisdom cat would generate video queue and channel subscriptions and put them to flask session, aka secure cookie. Now this brought an impossible to debug issue that made be dippy few times. Turns out the cookie/session ended up being so big it would not update anymore appropriately since cookie has 4k byte limit and the wisdom cat setup, at the time with 30 videos, was already reaching that!  
So needless to say it was a bad idea from the very get go, fortunately with redis up and running it was no longer an issue that would be difficult to solve.

All in all it's hard to say something original about Flask since it has such a huge community and so many opinions, research and information already that anything I'd say would be awfully redundant so I'll just say that Flask was a real pleasure to work with and honestly, I can't wait to start a new project already!  

## Deploying

This was my most dreaded bit. I've been playing with servers to run crawlers and some notification tools for some time but I've never exposed them to public or made them accessible.  
Fortunately it all sounds more complicated than it actually is. All you need is an application, [wsgi](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) tool, some daemons and an afternoon!  

I ended up renting a [linode](https://www.linode.com/?r=37112fcbb52a0f3c556a91b37d215d72e4ef5702) (which is really lovely!) and using arch node with systemd, nginx and gunicorn.   
I've been using arch and systemd for few years now so this part was a breeze, however nginx gave me a bit of trouble. Mostly because most of the tutorials, guides and documentation assumed that it's running on Ubuntu which for some reason uses unusual structure and stores servers in `sites-enabled` and `sites-available` which were not present in arch(or most of the other distros). Apparently this was to replicated some apache server structure so I decided to join the cool kid's club and replicate the same structure with `inludes` and system links - it worked out perfectly fine and I with few lines of configs it was working.

Finally I wrote up two daemon services: `gunicorn` wsgi service to launch and expose the app, and a timer service - to run video crawler every half an hour, to update the video feed.

And with that wisdom.cat was finally drawing it's first breaths! 


##Conclusion

This was a really fun little project and I highly recommend investing some time into learning how to make a simple web app like this - it opens up so many gates for so many opportunities!
