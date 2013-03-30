# coding=utf8

from .blog import Tag
from .blog import Post
from .blog import Page
from .blog import Blog

from ._ import charset
from ._ import srcExt as se

from .parser import parse
from .renderer import render

from os.path import join as j
from os import listdir as ls

def build():

    sel = len(se) # source extension len
    posts = [Post(f[:-sel]) for f in ls(Post.sdir) if f.endswith(se)]

    for post in posts:
        c = open(post.srcp).read().decode(charset)
        print parse(c)
