#coding=utf8
# blog instance
from ._ import name
from ._ import description
from ._ import author


class Post(object):

    def __init__(self, name):
        self.name = name


class Tag(object):

    def __init__(self, name, posts=list()):
        self.name = name
        self.posts = posts


class Page(object):

    def __init__(self, number):
        self.number = number
