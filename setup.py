from setuptools import setup
from golb import __version__

setup(
    name='golb',
    version=__version__,
    author='hit9',
    author_email='nz2324@126.com',
    description='minimal static blog generator for coders. write posts in markdown and toml,\
    render templates with jinja2',
    license='BSD',
    keywords='static blog generator, markdown, posts',
    url='http://github.com/hit9/golb',
    long_description=open('Readme.md').read(),
    packages=['golb'],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'golb = golb.golb:main'
        ]
    },
    install_requires = open("requirements.pip").read().splitlines()
)
