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
from os import makedirs as mkdir
from os.path import dirname, exists

def build():

    posts = [Post(fn) for fn in ls(Post.sdir) if fn.endswith(se)]
    tags = dict()  # tagname: posts


    # parse posts and update posts' attr
    for post in posts:
        c = open(post.srcp).read().decode(charset)
        dct = parse(c)

        dct.setdefault("tags", [])
        dct.setdefault("title", "Untitled")

        # update post's attrs with parsed content
        post.__dict__.update(dct)

    # init tags
    for post in posts:
        for tag in post.tags:
            tags.setdefault(tag, []).append(post)

    # render post
    # check output dir
    if not exists(Post.odir):
        mkdir(Post.odir)
    for post in posts:
        r = render(dct=dict(blog=Blog, post=post), template=Post.tpl)
        open(post.outp, "w").write(r.encode(charset))

    # render tags

