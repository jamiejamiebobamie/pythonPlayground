

import random

class Dungeon:
    def __init__(self,numberOfRooms=None,numberOfPlayers=0):
        # self.numberOfRooms = numberOfRooms
        self.world = {}
        self.n = 0 # size of world, scales with number of players
        self.players = {}
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
        # first generates a random boolean to declare if the room is transparent or not.
        # if it is transparent, add it to the dictionary of the world
        # solid rooms are not stored to reduce storage
        if x == None or y == None or z == None:
            x = y = z = self.n
        if number == None:
            number = self.numberOfPlayers
        self.n = number
        # print(self.n, number)
        while x < number:
            coordinate = [x,y,z]
            for coord in self.permute(coordinate):
                if bool(random.getrandbits(1)):
                    self.world[coord] = self.Room(coord[0], coord[1], coord[2])
            x+=1
        else:
            while y < number:
                coordinate = [x,y,z]
                for coord in self.permute(coordinate):
                    if bool(random.getrandbits(1)):
                        self.world[coord] = self.Room(coord[0], coord[1], coord[2])
                y+=1
            else:
                while z < number:
                    coordinate = [x,y,z]
                    for coord in self.permute(coordinate):
                        if bool(random.getrandbits(1)):
                            self.world[coord] = self.Room(coord[0], coord[1], coord[2])
                    z+=1
                else:
                    coordinate = [x,y,z]
                    for coord in self.permute(coordinate):
                        if bool(random.getrandbits(1)):
                            self.world[coord] = self.Room(coord[0], coord[1], coord[2])

    def addPlayers(self, n=None, name=None, adventurerType=None, background=None):
        if n == None:
            n = 1
        for _ in range(n):
            self.players[self.n+_] = self.Player(name,adventurerType,background, self.world[0,0,0])
        self.numberOfPlayers += n
        #addRooms() modifies the self.n and self.numberOfPlayers and must be called after instantiating the correct number of players
        # in this function
        self.addRooms()

    def testMove(self, player, direction):
        test = player.move(direction)
        test = tuple(test)
        # print(test)
        if test in self.world:
            player.room = self.world[test]
            self.world[test].setDescription()
            return "You moved " + direction + "."
        else:
            return "There is nothing that way."


    class Room:
        def __init__(self, x, y, z, description=None):
            self.x=x
            self.y=y
            self.z=z
            self.coordinate = [x,y,z]
            self.description = None
            self.players = {}
            self.items = {}
            self.monsters = {}


        def setDescription(self, userInput=None):
            if self.description == None:
                self.description == userInput
                # print("it worked.")
            else:
                print(self.description)


    class Player:
        def __init__(self, name, adventurerType, background, room):
            self.name = name
            self.type = adventurerType
            self.background = background
            self.friends = {}
            self.room = room
            self.dialog = None#LinkedList() #need to make.

        def move(self, direction):
            direction_lookup = {"north":[0,1,0], "south":[0,-1,0], "east":[1,0,0], "west":[-1,0,0], "up":[0,0,1], "down":[0,0,-1]}
            test = direction_lookup[direction]
            for i, item in enumerate(self.room.coordinate):
                test[i] += item
            return test

        def tell(self):
            pass

        def speak(self, player):
            pass

        def yell(self):
            pass

    class Item:
        def __init__(self, name, description):
            self.name = name
            self.description = description

    class Monster:
        def __init__(self, name, description):
            self.name = name
            self.description = description



newDungeon = Dungeon()
newDungeon.addPlayers(5)
# print(len(newDungeon.world.keys()))
# for key in newDungeon.world.keys():
#     print(key)
# for player in newDungeon.players.keys():
#     print(player)

# for player in newDungeon.players:
#     print(newDungeon.players[player].room.coordinate)

# for room in newDungeon.world:
#     print(room)

# print(newDungeon.players[0].move("west"))
print(newDungeon.testMove(newDungeon.players[0],"east"))
