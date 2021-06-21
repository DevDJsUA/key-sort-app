import KeyDetect


engKey = ['C Maj', 'C# Maj', 'D Maj', 'D# Maj', 'E Maj', 'F Maj', 'F# Maj', 'G Maj', 'G# Maj', 'A Maj', 'A# Maj', 'B Maj','c min', 'c# min', 'd min', 'd# min', 'e min', 'f min', 'f# min', 'g min', 'g# min', 'a min', 'a# min', 'b min']

altKey = ['8b', '','10b','','12b','7b','2b','9b','','11b','','1b','5a','','7a','','9a','4a','11a','6a', '', '8a', '', '10a' ]

# key = KeyDetect.keyDetect("test2.mp3")
# print(key)

for i in range(24):
    print(f"{engKey[i]} / {altKey[i]} \n")