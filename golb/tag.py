#coding=utf8

class Tag(object):

    def __init__(self, name, posts=[]):
        self.name = name
        self.posts = posts

    def render(self):
        pass

