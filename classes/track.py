# -*- coding: utf-8 -*-
import os 
name = "track"

class Track:
    def __init__(self, id, name, src, key):
        self._id = id
        self._name = name
        self._src = src
        self._key = key
    
    def getId(self):
        return self._id
    def getName(self):
        return self._name
    def getSrc(self):
        return self._src
    def getKey(self):
        return self._key
