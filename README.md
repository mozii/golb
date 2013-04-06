golb
----

Not `gold` neither `glob`, `golb == reverse(blog)`

Markdown&TOML based static blog for programmers with simple templates and plugin support.

Usage
-----

```
Usage:
  golb [--local]
  golb (-h | --help)
  golb (-v | --version)

Options:
  -h --help      show this message
  -v --version   show version
  -l --local     generate html with an empty blog url.
```

How-To-Start
-------------

To start bloging:

1. make your repo directory:

```
mkdir -p  myblog/src/post
cd myblog
git init
```

2. In the root of repo, touch `conf.toml` and edit:

```
[blog]
# blog's name
name = "Follow My Heart"
# blog's description
description = "Make difference"
# the directory of your templates(required!)
templates = "classic"
# url of the blog. ends without forward slash
url = "http://example.com"
# plugins on
plugins = ["gravatar", "feed", "post_summary"]
# blog's author
[author]
# your github username
name = "hit9"
email = "nz2324@126.com"
# other settings can be touched in template files in this way:
# keygroup.key
# i.e:
# [mysettings]
# somevar = true
# you can reach this setting in templates: mysettings.somevar
```

3. Add one set of templates as submodule,  i.e. use the `classic`

```
git submodule add git://github.com/hit9/golb-templates-classic.git classic
```

And then set `templates` in section `blog` to `classic`


4. start blog the first post:

```
touch src/post/HelloWorld.md
```

golb use toml+Markdown as post's source:

```
title = "Hello World!"
tags = ["tag1", "tag2"]  # tags
----

## Hello World!
```

Templates
---------

* classic https://github.com/hit9/golb-templates-classic


DEMO
----

* https://github.com/hit9/hit9.github.com

License
-------

MIT
