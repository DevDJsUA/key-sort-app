from typing import Pattern
import KeyDetect
import os
from random import randint
from .modules.classes.movements import movements

from .modules.classes.track import Track
from .modules.classes.checkMixing import CheckMixing
from .modules.classes.createHarmonicMixingPattern import createHarmonicMixingPattern

from .modules.sorts.sortTracksUseCreateHardmonicMixingPatter import sortTracksUseCreateHarmonicMixingPattern
from .modules.sorts.initTracks import initTracks
from .modules.sorts.printTracks import printTracks
from .modules.sorts.hardcodeTracks import hardcodeTracks

dict = {'C Maj':'8B','C# Maj':'3B','D Maj':'10B','D# Maj':'5B','E Maj':'12B','F Maj':'7B','F# Maj':'2B','G Maj':'9B','G# Maj':'4B','A Maj':'11B','A# Maj':'6B','B Maj':'1B','c min':'5A','c# min':'12A','d min':'7A','d# min':'2A','e min':'9A','f min':'4A','f# min':'11A','g min':'6A','g# min':'1A','a min':'8A','a# min':'3A','b min':'10A'}





def sortTracks(tracks):
    return sortTracksUseCreateHarmonicMixingPattern(tracks)

def getSortTracks(directory):
    # tracks = initTracks(directory)
    tracks = hardcodeTracks()
    printTracks(tracks)
    [sortedTracks, unsortedTracks] = sortTracks(tracks)
    print("sorted:")
    printTracks(sortedTracks)
    
    print("unsorted:")
    printTracks(unsortedTracks)
    



# def testSort():
#     checkMixing.checkMix("10A", "10A")
#     checkMixing.checkMix("10A", "10B")
#     checkMixing.checkMix("10A", "9A")
#     checkMixing.checkMix("10A", "8A")
#     checkMixing.checkMix("10A", "7A")
#     checkMixing.checkMix("10A", "6A")


getSortTracks("./audio")

# testSort()


