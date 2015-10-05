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
        self.style = []


    def append(self, child, style):
        self.children.append(child)
        self.style.append(style)


    def render(self, f):
        f.write(" \n <{name} {style}>".format(name=self.name, style=self.style)
            if self.children == []:
                f.write(self.content)
            else
                for items in self.children:
                    items.render(f)
                    f.write("\n </{name}>".format(name=self.name))

class Html(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content='', name='html', style=style)

class Body(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content='', name='body', style=style)


class P(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content=content, name='p', style=style)


class Head(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content=content, name='head', style=style)


class Title(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content=content, name='title', style=style)
