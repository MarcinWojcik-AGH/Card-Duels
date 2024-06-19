import Colors
from pynput import keyboard
import os

Rarities = {
    "Common":["Normal","Grey"],
    "Uncommon":["Normal","Green"],
    "Rare":["Normal","Blue"],
    "Very Rare":["Normal","Magenta"],
    "Legendary":["Normal","Brown"],
    "Boss":["Normal","Red"],
    "Unique":["Rainbow","Grey"]
}
class Card:
    #Card Creator
    def __init__(self,ID):
        global Rarities
        self.ID = ID
        file = open("CardIndex.txt","r")
        self.CardInfo = file.readlines()[ID].split('|')
        file.close()
        self.Name = self.CardInfo[0]
        self.Description = self.CardInfo[1]
        self.Rarity = self.CardInfo[2]
        self.Cost = int(self.CardInfo[3])
        self.Damage = int(self.CardInfo[4])
        self.Heal = int(self.CardInfo[5])
        self.Shield = int(self.CardInfo[6])
        self.Armor = int(self.CardInfo[7])
        self.wasPlayed = False
        Info = []
        if(int(self.Damage)!=0):
            Info.append(" Deal "+str(self.Damage)+" Dmg. ")
        if(int(self.Heal)!=0):
            Info.append(" Heal "+str(self.Heal)+" HP   ")
        if(int(self.Shield)!=0):
            Info.append(" Gain "+str(self.Shield)+" SP   ")
        if(int(self.Armor)!=0):
            Info.append(" Gain "+str(self.Armor)+" AP   ")
        if(len(Info)!=4):
           Info = Info + [0]*(4-len(Info))
        self.CardView = []
        self.CardView.append("+-+-----------+")
        self.CardView.append("|"+Colors.AddColor(str(self.Cost),textcolor="Cyan")+"\033[0;37;40m|"+Colors.AddColor(self.Name,type=Rarities[self.Rarity][0],textcolor=Rarities[self.Rarity][1])+"\033[0;37;40m"+" "*(11-len(self.Name))+"|")
        self.CardView.append("+-+-----------+")
        if(Info[0]!=0):
            self.CardView.append("|"+Info[0]+"|")
        else:
            self.CardView.append("|             |")    
        self.CardView.append("|             |")
        if(Info[1]!=0):
            self.CardView.append("|"+Info[1]+"|")
        else:
            self.CardView.append("|             |")
        self.CardView.append("|             |")
        if(Info[2]!=0):
            self.CardView.append("|"+Info[2]+"|")
        else:
            self.CardView.append("|             |")
        self.CardView.append("|             |")
        if(Info[3]!=0):
            self.CardView.append("|"+Info[3]+"|")
        else:
            self.CardView.append("|             |")
        self.CardView.append("+-------------+")
    #Display single card
    def DisplayCard(self):
        global Rarities
        if(self.wasPlayed==True):
            self.wasPlayed==False
            self.CardView[1]="|"+Colors.AddColor(str(self.Cost),textcolor="Cyan")+"\033[0;37;40m|"+Colors.AddColor(self.Name,type=Rarities[self.Rarity][0],textcolor=Rarities[self.Rarity][1])+"\033[0;37;40m"+" "*(11-len(self.Name))+"|"
        for line in self.CardView:
            print(line)
    #Plays card
    def PlayCard(self,Player,Enemy):
        if(self.Damage!=0):
            Enemy.ReciveDamage(self.Damage)
        if(self.Heal!=0):
            Player.Heal(self.Heal)
        if(self.Shield!=0):
            Player.GainSP(self.Shield)
        if(self.Armor!=0):
            Player.GainAP(self.Armor)
        self.wasPlayed=True
        Player.MP -= self.Cost

