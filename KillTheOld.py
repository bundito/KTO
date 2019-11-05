
import os
import dateutil
from os import stat
import time
import moment

BASEDIR = r'C:\Users\bundi\Downloads\\'

isoFiles = []
isoDirs = []

filesOnly = os.scandir(BASEDIR)

def dateCheck(item):
    itemTime = os.path.getatime(item)

    # itemTime =  * 1000

    # make moments

    itemMoment = moment.unix(itemTime)
    nowMoment = moment.now()

    agedSeven = moment.unix(itemTime).add(days=7)

    if agedSeven > nowMoment:
        itemSafe = True
    else:
        itemSafe = False


    print("item: ", item)
    print("atime: ", itemMoment)
    print("aged: ", agedSeven)
    print("safe: ", itemSafe)
    print("-----------------")


for thisFile in filesOnly:
    if os.path.isfile(thisFile):
        if os.path.splitext(thisFile)[1] == ".iso":
            isoFiles.append(thisFile)
            dateCheck(thisFile)

dirsOnly = os.listdir(BASEDIR)

for searchDir in os.scandir(BASEDIR):
    if os.path.isdir(searchDir):
        for seekFile in os.listdir(searchDir):
            if os.path.splitext(seekFile)[1] == ".iso":
                dateCheck(searchDir)
                isoDirs.append(searchDir)
                break

'''
print("---- FILES ----")
for isoFile in isoFiles:
    print(isoFile)

print("\n")

print("---- DIR ----")
for isoDir in isoDirs:
    print(isoDir)
'''