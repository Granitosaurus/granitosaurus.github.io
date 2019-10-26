Title: Get Organized With TaskWarrior!
Date: 2019-10-26
Tags: productivity, linux
Slug: taskwarrior-intro
Summary: Quick introduction how to get productive and organized with amazing commandline tool called Taskwarrior!

If you've been part of terminal ecosystem for you're most likely familiar with numerous terminal _todo_ sort of programs. I'd like to introduce you to king of all of them [Taskwarrior][taskwarrior].   
The name might sound intimidating but don't go - it's quite the opposite: it's butter smooth!  

# Intro

Your key command here is `task`. Typing this alone will list your open tasks:

    $ task 

    ID Age  Description                    Urg 
    1 32s   write a blog about taskwarrior    1
    2 11s   make carrot cake                  1
    3 2s    pay electric bills                1

Then the rest of cli goes as intuitive as it follows, these are your 3 vital beginner commands:

* `add "some task"` - to add a task.
* `done <id>` - to close task.
* `modify <id>` - change something about task.
    
Finally Taskwarrior has one vital important feature for managing your tasks - __tags__. You simply specify tags with `+` signs in front of your commands:

    $ task +work add "fix linkedin.com crawler"
    $ task +work 
    ID Age  Description                    Urg 
    1  2s   fix linkedin.com crawler        1

You can see already with these 4 little things: add, list, modify, tags - you have great powers. Time for example workflow!

# Example Workflow

This is a simple version of my taskwarrior workflow; First add tasks the moment you get them and try to split them up into small tasks - you're not an idiot you won't get confused don't worry:

```shell
$ task add +work "fix project1"
Created task 1.

$ task add +work "msg admin about project1 dump"
Created task 2.

$ task add +shop "potatoes - for potato cannon"
Created task 3.

$ task add +me "1 chapter of new book"
Created task 4.

$ task add +me "wash dishes"
Created task 5.

$ task add +gf "research christmas present on etsy"
Created task 6.

$ task add +me "practice bass a bit"
Created task 7.

$ task
ID Age  Tag  Description                        Urg 
1 7min work fix project1                        0.8
2 6min work msg admin about project1 dump       0.8
3 6min shop potatoes - for potato cannon        0.8
4 5min me   1 chapter of new book               0.8
5 5min me   wash dishes                         0.8
6 4min gf   research christmas present on etsy  0.8
7 4min me   practice bass a bit                 0.8 
```

Right, got bunch of tasks and now just pop them as you feel like. Having a weekday work day? 

    $ task +work
    ID Age   Tag  Description                   Urg 
    1 11min work fix project1                   0.8
    2 10min work msg admin about project1 dump  0.8
 
Task 1 really needs to get done: 

    $ task start 1
    Starting task 1 'fix project1'.
    Started 1 task.

_All this does is mark the task in your list that it's "ongoing"_ :
    
    $ task +work
    ID Active Age   Tag  Description                   Urg 
     1 1min   14min work fix project1                   4.8
     2        13min work msg admin about project1 dump  0.8  
     
 Been working hard for an hour or so, time for a short break. Lets keep the task active so we could jump right back in after our break and take a look at `me` tasks we have for our break:
    
    $ task +me 
    ID Age   Tag Description           Urg 
     4 14min me  1 chapter of new book  0.8    
     5 14min me  wash dishes            0.8
     7 12min me  practice bass a bit    0.8
     
Great time to boot up the bass for a song or two and while _Rocksmith on ps4_ is booting up - wash the dishes:

    $ task 5 done
    Completed task 5 'wash dishes'.
    Completed 1 task.
    
Break over, simply jump back to work, the task you've been working on is still glowing red there waiting for you ;)

# Get Micro Motivated!

Taskwarrior allows this sort of dead-simple micro-motivation. It's so simple an intuitive that in never feels like _additional_ work.

Often it's easy to go through your day without having tangible experience of your accomplishments. No matter how small your tasks are - the day feels so much better when you can visualize and feel the tiny hills you've conquered!

# Further Reading

Taskwarrior also packs a bunch of awesome, rich features but those are beyond the scope of this blog post.  
Taskwarrior documentation is well written and quite short:

    * intro: https://taskwarrior.org/docs/introduction.html
    * 30 second tutorial: https://taskwarrior.org/docs/30second.html
    * example workflows of users: https://taskwarrior.org/docs/workflow.html
    * `man task`


[taskwarrior]: https://taskwarrior.org/
