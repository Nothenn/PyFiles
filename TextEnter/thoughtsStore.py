import os
import time

wordInput = raw_input("")
y = (time.strftime("%d/%m/%Y at %H:%M") + "\n" + wordInput)

with open("words.txt","a") as x:
    x.write("\n\n" + y)
