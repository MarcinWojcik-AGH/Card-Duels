import Screen
import random
#In development
class Dungeon():
    
    def Create(self,EventNumber,LoreNumber,MonsterNumber,EventPool,LorePool,MonsterPool,Boss):
        for i in range(EventNumber):
            self.Rooms.append(random.choice(EventPool))
        for i in range(LoreNumber):
            self.Rooms.append(random.choice(LorePool))
        for i in range(MonsterNumber):
            self.Rooms.append(random.choice(MonsterPool))
        random.shuffle(self.Rooms)
        self.Rooms.append(Boss)
class SandyShore(Dungeon):
    
    def __init__(self):
        self.MonsterPool = []
        self.EventPool = []
        self.LorePool = []
        self.Rooms = []
        self.Boos = 0
        self.Create(random.randint(0,1),random.randint(0,1),random.randint(2,3),self.EventPool,self.LorePool,self.MonsterPool,self.Boss)