# coding=utf8

"""
Plugin for golb:
    generate summary for each post. to get it in templates: {{post.summary}}
"""

from golb import signals
from golb.parser import markdown

def add_summary_to_post(runtime):
    posts = runtime.posts

    for post in posts:
        setattr(post, "summary", markdown.render(post.markdown[:255]))


def register():
    signals.runtime.connect(add_summary_to_post)
