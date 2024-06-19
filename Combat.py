import Screen
from pynput import keyboard
import os
import time

class Combat():
    def __init__(self,Oponent,Player):
        self.turnCounter = 0
        self.Oponent = Oponent
        self.Player = Player
        self.Hovered = 0
    #Draws a turn.
    def DrawTurn(self):
        self.Oponent.Draw()
        Screen.Write(self.Oponent.Name,type=self.Oponent.TextType,fgcolor=self.Oponent.TextColor)
        Screen.Write(" will play ")        
        Screen.Write(self.Oponent.WhatNextMove(),type=self.Oponent.TextType,fgcolor="Brown")
        Screen.Write("")
        print("\n",end="")
        self.Player.Hand.DisplayHand(self.Hovered,InCombat=True)
        print("\n",end="")
        Screen.Write(("+"+"-"*19)*4+"+\n")
        Screen.Write("|")
        Screen.Write("Mana: ",fgcolor="Blue")
        Screen.Write(str(self.Player.MP)+"/"+str(self.Player.maxMP))
        Screen.Write("          |")
        Screen.Write("HP: ",fgcolor="Red")
        Screen.Write(str(self.Player.HP)+"/"+str(self.Player.maxHP))
        Screen.Write("          |")
        Screen.Write("Shield: ",fgcolor="Green")
        Screen.Write(str(self.Player.Shield))
        Screen.Write("          |")
        Screen.Write("Armor: ",fgcolor="Brown")
        Screen.Write(str(self.Player.Armor))
        Screen.Write("           |\n")
        Screen.Write(("+"+"-"*19)*4+"+")
        print("\n",end="")

    def Start(self):
        
        end = False
        endPlayer = False
        # Opponent vs. Player Text
        for i in range(len(self.Oponent.Name)+1):
            Screen.WriteTitle(self.Oponent.Name[0:i],fgcolor=self.Oponent.TextColor)
            time.sleep(0.08)
            os.system('cls')
        
        for i in range(len("vs")+1):
            Screen.WriteTitle(self.Oponent.Name,fgcolor=self.Oponent.TextColor)
            Screen.WriteTitle("vs"[0:i],)
            time.sleep(0.08)
            os.system('cls')

        for i in range(len(self.Player.Name)+1):
            os.system('cls')
            Screen.WriteTitle(self.Oponent.Name,fgcolor=self.Oponent.TextColor)
            Screen.WriteTitle("vs")
            Screen.WriteTitle(self.Player.Name[0:i],type="Rainbow")
            time.sleep(0.08)
        
        time.sleep(2)
        #Combat loop and logic
        while (not end):
            while (not endPlayer):
                self.DrawTurn()
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
                                os.system('cls')
                                self.DrawTurn()
                            else:
                                self.Hovered=4    
                                os.system('cls')
                                self.DrawTurn()
                        case keyboard.Key.right:
                            if(self.Hovered!=4):
                                self.Hovered +=1    
                                os.system('cls')
                                self.DrawTurn()
                            else:
                                self.Hovered=0
                                os.system('cls')
                                self.DrawTurn()
                        case keyboard.Key.enter:
                            listener.stop()
                    if (key==Num1):
                        self.Hovered=0
                        os.system('cls')
                        self.DrawTurn()
                    elif (key==Num2):
                        self.Hovered=1
                        os.system('cls')
                        self.DrawTurn()
                    elif (key==Num3):
                        self.Hovered=2
                        os.system('cls')
                        self.DrawTurn()
                    elif (key==Num4):
                        self.Hovered=3
                        os.system('cls')
                        self.DrawTurn()
                    elif (key==Num5):
                        self.Hovered=4
                        os.system('cls')
                        self.DrawTurn()

                with keyboard.Listener(on_press=on_press) as listener:
                    listener.join()

                #Playing chosen card and displaying effect

                if(self.Player.Hand.Cards[self.Hovered].wasPlayed==False and self.Player.MP>=self.Player.Hand.Cards[self.Hovered].Cost):
                    os.system('cls')
                    if(self.Player.Hand.Cards[self.Hovered].Damage!=0):
                        Screen.LoreRead("You deal "+str(self.Player.Hand.Cards[self.Hovered].Damage),speed=1)
                        Screen.LoreRead(" Damage.",fgcolor="Blue",speed=1) 
                        print('\n', end='')
                        time.sleep(0.5)
                    if(self.Player.Hand.Cards[self.Hovered].Heal!=0):
                        Screen.LoreRead("You heal "+str(self.Player.Hand.Cards[self.Hovered].Heal),speed=1)
                        Screen.LoreRead(" HP.",fgcolor="Red",speed=1) 
                        print('\n', end='')
                        time.sleep(0.5)
                    if(self.Player.Hand.Cards[self.Hovered].Shield!=0):
                        Screen.LoreRead("You gain "+str(self.Player.Hand.Cards[self.Hovered].Shield),speed=1)
                        Screen.LoreRead(" Shield.",fgcolor="Green",speed=1)
                        print('\n', end='')
                        time.sleep(0.5)
                    if(self.Player.Hand.Cards[self.Hovered].Armor!=0):
                        Screen.LoreRead("You gain "+str(self.Player.Hand.Cards[self.Hovered].Armor),speed=1)
                        Screen.LoreRead(" Armor.",fgcolor="Brown",speed=1)
                        print('\n', end='')
                        time.sleep(0.5)
                    self.Player.Hand.Cards[self.Hovered].PlayCard(self.Player,self.Oponent)
                    os.system('cls')
                
                if(self.Oponent.HP <= 0):
                    break
                temp =[]

                for k in range(5):
                    temp.append(int(self.Player.Hand.Cards[k].Cost))
                #Checking if player is out of mana or possible moves.
                if(self.Player.MP == 0 or min(temp) > self.Player.MP):
                    time.sleep(0.75)
                    break

            if(self.Oponent.HP <= 0 ):
                break
            
            #Opponent turn.
            os.system('cls')
            Screen.LoreRead(self.Oponent.Name,type=self.Oponent.TextType,fgcolor=self.Oponent.TextColor,speed=1)
            Screen.LoreRead(" plays ",speed=1)
            Screen.LoreRead(self.Oponent.WhatNextMove(),type=self.Oponent.TextType,fgcolor="Brown",speed=1)
            print('\n', end='')
            self.Oponent.MakeTurn(self.Player)
            os.system('cls')
            self.Player.Hand.Update()
            self.Player.MP = 3
            self.Player.Armor = 0
            if(self.Player.HP <= 0 ):
                break