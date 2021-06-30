from typing import Pattern
import KeyDetect
import os
from random import randint
from classes.movements import movements

from classes.track import Track
from classes.checkMixing import CheckMixing
from classes.createHarmonicMixingPattern import createHarmonicMixingPattern

cr = createHarmonicMixingPattern()

def test():
    patterns = cr.createHarmonicMixingPattern(20) 
    _patt = []
    for i in movements:
        _patt.append(i.title())
    for i in range(len(patterns) - 1):
        print(_patt.index(patterns[i]))

test()