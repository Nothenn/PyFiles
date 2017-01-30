from pydub import AudioSegment
import re
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
filename = filedialog.askopenfilename()
root.withdraw()
#filename = "\"" + filename + "\""
#filename = filename.replace('/','\\')
print(filename)

#sound = AudioSegment.from_mp3("D:\My Music\Chill\left alone in the rain.mp3")
sound = AudioSegment.from_mp3(filename)

#Read in timestamp file
with open("txt.txt", "r") as f:
    array = []
    for line in f:
        array.append(line.strip('\n'))

count = 0
for x in array:
    
    split = x.split(" ",1)
    time = split[0]

    s = time
    minutes, seconds = (["0", "0"] + s.split(":"))[-2:]
    minutes = int(minutes)
    seconds = float(seconds)
    miliseconds = int(60000 * minutes + 1000 * seconds)
    array[count] = str(miliseconds) + " " + split[1]
    name = array[count].split(" ",2)
    count += 1

newcount = 0
for x in array:

    if ((newcount + 1) < len(array)):
        tim1 = array[newcount].split(" ",1)
        tim2 = array[newcount + 1].split(" ",1)
        name = tim1[1]
        for ch in ['<','>',':','\"','/','\\','|','?','*']:
            if ch in name:
                name=name.replace(ch,"")
        print(name)

        tim1 = int(tim1[0]) #0
        tim2 = int(tim2[0]) #1700000
    else:
        tim1 = array[newcount].split(" ",1)
        tim2 = sound.duration_seconds * 1000
        name = tim1[1]
        for ch in ['<','>',':','\"','/','\\','|','?','*']:
            if ch in name:
                name=name.replace(ch,"")
        tim1 = int(tim1[0]) #0
        print(name)
    
    song = sound[:tim2]
    test = tim2 - tim1
    song = song[-test:]
    #song.export("D:/My Music/Test/" + name + ".mp3", format="mp3")
    newcount+=1

input('Press ENTER to exit')

