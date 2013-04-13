# coding=utf8

"""
404 plugin for golb - Output 404.html right under the root of your blog via template '404.html'

So, you need '404.html' in your templates.

"""

from golb import signals

def gen_page_404(runtime):
    print "Render 404.html.."
    render = runtime.render
    c = render('404.html')
    open('404.html', 'w').write(c.encode(runtime.charset))

def register():
    signals.runtime.connect(gen_page_404)
