#coding=utf8

from .g import g
from .reader import readPost
from .writer import writePost
from ._ import PostTemplate

import os
import parser
import renderer


class Post(g):

    def __init__(self, name):
        self.name = name

    # parse this post'content and update its attr
    def parse(self):

        content = readPost(self.name)
        dct = parser.parse(content)
        # update post's attributes
        self.__dict__.update(dct)

    # render post with templates/post.html
    def render(self):
        # render template
        content = renderer.render(self, PostTemplate)
        # write
        writePost(self.name, content)
