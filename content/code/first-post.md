Title: First post. Hello Pelican! 
Date: 2016-09-14
Tags: pelican, python, blog
Slug: installing-pelican
Summary: Starting up the blog with Python and Pelican static blog generator!

I've decided to start a blog after Python package called Pelican caught my eye.
### Installing Pelican
![Pelicans are cool]({filename}/images/pelican-bird.jpg)  
The setup for `Pelican` is pretty straightforward just run:
```bash
~> pip install pelican  # Installing Pelican package for python
~> mdir blog && cd blog  # Create and jump into your blog directory!
~/blog/> pelican-quickstart
	... #answer some simple questions here
~/blog/> vim content/first-page.md
	... #write your blog here in simple markdown
~/blog/> pelican content  # regenerate website
~/blog/> cd output
~/blog/output> python -m pelican.server  # run pelican server to test locally
```
Now connect to `http://localhost:8000` and there you go!  
You can check [here](http://docs.getpelican.com/en/latest/content.html#articles-and-pages) for how to template your message how to format your blog entry.
### Vim markdown highlight for .md files
While going through the installation I've noticed that markdown doesn't have highlighting in vim which was peculiar. I found [this post which describes a simple fix](http://superuser.com/questions/701496/no-syntax-highlight-on-md-files).  
Simply create directories and file: 
```
~/.vim/ftdetect/markdown.vim
``` 
with content: 
```
au BufNewFile,BufRead *.md  setf markdown
```

