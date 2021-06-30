class CheckMixing:
    def checkMix(self, oldKey, newKey = "1A"):
        key = Key(oldKey)

        '''
        print(f"{oldKey} {self.perfectMatch(key).toString()} {newKey}")
        print(f"{oldKey} {self.energyBoost(key).toString()} {newKey}")
        print(f"{oldKey} {self.energyDrop(key).toString()} {newKey}")
        print(f"{oldKey} {self.energySwitch(key).toString()} {newKey}")
        print(f"{oldKey} {self.moodBoost(key).toString()} {newKey}")
        print(f"{oldKey} {self.moodDrop(key).toString()} {newKey}")
        print(f"{oldKey} {self.domKey(key).toString()} {newKey}")
        print(f"{oldKey} {self.subDomKey(key).toString()} {newKey}")
        print(f"{oldKey} {self.energyRaise(key).toString()} {newKey}")
        print("----------")
        '''


        if self.perfectMatch(key).toString() == newKey:
            return True
        if self.energyBoost(key).toString() == newKey:
            return True
        if self.energyDrop(key).toString() == newKey:
            return True
        if self.energySwitch(key).toString() == newKey:
            return True
        if self.moodBoost(key).toString() == newKey:
            return True
        if self.moodDrop(key).toString() == newKey:
            return True
        if self.domKey(key).toString() == newKey:
            return True
        if self.subDomKey(key).toString() == newKey:
            return True
        if self.energyRaise(key).toString() == newKey:
            return True
        return False

    def perfectMatch(self, key):
        return key

    def energyBoost(self, key):

        key.hour = self.cyclicOffset(key.hour, 1, [1, 12])
        return key

    def energyDrop(self, key):

        key.hour = self.cyclicOffset(key.hour, -1, [1, 12])
        return key
    def energySwitch(self, key):
        key.letter = self.switchLetter(key.letter)
        return key
    def moodBoost(self, key):
        key.hour = self.cyclicOffset(key.hour, 3, [1, 12])
        return key
    def moodDrop(self, key):
        key.hour = self.cyclicOffset(key.hour, -3, [1, 12])
        return key
    def domKey(self, key):
        newKey = self.energySwitch(key)
        _newKey = self.energyBoost(newKey)
        return _newKey
    def subDomKey(self, key):
        newKey = self.energySwitch(key)
        _newKey = self.energyDrop(newKey)
        return _newKey
    def energyRaise(self, key):
        key.hour = self.cyclicOffset(key.hour, 7, [1, 12])
        return key
    #utils
    def cyclicOffset(self, reference, offset, limits):
        if offset and reference >= limits[0] and reference <= limits[1]:
            reference += offset
            if reference < limits[0]:
                reference += limits[1]
            if reference > limits[1]:
                reference -= limits[1]
        return reference
    def switchLetter(self, letter):
        if letter == 'A':
            return 'B'
        return 'A'

class Key:
    hour = 0,
    letter = "A"
    # def __init__(self, _hour, _letter):
    #     self.hour = _hour
    #     self.letter = _letter

    def __init__(self, oldKey):
        self.hour = int(oldKey[0])
        if len(oldKey) == 3:
            self.hour = int(f"{oldKey[0]}{oldKey[1]}")
        self.letter = oldKey[-1]
    def toString(self):
        return f"{self.hour}{self.letter}"
