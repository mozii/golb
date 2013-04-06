import toml
from ._ import conf_fn
from ._ import charset
from ._ import srcExt as se
from ._ import default_conf as conf
from .blog import Tag
from .blog import Post
from .blog import Page
from .blog import tags as _tags  # make alias
from .blog import feed as _feed
from .blog import about
from .blog import index
from .blog import archives
from .parser import parse
from os.path import exists
from os.path import join as j
from os import listdir as ls
from os import makedirs as mkdir
from os.path import exists
from pyatom import AtomFeed
from jinja2 import Environment, FileSystemLoader


# jinja2 environment

env = None

def init_jinja():
    global env
    loader = FileSystemLoader(conf["blog"]["templates"])
    env = Environment(loader=loader)
    env.trim_blocks = True


def render(template, **dct):
    """
    render template
    """
    dct.update(conf)
    return env.get_template(template).render(**dct)


def get_conf():
    """
    read config from conf.toml and update the default
    """
    # if user conf exists, update the conf
    if exists(conf_fn):
        dct = toml.loads(open(conf_fn).read().decode(charset))
        conf.update(dct)
    return conf


def chunks(l, n):
    # split list into equal parts
    # chunks(range(1, 9), 3) => (1, 2, 3), (4, 5, 6), (7, 8)
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def get_posts():
    posts = [Post(fn) for fn in ls(Post.src_dir) if fn.endswith(se)]
    # parse posts and update posts' attr
    for post in posts:
        c = open(post.src).read().decode(charset)
        dct = parse(c)

        dct.setdefault("tags", [])
        dct.setdefault("title", "Untitled")

        # update post's attrs with parsed content
        post.__dict__.update(dct)
        # cast
        post.tags = set(post.tags)
    return posts


def get_tags(posts):

    tagdct = dict()

    for post in posts:
        for tag in post.tags:
            tagdct.setdefault(tag, []).append(post)

    # init tags
    tags = list()
    for tag, tag_posts in tagdct.items():
        tags.append(Tag(tag, tag_posts))
    return tags


def sort_posts(posts):
    posts.sort(key=lambda p: p.update_at.timetuple(), reverse=True)
    return posts


def sort_tags(tags):
    tags.sort(key=lambda x: len(x.posts), reverse=True)
    return tags


def get_pages(posts):
    # default, 10
    x = chunks(posts, 10)
    pages = [Page(number=i + 1, posts=list(k)) for i, k in enumerate(x)]
    pages[0].first = True
    pages[-1].last = True
    return pages


def render_posts(posts):
    if not exists(Post.out_dir):
        mkdir(Post.out_dir)
    for post in posts:
        r = render(Post.template, post=post)
        open(post.out, "w").write(r.encode(charset))


def render_tags(tags):
    if not exists(Tag.out_dir):
        mkdir(Tag.out_dir)
    for tag in tags:
        r = render(Tag.template, tag=tag)
        open(tag.out, "w").write(r.encode(charset))
    r = render(_tags.template, tags=tags)
    open(_tags.out, "w").write(r.encode(charset))


def render_pages(pages):
    if not exists(Page.out_dir):
        mkdir(Page.out_dir)
    for page in pages:
        r = render(Page.template, page=page)
        if page.first:
            open(index.out, "w").write(r.encode(charset))
        else:
            open(page.out, "w").write(r.encode(charset))


def render_archives(posts):
    r = render(archives.template, posts=posts)
    open(archives.out, "w").write(r.encode(charset))


def render_about():
    if exists(about.src):
        c = open(about.src).read().decode(charset)
        dct = parse(c)
    else:
        dct = {}
    about.__dict__.update(dct)
    r = render(about.template, about=about)
    open(about.out, "w").write(r.encode(charset))


def gen_feed(posts):
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

    open(_feed.out, "w").write(feed.to_string().encode(charset))


def main():
    print "Read conf.toml.."
    conf = get_conf()
    print "Init jinja environment.."
    init_jinja()
    print "Read and parse posts.."
    posts = get_posts()
    print "Sort posts by updated time.."
    posts = sort_posts(posts)
    print "Extract tags from posts.."
    tags = get_tags(posts)
    print "Sort tags by posts number.."
    tags = sort_tags(tags)
    print "Generate pages from posts.."
    pages = get_pages(posts)
    print "Render posts.."
    render_posts(posts)
    print "Render tags.."
    render_tags(tags)
    print "Render pages.."
    render_pages(pages)
    print "Render archives.."
    render_archives(posts)
    print "Render about page.."
    render_about()
    print "Generate feed to feed.atom.."
    gen_feed(posts)
    print "Build complete."
