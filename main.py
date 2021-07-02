from typing import Pattern
import os

from random import randint
import modules.classes.movements

from modules.classes.track import Track
from modules.classes.checkMixing import CheckMixing
from modules.classes.createHarmonicMixingPattern import createHarmonicMixingPattern

from modules.sorts.sortTracksUseCreateHardmonicMixingPatter import sortTracksUseCreateHarmonicMixingPattern
from modules.sorts.sortTracksByRandom import sortTracksByRandom
from modules.sorts.initTracks import initTracks
from modules.sorts.printTracks import printTracks
from modules.sorts.hardcodeTracks import hardcodeTracks





def sortTracks(tracks):
    return sortTracksByRandom(tracks)

def getSortTracks(directory):
    tracks = initTracks(directory)
    # tracks = hardcodeTracks()
    printTracks(tracks)
    [sortedTracks, unsortedTracks] = sortTracks(tracks)

    return sortedTracks
    # print("sorted:")
    # printTracks(sortedTracks)
    
    # print("unsorted:")
    # printTracks(unsortedTracks)
    



# def testSort():
#     checkMixing.checkMix("10A", "10A")
#     checkMixing.checkMix("10A", "10B")
#     checkMixing.checkMix("10A", "9A")
#     checkMixing.checkMix("10A", "8A")
#     checkMixing.checkMix("10A", "7A")
#     checkMixing.checkMix("10A", "6A")


# getSortTracks("./audio")

# testSort()


