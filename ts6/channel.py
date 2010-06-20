#!/usr/bin/env python

class Channel:
    def __init__(self, name, modes, ts):
        self.name = name
        self.modes = modes
        self.topic = ''
        self.clients = []
        self.ts = ts

    def joined(self, client):
        self.clients.append(client)
        for c in self.clients:
            if c.conn:
                if c == client:
                    c.joined(self)
                else:
                    c.userJoined(client, self)

    def left(self, client, message):
        for c in self.clients:
            if c.conn:
                if c == client:
                    c.left(self)
                else:
                    c.userLeft(client, self, message)
        self.clients.remove(client)

    def modeset(self, src, modes):
        print '%s modes %s' % (self, modes)

    def tschange(self, newts, modes):
        print '%s ts change %d %s' % (self, newts, modes)

    def __str__(self):
        return self.name

    def privmsg(self, source, dest, message):
        """ distribute messages to local clients """
        for  c in self.clients:
            if c.conn:
                if c != source:
                    c.privmsg(source, dest, message)
