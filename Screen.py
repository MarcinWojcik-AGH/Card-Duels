import Colors
import Letters
from pynput import keyboard
import cursor
import os
import time
#Writes with normal letters
def Write(text,type="Normal",fgcolor="Grey",bgcolor="Black"):
    temp1 = text.split("Rainbow Dragon")
    if (len(temp1)>1 and text != "Rainbow Dragon"):
        for i in range(len(temp1)):
            if (i != 0):
                Write("Rainbow Dragon","Rainbow")
            Write(temp1[i],type,fgcolor,bgcolor)
        return
    print(Colors.AddColor(text,type,fgcolor,bgcolor), end='')
#Writes with huge letters
def WriteTitle(text,type="Normal",fgcolor="Grey",bgcolor="Black",tittle=True):
    Letters.printTitle(text,type,fgcolor,bgcolor,tittle)
#Prints Options
def PrintOptions(Options,Chosen=0,Header=None,First=False):
    if(Header!=None):
        temp1 = Header.split('|')
        temp2 = temp1[0].split("(o)")
        
        for j in range(len(temp2)):
            if(First==True):
                LoreRead(temp2[j],temp1[1],temp1[2],temp1[3])
                print("\n",end="")
            else:
                Write(temp2[j]+"\n",temp1[1],temp1[2],temp1[3])
    for i in range(len(Options)):
        temp = Options[i].split('|')
        
        if(Chosen!=i):
            Write(temp[0]+"\n",temp[1],temp[2],temp[3])
        else:
            Write(">"+temp[0]+"<"+"\n",temp[1],temp[3],temp[2])
        if(First==True):
            time.sleep(0.1)
    print("\033[0;37;40m")

Hovered = 0
Answer = 0
#Lets Player choose an option
def ChoseOption(Options,Choice=0,Header=None):
    global Hovered
    global Answer
    First = True
    PrintOptions(Options,Hovered,Header,First)
    First = False
    Hovered = Choice
    def on_press(key):
        global Hovered
        global Answer
        match key:
            case keyboard.Key.up:
                if(Hovered!=0):
                    Hovered -= 1
                    os.system('cls')
                    PrintOptions(Options,Hovered,Header)
                else:
                    Hovered=len(Options)-1
                    os.system('cls')
                    PrintOptions(Options,Hovered,Header)
            case keyboard.Key.down:
                if(Hovered!=len(Options)-1):
                    Hovered +=1
                    os.system('cls')
                    PrintOptions(Options,Hovered,Header)
                else:
                    Hovered=0
                    os.system('cls')
                    PrintOptions(Options,Hovered,Header)
            case keyboard.Key.enter:
                
                input()
                os.system('cls')
                time.sleep(0.5)
                Answer = Hovered
                Hovered = 0
                listener.stop()  
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    return Answer
#Creates Yes or No question
def YesorNoQuestion(Header,Chosen=0):
    file = open("YesNo.txt","r")
    YesorNo = list(file.readlines())
    file.close()
    return ChoseOption(YesorNo,Chosen,Header)
#Prints slowly appearing text.
def LoreRead(text,type="Normal",fgcolor="Grey",bgcolor="Black",speed=2):
    temp1 = text.split("Rainbow Dragon")
    if (len(temp1)>1 and text != "Rainbow Dragon"):
        for i in range(len(temp1)):
            if (i != 0):
                LoreRead("Rainbow Dragon","LoreRainbow",speed=speed)
            LoreRead(temp1[i],type,fgcolor,bgcolor,speed)
        return
    for i in text:
        print(Colors.AddColor(i,type,fgcolor,bgcolor), end='')
        time.sleep(int(speed)/100)

class Menu:
    #Loads Menu from file
    def __init__(self,ID):
        self.ID=ID
        file = open("Menus\Menu"+str(ID)+".txt","r")
        lines = file.readlines()
        file.close()
        self.Tittle = lines[0]
        self.Description = lines[1]
        self.Options = lines[2:len(lines)]
        file = open("Links.txt","r")
        self.Links = list(file.readlines())[ID] 
        file.close()
        self.Chosen = 0
    #Draws a Menu
    def Draw(self):
        os.system('cls')
        Tittle=self.Tittle.split('|')
        
        WriteTitle(Tittle[0],Tittle[1],Tittle[2],Tittle[3])
        
        Description=self.Description.split('|')
        DescLines=Description[0].split("(o)")
        for j in range(len(DescLines)):    
            Write(DescLines[j]+"\n",Description[1],Description[2],Description[3])
        
        PrintOptions(self.Options,self.Chosen)

        print("\033[0;37;40m")
    #Let's player choose a menu option
    def Choice(self):
        self.Draw()
        def on_press(key):
            global IsEscapePressed
            match key:
                case keyboard.Key.up:
                    if(self.Chosen!=0):
                        self.Chosen -= 1
                        self.Draw()
                    else:
                        self.Chosen=len(self.Options)-1
                        self.Draw()
                case keyboard.Key.down:
                    if(self.Chosen!=len(self.Options)-1):
                        self.Chosen +=1
                        self.Draw()
                    else:
                        self.Chosen=0
                        self.Draw()
                case keyboard.Key.enter:
                    IsEscapePressed=False
                    input()
                    os.system('cls')
                    time.sleep(0.5)
                    listener.stop()
                case keyboard.Key.esc:
                    IsEscapePressed=True
                    listener.stop()   
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        if(IsEscapePressed!=True):
            return self.Links[self.Chosen]
        else:
            return -1
