# coding=utf8

"""
plugin for golb.

To use:
    1. in conf.toml:
    [blog]
    plugins = [..., "gravatar"]  # add gravatar to plugins
    2. in templates:
    {{author.gravatar_id}}
"""


from golb import signals

from hashlib import md5


def add_gravatar_id(runtime):
    # add item gravatar_id to conf["author"]
    conf = runtime.conf
    m = md5()
    m.update(conf["author"]["email"])
    conf["author"]["gravatar_id"] = m.hexdigest()


def register():
    signals.runtime.connect(add_gravatar_id)
