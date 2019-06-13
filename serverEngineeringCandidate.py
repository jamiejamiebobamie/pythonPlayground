

import random

class Dungeon:
    def __init__(self,numberOfRooms):
        self.numberOfRooms = numberOfRooms
        self.world = {}
        # self.world[(0,0,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
        self.nextRoomCoordinate = [1,0] # first item is the coordinate value, the second item denotes xyz (x=0,y=1,z=2)
        self.current_coordinate = [0,0,0]
        # self.instantiateDungeon()

    def instantiateDungeon(self):
        for n in range(self.numberOfRooms):
            self.world[(n,0,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(0,n,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(0,0,n)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(n,n,0)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(0,n,n)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))
            self.world[(n,n,n)] = self.Room(0, 0, 0, bool(random.getrandbits(1)))


    def addRooms(self):
        # add an xyz room coordinate and its positive/negative variations.
        print(self.current_coordinate)
        if self.nextRoomCoordinate[1] > 1:
            self.nextRoomCoordinate[0] = 0
            self.nextRoomCoordinate[1] = 0
        else:
            self.nextRoomCoordinate[1] += 1
        # print(self.nextRoomCoordinate)
        self.current_coordinate[self.nextRoomCoordinate[1]] = self.nextRoomCoordinate[0]


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
            self.dialogue = LinkedList() #need to make.

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

# print(len(newDungeon.world.keys()))
# for key in newDungeon.world.keys():
#     print(key)

for _ in range(50):
    newDungeon.addTwoRooms()

#what room coordinates from -2 to 2 of unit size 1 look like:
#
# (0,0,0)
#
# (0,0,1)
# (0,0,-1)
#
# (0,1,0)
# (0,-1,0)
#
# (1,0,0)
# (-1,0,0)
#
# (0,1,1)
# (0,-1,-1)
# (0,-1,1)
# (0,1,-1)
#
# (1,1,0)
# (-1,-1,0)
# (1,-1,0)
# (-1,1,0)
#
# (1,0,1)
# (-1,0,1)
# (1,0,-1)
# (-1,0,-1)
#
# (1,1,1)
# (-1,1,1)
# (1,-1,1)
# (1,1,-1)
# (1,-1,-1)
# (-1,-1,1)
# (-1,1,-1)
# (-1,-1,-1)
#
# (0,0,2)
# (0,0,-2)
#
# (0,1,2)
# (0,1,-2)
# (0,-1,2)
# (0,-1,-2)
#
# (1,0,2)
# (1,0,-2)
# (-1,0,2)
# (-1,0,-2)
#
# (1,1,2)
# (1,1,-2)
# (1,-1,2)
# (-1,1,2)
# (1,-1,-2)
# (-1,-1,2)
# (-1,1,-2)
# (-1,-1,-2)
#
# (2,0,0)
# (-2,0,0)
#
# (2,1,0)
# (-2,1,0)
# (2,-1,0)
# (-2,-1,0)
#
# (2,0,1)
# (2,0,-1)
# (-2,0,1)
# (-2,0,-1)
#
# (0,2,0)
# (0,-2,0)
#
# (1,2,0)
# (-1,2,0)
# (1,-2,0)
# (-1,-2,0)
#
# (0,2,1)
# (0,-2,1)
# (0,2,-1)
# (0,-2,-1)
#
# (1,2,1)
# (-1,2,1)
# (1,-2,1)
# (1,2,-1)
# (-1,-2,1)
# (1,-2,-1)
# (-1,-2,-1)
#
# (2,1,1)
# (-2,1,1)
# (2,-1,1)
# (2,1,-1)
# (2,-1,-1)
# (-2,-1,1)
# (-2,-1,-1)
# (-2,1,1-)
#
# (2,2,1)
# (-2,2,1)
# (2,-2,1)
# (2,2,-1)
# (-2,-2,1)
# (2,-2,-1)
# (-2,2,-1)
# (-2,-2,-1)
#
# (2,2,2)
# (2,2,-2)
# (2,-2,2)
# (-2,2,2)
# (2,-2,-2)
# (-2,-2,2)
# (-2,2,-2)
# (-2,-2,-2)
