from typing import Callable
import typing_extensions

print("ahoj")
print(144 % 15)

print("python is great".title())

print("Python Is Great".swapcase())
#print("John Keller". initials())
print("rebelliousness"[2::3])

nine_words="The man the professor the student has studies Rome".split()
print(nine_words)
print(nine_words[-2])

#cat < dog
#Katze < Hund

veta = "Sphinx of black quartz; judge my wov"
retezec = "art"
if retezec in veta:
    print("nalezeno")
else:
    print("nenalezeno")