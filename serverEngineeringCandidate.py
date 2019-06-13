

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
        # solid rooms are not stored.
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
            new_player = self.Player(name,adventurerType,background, self.world[0,0,0])
            self.players[self.n+_] = new_player
            self.world[0,0,0].players[self.n+_] = new_player
        self.numberOfPlayers += n
        #addRooms() modifies the self.n and self.numberOfPlayers and must be called after instantiating the correct number of players
        # in this function
        self.addRooms()

    def testMove(self, player, direction):
        test = player.move(direction)
        test = tuple(test)
        # print(test)
        if test in self.world:
            for room_occupants in self.world[test].players:
                if player == room_occupants:
                    del self.world[test].players[room_occupants]
            player.room = self.world[test]
            # self.world[test].players[player] =
            self.world[test].setDescription()
            return "You moved " + direction + "."
        else:
            return "There is nothing that way."

    def whereMove(self, player):
        directions = ["north","south","east","west","up","down"]
        moves = []
        for direction in directions:
            test = player.move(direction)
            test = tuple(test)
            if test in self.world:
                moves.append("You can move " + direction + ".")
        return moves

    def addYells(self, yeller, content):
        for player in self.world:
            if player.quietMode == False:
                player.DialogList.addNode(content)

    def addTell(self, player, content):
        if player in self.world:
            self.world[player].DialogList.addNode(content)

    class Room:
        def __init__(self, x, y, z, description=None):
            self.x=x
            self.y=y
            self.z=z
            self.coordinate = [x,y,z]
            self.description = None
            self.players = {} # need to update upon player instantiation and on player.move()
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
            self.dialog = self.DialogList()
            self.quietMode = False

        def move(self, direction):
            direction_lookup = {"north":[0,1,0], "south":[0,-1,0], "east":[1,0,0], "west":[-1,0,0], "up":[0,0,1], "down":[0,0,-1]}
            # direction = tuple(direction)
            test = direction_lookup[direction]
            for i, item in enumerate(self.room.coordinate):
                test[i] += item
            return test

        def say(self, content):
            for player in self.room.players:
                self.room.players[player].dialog.addNode(content, self)

        # def tell(self, player, content):
        #     return player, content

        # def yell(self, content):
        #     return content

        class DialogList:
            def __init__(self, head=None, tail=None, maxNodes=5):
                self.head = head
                self.tail = tail
                self.numberOfNodes = 0
                self.maxNodes = maxNodes

            class DialogNode:
                def __init__(self, content="", player=None):
                    self.previous = None
                    self.next = None
                    self.content = content
                    self.speaker = player

            def addNode(self, content, speaker):
                new_node = self.DialogNode(content, speaker)
                self.numberOfNodes += 1
                if self.numberOfNodes > self.maxNodes:
                    self.head = self.head.next
                    self.head.previous = None
                if self.head == None:
                    self.head = self.tail = new_node
                self.tail.next = new_node
                self.tail = new_node

            def showDialog(self):
                content = []
                node = self.head
                while node:
                    content.append(node.content)
                    node = node.next
                return content

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

print(newDungeon.players[0].move("west"))
# print(newDungeon.players[0].room.players)
# newDungeon.players[0].say("1!")
# newDungeon.players[0].say("2!")
# newDungeon.players[0].say("3!")
# newDungeon.players[0].say("4!")
# newDungeon.players[0].say("5!")
# newDungeon.players[0].say("6!")
# newDungeon.players[0].say("7!")
# newDungeon.players[0].say("8!")
# newDungeon.players[0].say("9!")
# newDungeon.players[0].say("10!")
# print(newDungeon.players[0].dialog.showDialog())
# print(newDungeon.players[1].dialog.showDialog())
for _ in range(100):
    print(newDungeon.testMove(newDungeon.players[0],newDungeon.players[0].move("west")))
    print(newDungeon.testMove(newDungeon.players[0],newDungeon.players[0].move("east")))
    print(newDungeon.testMove(newDungeon.players[0],newDungeon.players[0].move("north")))
    print(newDungeon.testMove(newDungeon.players[0],newDungeon.players[0].move("south")))
    print(newDungeon.testMove(newDungeon.players[0],newDungeon.players[0].move("up")))
    print(newDungeon.testMove(newDungeon.players[0],newDungeon.players[0].move("down")))


# print(newDungeon.whereMove(newDungeon.players[1]))
