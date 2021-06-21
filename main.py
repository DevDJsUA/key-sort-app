import KeyDetect
import os




dict = {'C Maj':'8B','C# Maj':'3B','D Maj':'10B','D# Maj':'5B','E Maj':'12B','F Maj':'7B','F# Maj':'2B','G Maj':'9B','G# Maj':'4B','A Maj':'11B','A# Maj':'6B','B Maj':'1B','c min':'5A','c# min':'12A','d min':'7A','d# min':'2A','e min':'9A','f min':'4A','f# min':'11A','g min':'6A','g# min':'1A','a min':'8A','a# min':'3A','b min':'10A'}

key = KeyDetect.keyDetect("test2.mp3")
print(dict[key])



'''
engKey = ['C Maj', 'C# Maj', 'D Maj', 'D# Maj', 'E Maj', 'F Maj', 'F# Maj', 'G Maj', 'G# Maj', 'A Maj', 'A# Maj', 'B Maj','c min', 'c# min', 'd min', 'd# min', 'e min', 'f min', 'f# min', 'g min', 'g# min', 'a min', 'a# min', 'b min']

altKey = ['8B', '3B','10B','5B','12B','7B','2B','9B','4B','11B','6B','1B','5A','12A','7A','2A','9A','4A','11A','6A', '1A', '8A', '3A', '10A' ]
'''



