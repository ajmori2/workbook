# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:40:19 2015

@author: cheeren
"""

def traverse(t):
    try:
        t.label()
    except AttributeError:
        print t,
    else:
        # Now we know that t.node is defined
        print '(', t.label(),
        for child in t:
            traverse(child)
        print ')',
