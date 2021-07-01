from modules.classes.createHarmonicMixingPattern import createHarmonicMixingPattern
from ...modules.classes.movements import movements
from ...modules.classes.checkMixing import CheckMixing

checkMixing = CheckMixing()

"""
Использует рандомный createHardmonicMixingPatter и ищет сводки под них.
"""
def sortTracksUseCreateHarmonicMixingPattern(tracks):       
    allTracks = tracks
    oldTracks = tracks
    newTracks = []
    patterns = createHarmonicMixingPattern.createHarmonicMixingPattern(len(allTracks)) 

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
    for patt in patterns:
        print(patt)
    return [newTracks, oldTracks]