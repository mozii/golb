#coding=utf8
# blog instance
from ._ import name
from ._ import description
from ._ import author


from ._ import src as s
from ._ import output as o
from ._ import srcExt as se
from ._ import outputExt as oe
from ._ import postDir as postd
from ._ import tagDir as tagd
from os.path import join as j


class Blog(object):

    name = name
    description = description
    author = author


class Post(object):

    sdir = j(s, postd)  # source dir
    odir = j(o, postd) # output dir

    def __init__(self, name):
        self.name = name
        self.srcp =  j(Post.sdir, name + se) # source path
        self.outp = j(Post.odir, name + oe)  # output path


class Tag(object):

    sdir = j(s, tagd)
    odir = j(o, tagd)

    def __init__(self, name, posts=list()):
        self.name = name
        self.posts = posts


class Page(object):

    def __init__(self, number):
        self.number = number
