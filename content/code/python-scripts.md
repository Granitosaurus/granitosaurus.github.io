Title: Guide: setup python scripting
Date: 2017-01-17
Tags: python, linux, guide
Slug: python-scripts 
Summary: Short guide on how to setup an environment for executable python scripts

Few python scripts can make your daily routines significantly easier and enjoyable. In this post I'll cover how to set up your linux environment to have your scripts always easily accessible.  
In other words, how to make this reality:

```
$ amicool 
Yes you are, keep it up!
```

To start off we need to create a directory where your scripts be located. A de facto standard is `~/bin`:

```
$ mkdir bin
```

## Handling the PATH

Now depending on your system and the shell you use, this directory might already be created or might not be in your `PATH` environment at all.  
`PATH` environment variable is a list of locations your shell will look for executable files - programs in other words. So if you're using good ol' bash simply adding this line to your `~/.bashrc` file will do:

```
export PATH="~/bin:$PATH"
```

## Creating the script 

Now we can create the script itself:

```
$ touch ~/bin/amicool 
```

Notice that we do not use `.py` extension, because linux takes executables in path literally and we don't want to type the extension whenever we call the script.  
We should populate this script with some actual code:

```
#!/usr/bin/env python3

if __name__ == '__main__':
    print("Yes you are, keep it up!")
```

Notice that we start of the file with `#!/usr/bin/env python3`. This is called shebang, it's basically a header that tells your operating system what to use to execute the file, in this case we want to use `python3`.  
Afterwards we have most simple of python code that just prints "hello world!" when called directly (that's what `__name__ == '__main__'` part stands for).

## Making it executable

Lastly we want to mark our file "executable" so the operating system know it can actually call this file as a script or a program:

```
chmod +x ~/bin/amicool
```

And there we go! Your script is good to go and whenever you feel inadequate regarding your coolness just type:

```
$ amicool
Yes you are, keep it up!
```


