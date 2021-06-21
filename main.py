import KeyDetect


engKey = ['C Maj', 'C# Maj', 'D Maj', 'D# Maj', 'E Maj', 'F Maj', 'F# Maj', 'G Maj', 'G# Maj', 'A Maj', 'A# Maj', 'B Maj','c min', 'c# min', 'd min', 'd# min', 'e min', 'f min', 'f# min', 'g min', 'g# min', 'a min', 'a# min', 'b min']

altKey = ['8B', '3B','10B','5B','12B','7B','2B','9B','4B','11B','6B','1B','5A','12A','7A','2A','9A','4A','11A','6A', '1A', '8A', '3A', '10A' ]

key = KeyDetect.keyDetect("test2.mp3")
# result = ""
# for i in range(24):
#     if key == engKey[i]:
#         result = altKey[i]


# print(result)
print(key)

# for i in range(24):
#     print(f"{engKey[i]} / {altKey[i]} \n")