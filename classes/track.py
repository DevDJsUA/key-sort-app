# -*- coding: utf-8 -*-
import os 
name = "track"

class Track:
    id = 0
    name = ""
    src = ""
    key = ""
    def __init__(self, _id, _name, _src, _key):
        self.id = _id
        self.name = _name
        self.src = _src,
        self.key = _key
