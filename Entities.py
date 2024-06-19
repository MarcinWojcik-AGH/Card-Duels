import Cards
import os
import Screen
import time
import Colors

class Entity():

    def ReciveDamage(self,Damage):
        self.Shield -= Damage - self.Armor
        if(self.Shield<0):
            self.HP += self.Shield
            self.Shield = 0
    
    def Heal(self,Heal):
        if(self.HP<=self.maxHP):
            self.HP = self.HP + Heal
            if(self.HP<self.maxHP):
                self.HP = self.maxHP
    
    def GainAP(self,bonusAP):
        self.Armor += bonusAP
    
    def GainSP(self,bonusSP):
        self.Shield += bonusSP
    
    def DealDamage(self,Damage,Enemy):
        Enemy.ReciveDamage(Damage)
    #Draws Entity
    def Draw(self,type="Normal",fgcolor="Grey",bgcolor="Black",forceColors=False):
        file = open(f"Enemies\{self.Name}.txt", "r")
        self.Image = list(file.readlines())
        file.close()
        if(self.HP <= self.maxHP/4 and forceColors==False):    
            for line in self.Image:
                Screen.Write(line,type="Blinking",fgcolor="Red")
        else:
            for line in self.Image:
                Screen.Write(line,type=type,fgcolor=fgcolor,bgcolor=bgcolor)
        Screen.Write("HP: ",fgcolor="Red")
        Screen.Write(str(self.HP)+"/"+str(self.maxHP)+"     ")
        Screen.Write("Shield: ",fgcolor="Green")
        Screen.Write(str(self.Shield)+"     ")
        Screen.Write("Armor: ",fgcolor="Brown")
        Screen.Write(str(self.Armor))
        

        print("\n",end="")
    #Informs Player about what move does
    def InformPlayer(self,type,value):
        if(type=="Damage"):
            Screen.LoreRead(self.Name,type=self.TextType,fgcolor=self.TextColor,speed=1)
            Screen.LoreRead(" deals "+ str(value) +" ",speed=1)
            Screen.LoreRead("Damage.",fgcolor="Blue",speed=1)
            time.sleep(0.5)
        if(type=="Heal"):
            Screen.LoreRead(self.Name,type=self.TextType,fgcolor=self.TextColor,speed=1)
            Screen.LoreRead(" heals "+ str(value) +" ",speed=1)
            Screen.LoreRead("HP.",fgcolor="Red",speed=1)
            time.sleep(0.5)
        if(type=="Shield"):
            Screen.LoreRead(self.Name,type=self.TextType,fgcolor=self.TextColor,speed=1)
            Screen.LoreRead(" gains "+ str(value) +" ",speed=1)
            Screen.LoreRead("Shield.",fgcolor="Green",speed=1)
            time.sleep(0.5)
        if(type=="Armor"):
            Screen.LoreRead(self.Name,type=self.TextType,fgcolor=self.TextColor,speed=1)
            Screen.LoreRead(" gains "+ str(value) +" ",speed=1)
            Screen.LoreRead("Armor.",fgcolor="Brown",speed=1)
            time.sleep(0.5)
    
    
    #Error Checks
    def WhatMoveNext():
        print("Entity doesnt have AI XD")
    def MakeTurn():
        print("Entity doesnt have AI XD")

class Player(Entity):
    
    def __init__(self):
        self.Name = ""
        self.maxHP = 20
        self.HP = self.maxHP
        self.maxMP = 3
        self.MP = self.maxMP
        self.Class = "Fighter"
        self.Armor = 0
        self.Shield = 0
        os.system('cls')
        Screen.LoreRead("Whats your name adveturer?")
        print("\n",end="")
        self.Name = input()
        os.system('cls')
        file = open("ClassesChoice.txt","r")
        ClassOptions = list(file.readlines())
        file.close()
        end = False
        while end==False:
            temp = Screen.ChoseOption(ClassOptions[1:len(ClassOptions)-4],Header=ClassOptions[0])
            file = open("ClientSave.txt","r")
            ClientSaveData = list(file.readlines())
            file.close()
            match temp:
                case 0:
                    if Screen.YesorNoQuestion(ClassOptions[temp + 5],0) == 0:
                        self.Class = "Fighter"
                        end = True
                case 1:
                    Ans = Screen.YesorNoQuestion(ClassOptions[temp + 5],0)
                    if (Ans == 0 and int(ClientSaveData[0]) >= 1):
                        self.Class = "Paladin"
                        end = True
                    elif(Ans == 0 and int(ClientSaveData[0]) < 1):
                        Screen.LoreRead("You need to defeat ")
                        Screen.LoreRead("Rainbow Dragon ","LoreRainbow")
                        Screen.LoreRead("at least once to unlock Paladin.")
                        time.sleep(2)
                        os.system('cls')
                case 2:
                    Ans = Screen.YesorNoQuestion(ClassOptions[temp + 5],0)
                    if (Ans == 0 and int(ClientSaveData[0]) >= 2):
                        self.Class = "Paladin"
                        end = True
                    elif(Ans == 0 and int(ClientSaveData[0]) < 2):
                        Screen.LoreRead("You need to defeat ",)
                        Screen.LoreRead("Rainbow Dragon ","LoreRainbow")
                        Screen.LoreRead("at least twice to unlock Mage.")
                        time.sleep(2)
                        os.system('cls')
                case 3:
                    Ans = Screen.YesorNoQuestion(ClassOptions[temp + 5],0)
                    if (Ans == 0 and int(ClientSaveData[4]) == 1):
                        self.Class = "Paladin"
                        end = True
                    elif(Ans == 0 and int(ClientSaveData[4]) != 1):
                        Screen.LoreRead("You need to defeat ",)
                        Screen.LoreRead("Rainbow Dragon ","LoreRainbow")
                        Screen.LoreRead("at least once as each character to unlock Berserker.")
                        time.sleep(2)
                        os.system('cls')
        match self.Class:
            case "Fighter":
                self.Hand = Cards.Hand(Cards.Card(0),Cards.Card(0),Cards.Card(1),Cards.Card(1),Cards.Card(2))
            case "Paladin":
                pass
            case "Mage":
                pass
            case "Berserker":
                pass

    
class Goblin(Entity):
    
    def __init__(self):
        self.Shield = 0
        self.Armor = 0
        self.maxHP = 7
        self.Shield = 0
        self.HP = self.maxHP
        self.Name = "Goblin"
        self.moves = ["Kick and Retreat","Broken Sword"]
        self.TextType = "Darker"
        self.TextColor = "Green"       
    #Example move
    def KickandRetreat(self,Player):
        self.GainSP(2)
        self.InformPlayer("Shield",2)
        self.DealDamage(2,Player)
        self.InformPlayer("Damage",2)
    #Example move 2
    def BrokenSword(self,Player):
        self.DealDamage(3,Player)
        self.InformPlayer("Damage",3)
    #AI
    def WhatNextMove(self):
        if(self.HP>4):
            return self.moves[1]
        else:
            return self.moves[0]
    #AI 2
    def MakeTurn(self,Player):
        if(self.HP>4):
            self.BrokenSword(Player)  
        else:
            self.KickandRetreat(Player)