class Hand:

    def __init__(self,Card1,Card2,Card3,Card4,Card5):
        self.Cards = []
        self.Cards.append(Card1)
        self.Cards.append(Card2)
        self.Cards.append(Card3)
        self.Cards.append(Card4)
        self.Cards.append(Card5)
        self.Hovered = 0
    
    def __str__(self):
        for i in range(5):
            print(self.Cards[i].CardInfo)
        return "Your Hand!"
    
    def ChangeCard(self,ID,Card1):
        self.Cards[ID]=Card1
    
    def Update(self):
        for i in range(5):
            self.Cards[i].wasPlayed=False
    #Display Player's hand
    def DisplayHand(self,Hovered,InCombat=False):
        global Rarities
        if(InCombat==True):
            for k in range(5):
                if(self.Cards[k].wasPlayed==False):
                    self.Cards[k].CardView[1]="|"+Colors.AddColor(str(self.Cards[k].Cost),textcolor="Cyan")+"\033[0;37;40m|"+Colors.AddColor(self.Cards[k].Name,type=Rarities[self.Cards[k].Rarity][0],textcolor=Rarities[self.Cards[k].Rarity][1])+"\033[0;37;40m"+" "*(11-len(self.Cards[k].Name))+"|"
                else:
                    self.Cards[k].CardView[1]="|"+Colors.AddColor(str(self.Cards[k].Cost),type="Reverse",textcolor="Red")+"\033[0;37;40m|"+Colors.AddColor(self.Cards[k].Name,type=Rarities[self.Cards[k].Rarity][0],textcolor=Rarities[self.Cards[k].Rarity][1])+"\033[0;37;40m"+" "*(11-len(self.Cards[k].Name))+"|"
        for i in range(14):
            temp = ""
            if(i<3):
                temp = " "*(Hovered*16)+self.Cards[Hovered].CardView[i]+" "+" "*((4-Hovered)*16)
            else:
                for j in range(5):
                    if(j==Hovered):
                        try:
                            temp=temp+self.Cards[j].CardView[i]+" "
                        except:
                            temp=temp+" "*16
                    else:
                        temp=temp+self.Cards[j].CardView[i-3]+" "            
            print(temp)
    #Choses a card to play from plaers hand(by player input)
    def ChooseCard(self,InCombat=False):
        self.Hovered = 0
        self.DisplayHand(self.Hovered,InCombat)
        def on_press(key):
            Num1 = keyboard.KeyCode.from_char('1')
            Num2 = keyboard.KeyCode.from_char('2')
            Num3 = keyboard.KeyCode.from_char('3')
            Num4 = keyboard.KeyCode.from_char('4')
            Num5 = keyboard.KeyCode.from_char('5')
            match key:
                case keyboard.Key.left:
                    if(self.Hovered!=0):
                        self.Hovered -= 1
                        if(InCombat==False):
                            os.system('cls')
                        self.DisplayHand(self.Hovered,InCombat)
                    else:
                        self.Hovered=4
                        if(InCombat==False):    
                            os.system('cls')
                        self.DisplayHand(self.Hovered,InCombat)
                case keyboard.Key.right:
                    if(self.Hovered!=4):
                        self.Hovered +=1
                        if(InCombat==False):    
                            os.system('cls')
                        self.DisplayHand(self.Hovered,InCombat)
                    else:
                        self.Hovered=0
                        if(InCombat==False):
                            os.system('cls')
                        self.DisplayHand(self.Hovered,InCombat)
                case keyboard.Key.enter:
                    if(InCombat==True):
                        self.Cards[self.Hovered].wasPlayed=True
                    os.system('cls')
                    listener.stop()
            if (key==Num1):
                self.Hovered=0
                os.system('cls')
                self.DisplayHand(self.Hovered,InCombat)
            elif (key==Num2):
                self.Hovered=1
                os.system('cls')
                self.DisplayHand(self.Hovered,InCombat)
            elif (key==Num3):
                self.Hovered=2
                os.system('cls')
                self.DisplayHand(self.Hovered,InCombat)
            elif (key==Num4):
                self.Hovered=3
                os.system('cls')
                self.DisplayHand(self.Hovered,InCombat)
            elif (key==Num5):
                self.Hovered=4
                os.system('cls')
                self.DisplayHand(self.Hovered,InCombat)       
            
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
        
        return self.Cards[self.Hovered]