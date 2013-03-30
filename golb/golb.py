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


def chunks(l, n):
    # split list into equal parts
    # chunks(range(1, 9), 3) => (1, 2, 3), (4, 5, 6), (7, 8)
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def build():

    posts = [Post(fn) for fn in ls(Post.sdir) if fn.endswith(se)]

    print "Read and parse posts.."

    # parse posts and update posts' attr
    for post in posts:
        c = open(post.srcp).read().decode(charset)
        dct = parse(c)

        dct.setdefault("tags", [])
        dct.setdefault("title", "Untitled")

        # update post's attrs with parsed content
        post.__dict__.update(dct)
        # cast
        post.tags = set(post.tags)

    # grab tags from posts
    print "Extract tags.."
    tagdct = dict()

    for post in posts:
        for tag in post.tags:
            tagdct.setdefault(tag, []).append(post)

    # init tags
    tags = list()
    for tag, ps in tagdct.items():
        tags.append(Tag(tag, ps))

    # sort pages
    print "Sort pages.."
    # sort posts by update time
    posts.sort(key=lambda p: p.update_at.timetuple(), reverse=True)
    # 12 posts per page
    x = chunks(posts, 3)
    pages = [Page(number=i + 1, posts=list(k)) for i, k in enumerate(x)]

    # render posts
    print "Render posts.."
    if not exists(Post.odir):
        mkdir(Post.odir)
    for post in posts:
        r = render(dct=dict(blog=Blog, post=post), template=Post.tpl)
        open(post.outp, "w").write(r.encode(charset))

    # render tags
    print "Render tags.."
    if not exists(Tag.odir):
        mkdir(Tag.odir)
    for tag in tags:
        r = render(dct=dict(blog=Blog, tag=tag), template=Tag.tpl)
        open(tag.outp, "w").write(r.encode(charset))

    # render pages
    print "Render pages.."
    if not exists(Page.odir):
        mkdir(Page.odir)
    for page in pages:
        r = render(dct=dict(blog=Blog, page=page), template=Page.tpl)
        open(page.outp, "w").write(r.encode(charset))

    print "Build complete"
