from setuptools import setup

setup(
    name='golb',
    version="0.1.3",
    author='hit9',
    author_email='nz2324@126.com',
    description='minimal static blog generator for programmers. write posts in markdown and toml,\
    render templates with jinja2',
    license='MIT',
    keywords='static blog generator, markdown, toml, posts',
    url='http://github.com/hit9/golb',
    long_description=open('README.md').read(),
    packages=['golb'],
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'golb = golb.script:main'
        ]
    },
    install_requires = open("requirements.pip").read().splitlines()
)
