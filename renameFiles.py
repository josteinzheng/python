import os

def renameFiles(path):
    fileList = os.listdir(path);
    for fileName in fileList:
        newName = fileName.translate(None, "0123456789")
        print(fileName + ' to ' + newName)
        os.chdir(path)
        os.rename(fileName, newName)

renameFiles(r"/Users/jostein/temp/prank")
