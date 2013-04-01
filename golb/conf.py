# coding=utf8

import toml
from ._ import charset
from os.path import exists

conffn = "conf.toml"


# minimal & default configuration
conf = dict(
    blog=dict(
        name=u"HelloWorld!",
        description=u"Make difference",
        templates="templates",
        posts_per_page=12
    ),
    author=dict(
        name=u"you",
        email=u"you@some.com",
    )
)


if exists(conffn):
    dct = toml.loads(open(conffn).read().decode(charset))
    conf.update(dct)

# add md5 hash for author's email

from hashlib import md5

m = md5()
m.update(conf["author"]["email"])
conf["author"]["gravatar_id"] = m.hexdigest()
