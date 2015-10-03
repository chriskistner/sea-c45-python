#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, content='', name=''):
        self.name = name
        self.content = content
        self.children = []

    def append(self, child):
        self.children.append(child)

    def render(self, f):
        f.write("\n <{name}>".format(name=self.name))
        if self.children == []:
            f.write(self.content)
        else:
            for items in self.children:
                items.render(f)
        f.write("\n </{name}>".format(name=self.name))


class Html(Element):
    def __init__(self, content=''):
        Element.__init__(self, content='', name='html')


class Body(Element):
    def __init__(self, content=''):
        Element.__init__(self, content='', name='body')


class P(Element):
    def __init__(self, content=''):
        Element.__init__(self, content=content, name='p')
