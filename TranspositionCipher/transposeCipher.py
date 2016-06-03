import math

key = 0
plainText = ''
cipherText = ''
count = 0
x = 0

plainText = input("Enter plaintext: ").upper().replace (" ", "_")
key = int(input("Enter shift (Between 1 - < the length of the plaintext): "))
numRows = math.ceil(len(plainText) / key)
pad = input("Enter your padding: ").upper()

if key < len(plainText):
    while True:
        if len(plainText) == (numRows * key):
            break
        plainText += pad

    for i in range(key):
        x = count
        count += 1
        while True:
            cipherText += plainText[x]
            x += key
            if x >= len(plainText):
                break
    print(cipherText)
else:
    print("Key too large, try again")

