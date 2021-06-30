import KeyDetect
import os
from classes.track import Track



keys = []
tracks = []
dict = {'C Maj':'8B','C# Maj':'3B','D Maj':'10B','D# Maj':'5B','E Maj':'12B','F Maj':'7B','F# Maj':'2B','G Maj':'9B','G# Maj':'4B','A Maj':'11B','A# Maj':'6B','B Maj':'1B','c min':'5A','c# min':'12A','d min':'7A','d# min':'2A','e min':'9A','f min':'4A','f# min':'11A','g min':'6A','g# min':'1A','a min':'8A','a# min':'3A','b min':'10A'}
class Movements:
    perfectMatch = 35  # perfectMatch (=)
    energyBoost = 10  # energyBoost (+1)
    energyDrop = 10  # energyDrop (-1)
    energySwitch= 10  # energySwitch (B/A)
    moodBoost = 5  # moodBoost (+3)
    moodDrop = 5  # moodDrop (-3)
    energyRaise = 5  # energyRaise (+7)
    domKey = 10  # domKey (+1 & B/A) = energyBoost & energySwitch
    subDomKey = 10  # subDomKey (-1 & B/A) = energyDrop & energySwitch
movements = Movements()

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
    _track2 = Track(1,"track 1", "/track1", "9B")
    _track3 = Track(2,"track 2", "/track2", "8A")
    _track4 = Track(3,"track 3", "/track3", "4B")
    _track5 = Track(4,"track 4", "/track4", "6A")
    _track6 = Track(5,"track 5", "/track5", "1B")
    _track7 = Track(6,"track 6", "/track6", "7A")
    _track8 = Track(7,"track 7", "/track7", "8B")
    _track9 = Track(8,"track 8", "/track8", "12A")

    tracks = [_track1, _track2, _track3, _track4, _track5, _track6, _track7, _track8, _track9]
    return tracks

    
def sortTracks(directory):
    # tracks = initTracks(directory)
    tracks = hardcodeTracks()
    printTracks(tracks)







sortTracks("./audio")
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



