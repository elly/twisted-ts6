#!/usr/bin/env python

class Server:
    def __init__(self, _sid, _name, _desc):
        self.sid = _sid
        self.name = _name
        self.desc = _desc
        self.caps = []

    def __str__(self):
        return '%s:%s' % (self.sid, self.name)
