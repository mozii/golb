#coding=utf8

"""
Plugin for golb, add feed.atom.


"""
from golb import signals
from pyatom import AtomFeed

def gen_feed(runtime):
    print "Generate feed.atom.."
    posts = runtime.posts
    conf = runtime.conf
    charset = runtime.charset
    feed = AtomFeed(
        title=conf["blog"]["name"],
        subtitle=conf["blog"]["description"],
        feed_url=conf["blog"]["url"]+"/feed.atom",
        url=conf["blog"]["url"],
        author=conf["author"]["name"]
    )

    # gen the first 10 posts
    for post in posts[:10]:
        feed.add(
            title=post.title,
            content=post.html,
            content_type="html",
            author=conf["author"]["name"],
            url=conf["blog"]["url"]+"/"+post.out,
            updated=post.update_at
        )

    open("feed.atom", "w").write(feed.to_string().encode(charset))


def register():
    signals.runtime.connect(gen_feed)
