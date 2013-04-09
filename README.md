golb
----

Not `gold` neither `glob`, `golb == reverse(blog)`

Markdown&TOML based static blog for programmers with simple templates and plugin support.

Install
-------

    pip install git+git://github.com/hit9/golb.git

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
  name = "Follow My Heart"
  description = "Make difference"
  templates = "classic"
  url = "http://example.com"
  plugins = ["gravatar", "feed", "post_summary"]
  [author]
  name = "hit9"
  email = "nz2324@126.com"
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

5. Generate htmls

  ```
  golb -l
  python -m SimpleHTTPServer 5000
  ```
  see results in browser: http://localhost:5000

Templates
---------

* classic https://github.com/hit9/golb-templates-classic

### How to modify the templates to meet my needs?

* fork the old repo

* Check out classic templates to learn how to and then modify templates.

* push to your forked repo. 

* Add your forked repo as a submodule in your blog's repo.

Plugins
--------

* feed - Generate feed.atom with the latest 10 posts.

* post_summary - Add attribute `summary` to each post(Html rendered from first 255 character of markdown.)

  To touch it in templaes:`{{post.summary}}`

* gavatar - Add attribute: gavatar_id  to author

  To touch it in templates:

  ```html
  <img src="https://secure.gravatar.com/avatar/{{author.gravatar_id}}?s=200"/>
  ```

DEMO
----

* https://github.com/hit9/hit9.github.com


Develop
-------

1. plugin develop, checkout [golb/plugins](golb/plugins). golb use `blinker` to implement plugins. One plugin needs a method called `register` to connect to `runtime` signal.

2. templates develop, checkout [classic](https://github.com/hit9/golb-templates-classic).


License
-------

MIT
