def fileCreate():
    name="json/"+addExtension()
    with open(name, 'w'):
        pass
    return name
def addExtension():
    from Translator import fileName
    ret= fileName + ".json"
    return ret
    
