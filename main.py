from typing import Pattern
import KeyDetect
import os
from random import randint
from classes.movements import movements

from classes.track import Track
from classes.checkMixing import CheckMixing
from classes.createHarmonicMixingPattern import createHarmonicMixingPattern

cr = createHarmonicMixingPattern()



keys = []
tracks = []
dict = {'C Maj':'8B','C# Maj':'3B','D Maj':'10B','D# Maj':'5B','E Maj':'12B','F Maj':'7B','F# Maj':'2B','G Maj':'9B','G# Maj':'4B','A Maj':'11B','A# Maj':'6B','B Maj':'1B','c min':'5A','c# min':'12A','d min':'7A','d# min':'2A','e min':'9A','f min':'4A','f# min':'11A','g min':'6A','g# min':'1A','a min':'8A','a# min':'3A','b min':'10A'}

checkMixing = CheckMixing()

def initTracks(directory):
    files = os.listdir(directory)
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    
    tracks = []

    for i in range(len(files)):
        trackName = files[i]
        trackNames = trackName.split('.')
        

        format = trackNames[-1]
        if format == 'mp3' or format == 'wav':
            path = directory + '/' + trackName
            key = KeyDetect.keyDetect(path)
            keys.append(dict[key])
            _track = Track(i, trackName, path, dict[key])
            tracks.append(_track)

    return tracks

def printTracks(tracks):
    for track in tracks:
        for i in range(10):
            print("-", end=" ")
        print(f"\n{track.getId()}\n{track.getName()}\n{track.getSrc()}\n{track.getKey()}")
def hardcodeTracks():
    _track1 = Track(0,"track 0", "/track0", "10B")
    _track2 = Track(1,"track 1", "/track1", "10B")
    _track3 = Track(2,"track 2", "/track2", "9A")
    _track4 = Track(3,"track 3", "/track3", "4B")
    _track5 = Track(4,"track 4", "/track4", "10A")
    _track6 = Track(5,"track 5", "/track5", "1B")
    _track7 = Track(6,"track 6", "/track6", "7A")
    _track8 = Track(7,"track 7", "/track7", "8B")
    _track9 = Track(8,"track 8", "/track8", "12A")

    tracks = [_track1, _track2, _track3, _track4, _track5, _track6, _track7, _track8, _track9]
    return tracks

def sortTracks(tracks):
    allTracks = tracks
    oldTracks = tracks
    newTracks = []
    patterns = cr.createHarmonicMixingPattern(len(allTracks)) 

    newTracks.append(oldTracks[0])
    oldTracks.remove(oldTracks[0])

    i = 0
    no = 0
    while i < len(oldTracks) and no < 1000:
        if(len(oldTracks) == 0):
            print("shuyali?")
            return [newTracks, oldTracks]
        
        newTrack = oldTracks[i]
        _movements = []
        for j in movements:
            _movements.append(j.title())
        if checkMixing.checkMix(newTracks[-1].getKey(), newTrack.getKey(), _movements.index(patterns[i])) == True:
            newTracks.append(oldTracks[i])
            oldTracks.remove(oldTracks[i])
            i = 0
        else:
            no += 1


        i += 1
    return [newTracks, oldTracks]

def _sortTracks(tracks):
    allTracks = tracks
    oldTracks = tracks
    newTracks = []
    patterns = cr.createHarmonicMixingPattern(len(allTracks)) 

    newTracks.append(oldTracks[0])
    oldTracks.remove(oldTracks[0])

    no = 0
    i = 0
    while len(oldTracks) > 0 and no < 500:
        if(len(oldTracks) == 1):
            i = 0
        if(len(oldTracks) == 0):
            print("shuyali?")
            return
        
        
        
        newTrack = oldTracks[i]
        _movements = []
        for j in movements:
            _movements.append(j.title())
        # print(checkMixing.checkMix(newTracks[-1].getKey()))
        # print( newTrack.getKey() )
        if checkMixing.checkMix(newTracks[-1].getKey(), newTrack.getKey(), _movements.index(patterns[i])) == True:
            newTracks.append(oldTracks[i])
            oldTracks.remove(oldTracks[i])
        else:
            print('no')
            no += 1
        i += 1
        if(i >= len(oldTracks)):
            i = 0
        
    return [newTracks, oldTracks]

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
'''

1A: A Flat Minor Abm / G#m / G#
1B: B Major B

2A: E Flat Minor Ebm / D#m / D#
2B: F Sharp Major F# / Gb

3A: B Flat Minor Bbm / A#m / A#
3B: D Flat Major Db

4A: F Minor Fm
4B: A Flat Major Ab

5A: C Minor Cm
5B: E Flat Major Eb

6A: G Minor Gm
6B: B Flat Major Bb

7A: D Minor Dm
7B: F Major F

8A: A Minor Am
8B: C Major C

9A: E Minor Em
9B: G Major G

10A: B Minor Bm
10B: D Major D

11A: F Sharp Minor F#m / Gbm
11B: A Major A

12A: D Flat Minor Dbm / C#m / C#
12B: E Major E



engKey = ['C Maj', 'C# Maj', 'D Maj', 'D# Maj', 'E Maj', 'F Maj', 'F# Maj', 'G Maj', 'G# Maj', 'A Maj', 'A# Maj', 'B Maj','c min', 'c# min', 'd min', 'd# min', 'e min', 'f min', 'f# min', 'g min', 'g# min', 'a min', 'a# min', 'b min']

altKey = ['8B', '3B','10B','5B','12B','7B','2B','9B','4B','11B','6B','1B','5A','12A','7A','2A','9A','4A','11A','6A', '1A', '8A', '3A', '10A' ]
'''



