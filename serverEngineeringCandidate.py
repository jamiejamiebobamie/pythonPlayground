

import random

class Dungeon:
    def __init__(self,numberOfRooms=None,numberOfPlayers=1):
        # self.numberOfRooms = numberOfRooms
        self.world = {}
        self.n = 0
        self.numberOfPlayers = numberOfPlayers
        self.addRooms(numberOfRooms)

    def permute(self, a):
        array = a
        permutations = set()
        def __helper(a, l, r):
            if l==r:
                perm = tuple(a)
                permutations.add(perm)
            else:
                for i in xrange(l,r+1):
                    a[l], a[i] = a[i], a[l]
                    __helper(a, l+1, r)
                    a[l], a[i] = a[i], a[l]
            return permutations
        return __helper(array, 0, 2)

    def addRooms(self, number=None, x=None, y=None, z=None):
        # builds out the world space creating 3d coordinates in a number x number x number block
        if x == None or y == None or z == None:
            x = y = z = self.n
        if number == None:
            number = self.numberOfPlayers
        self.n = number
        while x < number:
            coordinate = [x,y,z]
            for coord in self.permute(coordinate):
                self.world[coord] = self.Room(coord[0], coord[1], coord[2], bool(random.getrandbits(1)))
            x+=1
        else:
            while y < number:
                coordinate = [x,y,z]
                for coord in self.permute(coordinate):
                    self.world[coord] = self.Room(coord[0], coord[1], coord[2], bool(random.getrandbits(1)))
                y+=1
            else:
                while z < number:
                    coordinate = [x,y,z]
                    for coord in self.permute(coordinate):
                        self.world[coord] = self.Room(coord[0], coord[1], coord[2], bool(random.getrandbits(1)))
                    z+=1
                else:
                    coordinate = [x,y,z]
                    for coord in self.permute(coordinate):
                        self.world[coord] = self.Room(coord[0], coord[1], coord[2], bool(random.getrandbits(1)))

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
            self.dialogue = None#LinkedList() #need to make.

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

newDungeon = Dungeon(None, 1)
print(len(newDungeon.world.keys()))
for key in newDungeon.world.keys():
    print(key)
