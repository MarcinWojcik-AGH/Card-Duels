#Creates a save file

def CreateClientData():
    file = open("ClientSave.txt","w")
    file.write("0\n")
    file.write("0\n")
    file.write("0\n")
    file.write("0\n")
    file.write("0")
    file.close()
