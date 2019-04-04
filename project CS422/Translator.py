import holder
fileName=holder.progName

def printFilename():
    print(fileName)
    return

import toJson
from toJson import*

def idGenerator(filename):
    import datetime
    token=filename+"_"+str(datetime.datetime.now())
    return token

def jsonCreate():
    global fileName
    fileName=idGenerator(fileName)
    formatFileName()
    toJson.fileCreate()
    return
def formatFileName():
    global fileName
    ret=fileName.replace(":","_")
    ret=ret.replace(" ","")
    ret=ret.replace(".","_")
    fileName=ret
    return ret
