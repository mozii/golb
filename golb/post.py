#coding=utf8

from .reader import readPost
from .writer import writePost

import os
import parser
import renderer

tpl = "post.html"
dir = "post"

class Post(object):

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
        dct = dict(post=self)
        # render template
        content = renderer.render(dct, tpl)
        # write
        writePost(self.name, content)
