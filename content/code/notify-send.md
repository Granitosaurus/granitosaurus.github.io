Status: draft
Title: Using python to setup desktop notifications.
Date: 2016-11-03 10:20
Tags: python, linux, guide
Slug: notify-send
Summary: Notify-send is great, you should use it!

Have you ever wondered how could you incorporate notification pop ups you might see thrown by your operating system in your application? Well worry no more, because this is the subject of this blog.   
Linux has some very powerful notification tools that if incorporated into your daily workflow can make things so much more convenient, easy and fun!  

In this blog I'll tell you more about some inner workings of notifications and how to set up a small app in python that can send such notifications.

# Notifications On Linux

Most gnu/linux systems use `libnotify` package for notifications - this package provides simple `notify-send` command line interface for sending notifications to your desktop environment or directly to your xorg display.  
To use it however, you need a running daemon program that would handle all of this; my personal recommendation is a great, robust daemon called `dunst`. You can find more info about this and alternatives to `dunst` in this arch-wiki [article][notifyaw].

See [Bonus: Set Up Notification] section of the blog for more info how to set it up.


# Python and Notifications.

Python is a perfect language for making such notification applications!  
By default python comes with everything we need to set this up, however to make things nicer lets use `click` command line interface package. It will greatly simplify the CLI part of the program.   
You can get it from pip via `pip install click` and skim through the [tutorial here][click] to get a quick gist of what it does.

To display a notification on your desktop using python all you need is to call `notify-send` via `subprocess` module like so:

    subprocess.call(['notify-send', 'title', 'body'])
    
This will start a process in your terminal that will tell notification daemon to show a notification with supplied title and a body.

# Simple Notification App

Now that we know how to send notification, we can use this to make a real application.

Combined that with a bit of web-scraping we can create cool little apps that will send this notification when something happens on the web.  
For this example let's do hackernews - notification when a new post containing some keywords is being posted.

For this we'll need few python dependencies:  
`click` - an easier way to generate command line interface.  
`requests` - an easier way to get data via http.  
`parsel` - a way to parse the html for the data we need.  
All of these are somewhat optional and could be replaced with python's inbuilt tools but these packages are just plain better.






### Bonus: Setup Notifications

By default majority of gnu/linux distributions already have everything covered for you! `libnotify` should be installed and some sort of notification daemon should be running in the background.  
Try writing this in your terminal:

    notify-send "test title" "test body"

If you see something, then great - you're done with this step!  

Otherwise you're probably missing a notification daemon. To fix that you need to install one. I recommend and will use [dunst][dunst] in this example.  
You can simply pull it from you package manager, e.g.:

    sudo pacman -S dunst  # for arch
    sudo apt install dunst  # for ubuntu

Usually `dunst` autostarts on majority of system on boot up as DBus autostarts it by default, but some systems might require explicit autostart, so in your init file just call `dunst`, e.g. for i3wm you'd add `exec dunst`.  

![dunst solarized]({filename}/images/dunst.png)
You can also customize your dunst quite extensively as well. All you need to do is pass the location of the config file as `--conf` parameter, i.e. `dunst --config ~/.dunstrc`.  
I'm running solarized look and you can find my config [on my dotfiles repo here][dunstrc]

My favorite thing about this particular notification daemon is the fact it's keyboard driven which means you can do cool stuff like:

    # Close notifactions
    close = ctrl+space
    close_all = ctrl+shift+space
    # Show history of notifications
    history = ctrl+grave
    # Open context of the notification
    # e.g. if notification has an url - open it in default browser
    context = ctrl+shift+period

It's really lovely, convenient, customizable and robust, so give it a shot.



[notifyaw]: https://wiki.archlinux.org/index.php/Desktop_notifications#Standalone
[dunst]: http://knopwob.org/dunst/index.html
[dunstrc]: https://github.com/Granitosaurus/.dotfiles/.dunstrc
[click]: http://click.pocoo.org/
