from Translator import*


def fileCreate(extension):
    name=addExtension(fileName,extension)
    with open(name, 'w'):
        pass
    return name


def addExtension(filename, PL):
    if PL=="C":
        filename+=".c"
    return filename
