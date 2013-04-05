from .blog import Tag
from .blog import Post
from .blog import Page
from .blog import index
from .blog import archives
from .blog import about
from .blog import tags
from .blog import feed

from os import system

def clean():
    cmd = ["rm"]
    cmd.append(Tag.odir)
    cmd.append(Post.odir)
    cmd.append(Page.odir)
    cmd.append(index.outp)
    cmd.append(archives.outp)
    cmd.append(tags.outp)
    cmd.append(about.outp)
    cmd.append(feed.outp)
    cmd.append("-rf")
    cmdstr = " ".join(cmd)
    print cmdstr
    system(cmdstr)
