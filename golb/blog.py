#coding=utf8
# blog instance
from ._ import name
from ._ import description
from ._ import author


from ._ import src as s
from ._ import output as o
from ._ import srcExt as se
from ._ import outputExt as oe
from os.path import join as j

sel = len(se)


class Blog(object):

    name = name
    description = description
    author = author


class Post(object):

    sdir = j(s, "post")  # source dir
    odir = j(o, "post") # output dir
    tpl = "post.html"

    def __init__(self, fn):  # init one Post object by filename
        name = fn[:-sel]
        self.name = name
        self.filename = fn
        self.srcp =  j(Post.sdir, name + se) # source path
        self.outp = j(Post.odir, name + oe)  # output path


class Tag(object):

    sdir = j(s, "tag")
    odir = j(o, "tag")

    def __init__(self, name, posts=list()):
        self.name = name
        self.posts = posts


class Page(object):

    def __init__(self, number):
        self.number = number
