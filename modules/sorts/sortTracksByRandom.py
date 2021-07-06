from modules.classes.createHarmonicMixingPattern import createHarmonicMixingPattern
from modules.classes.movements import movements
from modules.classes.checkMixing import CheckMixing
from modules.classes.track import Track
from random import shuffle

checkMixing = CheckMixing()
import configparser

def getSteps():
    return int(config['sorttracks']['steps'])

config = configparser.ConfigParser()
config.read("config.ini")
steps = getSteps()

"""
Берем массив треков.
Создаем локальный, который рандомизируем.
Проходимся по нему, сводки которые выходят кидаем в массив.
То, что вышло добавляем в массив массивов.
И так 'количество треков в квадарате' раз.
"""
def sortTracksByRandom(tracks):
    _tracks = tracks #все треки, и каждый шаг, мы будем этот массив рандомизировать
    arrayOfMixing = [] #массив, массивов, в котором лежат треки в последовательности получившихся сводок
    tempMixingTracks = [] #временные треки, которые мы берем из массива _tracks, который рандомизируется, при получившейся сводке, убираем из него трек
    tempMixedTracks = [] #треки, которые мы добавляем сюда при получившейся сводке
    global steps
    # steps = len(tracks) * len(tracks)
    while steps > 0:
        no = steps
        tempMixingTracks = _tracks.copy()
        tempMixedTracks.append(tempMixingTracks[0])
        tempMixingTracks.remove(tempMixingTracks[0])

        while no > 0:
            checkM = False
            j = 0
            for value in tempMixingTracks:
                key = value.getKey()
                checkM = checkMixing.checkMix(tempMixedTracks[-1].getKey(), key)
                if(checkM == True):
                    tempMixedTracks.append(tempMixingTracks[j])
                    tempMixingTracks.remove(tempMixingTracks[j])
                j += 1
            j = 0
            if checkM == False:
                no -= 1
            checkM = False

        steps -= 1
        arrayOfMixing.append(tempMixedTracks)
        shuffle(_tracks)
        tempMixingTracks = _tracks.copy()
        tempMixedTracks = []

    arrayOfMixing.sort(key=len)
    steps = getSteps()
    # for array in arrayOfMixing:
    #     print("-------------------")
    #     for j in array:
    #         print(f" {j.getId()} {j.getKey()}|", end=" ")
    #     print("\n--------------")
    
    sortedMixes = []
    arrayOfMixing.reverse()
    maxLenghtOfMix = len(arrayOfMixing[0])
    print(len(arrayOfMixing[0]))
    print(len(arrayOfMixing[-1]))
    for i in arrayOfMixing:
        if len(i) == maxLenghtOfMix:
            sortedMixes.append(i)
            arrayOfMixing.remove(i)
        else:
            break 

    return [sortedMixes, arrayOfMixing]

