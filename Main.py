import cursor
import time
import Screen
import Colors
import os
import Entities
import Save

cursor.hide()
#Main funtion, will be built upon when i figure out game logic.
def RunGame(ID):
    temp = Screen.Menu(ID)
    nextID = temp.Choice()
    if (nextID == -1):
        quit()
    elif(nextID == "m"):
        print("Works!")
    elif(int(nextID) == 1):
        Player1 = Entities.Player()
    elif(int(nextID) == 4):
        os.system('cls')
        cursor.show()
        Pass = input(Colors.AddColor("Password:","Normal","Brown"))
        cursor.hide()
        if(Pass=="Sek"):
            RunGame(4)
        else:
            Screen.Write("Naah","Normal","Red")
            time.sleep(3)
            RunGame(0)        
    else:    
        RunGame(int(nextID))

Save.CreateClientData()
RunGame(0)
