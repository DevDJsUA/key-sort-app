import classes
import math
from  random import randint, shuffle
from classes.movements import movements

class createHarmonicMixingPattern:
#     perfectMatch = 35  # perfectMatch (=)
#     energyBoost = 10  # energyBoost (+1)
#     energyDrop = 10  # energyDrop (-1)
#     energySwitch= 10  # energySwitch (B/A)
#     moodBoost = 5  # moodBoost (+3)
#     moodDrop = 5  # moodDrop (-3)
#     energyRaise = 5  # energyRaise (+7)
#     domKey = 10  # domKey (+1 & B/A) = energyBoost & energySwitch
#     subDomKey = 10  # subDomKey (-1 & B/A) = energyDrop & energySwitch
# movements = Movements()
# checkMixing = CheckMixing()
    def createHarmonicMixingPattern(self, playlistLenght):
        
    
        pattern = []

        for key in movements:
            keysLen = math.ceil(playlistLenght * movements[key] / 100)

            # print(key.title())
 
            for i in range(keysLen):
                pattern.append(key.title())

        result = []
        result = pattern
        shuffle(result)
        return result

        # for i in result:
        #     print(i)
    



                    
cr = createHarmonicMixingPattern()
cr.createHarmonicMixingPattern(20)