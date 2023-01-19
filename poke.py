def drawAscii(aFileName):
    file = open(aFileName + ".txt","r")
    image = file.read()
    print(image)
    file.close()

drawAscii("bulbul")           