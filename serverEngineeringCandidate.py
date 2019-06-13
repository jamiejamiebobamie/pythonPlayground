

import random

class Dungeon:
    def __init__(self,numberOfRooms):
        self.numberOfRooms = numberOfRooms
        self.world = {}
        self.world[(0,0,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
        self.nextRoomCoordinate = [1,0,0]
        self.instantiateDungeon()

    def instantiateDungeon(self):
        for n in range(self.numberOfRooms):
            self.world[(n,0,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(0,n,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(0,0,n)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(n,n,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(0,n,n)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(n,n,n)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))


    def addRoom(self):


    class Room:
        def __init__(self, x, y, z, transparent,description=None):
            self.x=x
            self.y=y
            self.z=z
            self.transparent = transparent
            self.description = None
            self.players = {}
            self.items = {}
            self.monsters = {}

        def setDescription(self, userInput):
            if self.transparent == True and self.description == None:
                self.description == userInput

    class Player:
        def __init__(self, name, adventurerType, background):
            self.name = name
            self.type = adventurerType
            self.background = background

    class Item:
        def __init__(self, name, description):
            self.name = name
            self.description = description

    class Monster:
        def __init__(self, name, description):
            self.name = name
            self.description = description

newDungeon = Dungeon(7)

print(len(newDungeon.world.keys()))
for key in newDungeon.world.keys():
    print(key)
