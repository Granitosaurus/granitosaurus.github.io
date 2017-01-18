Title: My bin: center
Date: 2017-01-18
Tags: python, linux, guide
Slug: my-bin-center
Summary: Some of the useful things I have in my ~/bin

People are naturally lazy and strive to automate as much as possible. I'm no exception and my user scripts directory `~/bin` is full of scripts that make my life easier or at least makes me feel that way.  

Today I want to show you and explain some bits of a little python script for centering text. It's isn't particularly special, but it's a great base to show of how awesome and powerful python command line tools can be!  
It's a simple pipeable script that takes in some text, centers it according to your terminal size and outputs it to standard output.My use case for this is for reading poems and by default they are not centered properly. To add to that I also like to constantly resize my terminal window because I'm running [i3wm](http://i3wm.org/) - a tilling windows manager for linux, which forces every window to use up all of the space it can, which makes them very much dynamic and unpredictable.

In other words it turns something like:

```
$ cat raven.md
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore,
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
'Tis some visitor,' I muttered, 'tapping at my chamber door-
Only this, and nothing more.'
```

Into:

```
$ cat raven.md | center
             Once upon a midnight dreary, while I pondered, weak and weary,              
                Over many a quaint and curious volume of forgotten lore,                 
             While I nodded, nearly napping, suddenly there came a tapping,              
               As of some one gently rapping, rapping at my chamber door.                
              'Tis some visitor,' I muttered, 'tapping at my chamber door-               
                              Only this, and nothing more.'   
```

While taking your current terminal size into account, so no matter what you're doing or where you are the text will nice and pretty.   

### Source 

Now lets take a look at the source code:

```Python
    #!/usr/bin/env python3
    import click
    import sys
    import shutil


    @click.command()
    @click.argument('input', required=False, type=click.File('r'))
    @click.argument('output', required=False, type=click.File('w'))
    @click.option('-l', '--length', help='maximum line length [default:current terminal size]', type=click.INT)
    def cli(input, output, length):
        """Simple, pipeable tool for centering text"""
        columns = shutil.get_terminal_size()[0]  #1
        source = input.readlines() if input else sys.stdin  #2
        _format = '{{:^{}}}\n'.format(length or int(columns))  #3
        for line in source:  #4
            text = _format.format(line.strip())
            if output:
                output.write(text)
            else:
                sys.stdout.write(text)

    if __name__ == "__main__":
        cli()
```

### Explanation

I love `click` library, which is a tool for creating command line interface. It's beautiful, easy and saves so much space and time. So we start off with two positional arguments for input and output filenames, these are not necessary for pipe logic we need but is a nice addition if there's a need for standalone function.  
Next we have custom option for length which allows overriding maximum line length. In case you have a very huge terminal window and you just want a nice margin instead of the text being at the very center of your screen.
Finally there's the program itself:  
`#1` - We retrieve dimensions of the current terminal window. This returns a tuple of `(columns, rows)` since we only care about columns we take the first member.  
`#2` - We decide on which source to use for input, if first position argument is supplied to script, we'll use that as a source, otherwise use standard input.  
`#3` - This might appear complicated but what we are doing here is creating a format that we will use to format every line of our text. The line evaluates to `{:^<terminal_size>}\n` now if we call `.format()` on that we can insert text and it will be centered. For more check out [python's string formatting](https://docs.python.org/3.1/library/string.html#string-formatting), it's awesome!  
`#4` - And lastly we have the loop itself. Here we loop through every line, center it and either write it to file if the second positional argument is supplied or put it straight to standard output.  

### Improvements

You could probably go wild with bunch of flags and modifications but it's important to remember to KISS - keep it simple stupid. With pipes, aliases and various other shortcuts leaving this script to do one job is very much a good idea! :) 

### Pitfalls

One of the pitfalls I've experience with piping in python scripts is when piping to `less` or similar tools.   
Because of how `shutils.get_terminal_size()` works, if a parameter `fallback` is set, like: `shutils.get_terminal_size(fallback=(80,30))` the set fallback will actually be used instead of your terminal size if piped to `less` or similar tool.  
I'm not certain why it behaves like that, my guess being is that `less` breaks the terminal size function, but opposed to general recommendations of setting a fallback it's best to not set it in this case.


### Conclusion 

I'd like to encourage anyone who use ugly awk scripts and aliases just write a short command line application with click, it takes no longer than 10 minutes, is beautiful, usable, readable and easily shareable. Let me know if you have any questions and stay tuned for more scripts and explanations!
