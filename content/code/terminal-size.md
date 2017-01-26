Title: Getting Terminal Size In Python
Date: 2017-01-26
Tags: python, linux, guide
Slug: getting-terminal-size
Summary: Getting terminal size can be vital for your application, especially if you are doing some serious printing or drawing. There are some few tricks worth noting that I'd like to share.


Getting terminal size can be vital for your application, especially if you are doing some serious printing or drawing. There are some few tricks worth noting that I'd like to share.

The recommended way of retrieving terminal size for python3 is:

```python
import shutil
columns, rows = shutil.get_terminal_size(fallback=(80, 24))
```

And it works, for the most part.  

## The Issue

This particular function is just a high level wrapper around low level cpython function `os.get_terminal_size`. The only real thing it does is handle an exception and returns `fallback` values if that's the case.

However there's a huge pitfall with this function and it's that __it doesn't work with terminal pipes!__    
We can confirm that with this simple script:

```python
import sys
import shutil

columns, rows = shutil.get_terminal_size(fallback=(123, 456))
```

```bash
$ python size.py
cols:89
rows:22
$ python size.py | cat
cols:123
rows:456
```

89 to 22 is my actual size however when piping to anything, including python itself the size seems to fallback to the fallback values, which in most cases defeats the whole purpose of retrieving the terminal size.

### Making It Work!

If we use `os.get_terminal_size(0)` function, we'll get it to work!


```python
import sys
import os

columns, rows = os.get_terminal_size(0)
sys.stdout.write('cols:{}\nrows:{}\n'.format(columns, rows))
```

The thing to note here is the positional argument `0` in `os.get_terminal_size()` function, which tells which [file descriptor](https://en.wikipedia.org/wiki/File_descriptor) to use: 

>0 - Standard Input  
1 - Standard Output  
2 - Standard Error  

By default both `os` and `shutil` functions use `1`, which stands for Standard Output. This means that if we pipe and this output detaches itself we get an OsError:

```python
OSError: [Errno 25] Inappropriate ioctl for device
```

This default somewhat make sense if the size of your terminal changes when the output is displayed, but I'm having trouble even imagining an example where that would be the case.

If we were to run our script now, we'd get the results we are looking for

```bash
$ python size.py
cols:89
rows:22
$ python size.py | cat
cols:89
rows:22
# Even if we pipe multiple times!
$ python size.py | grep . | cat
cols:89
rows:22
```


## Conclusion  
I've spent more time than I'd like to admit trying to figure this out and the [stackoverflow thread](http://stackoverflow.com/a/41864359/3737009) for this subject only left me more confused.  
As always if you have any questions, critique or notices feel free to leave a comment!
