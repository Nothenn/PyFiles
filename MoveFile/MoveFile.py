import os
import shutil

cwd = os.getcwd()

folderName = (cwd + '\\' + input('Folder Name: ') + '\\')

fileList = os.listdir(folderName)
fileList = [folderName + filename for filename in fileList]

for f in fileList:
    print((f, folderName))
    if f.endswith('.db'):
        print("Skipped Thumbs.db")
    else:
        shutil.move(f, cwd)
