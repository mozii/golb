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

    posts = [Post(fn) for fn in ls(Post.sdir) if fn.endswith(se)]

    for post in posts:
        c = open(post.srcp).read().decode(charset)
        print parse(c)
