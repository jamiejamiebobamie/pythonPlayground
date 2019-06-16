import random

class Dungeon:
    def __init__(self, numberOfPlayers=1):
        self.world = {}
        self.players = {}

        self.n = 0 # size of world, scales with number of players
        self.numberOfPlayers = numberOfPlayers
        self.playerSpawn = (self.n, self.n, self.n)
        self.playerSpawn = (7,7,7)
        self.addRooms(numberOfPlayers)

    def permute(self, a):
        # takes in an array of x,y,z coordinates
        # returns a set of all the unique permutations of that array's items.
        array = a
        permutations = set()
        def __helper(a, l, r):
            if l==r:
                perm = tuple(a)
                permutations.add(perm)
            else:
                for i in range(l,r+1):
                    a[l], a[i] = a[i], a[l]
                    __helper(a, l+1, r)
                    a[l], a[i] = a[i], a[l]
            return permutations
        return __helper(array, 0, 2)


# BROKEN
    def addRooms(self, number=None, x=None, y=None, z=None):
        # builds out the world space creating 3d coordinates in a number by number by number block
        # first generates a random boolean to declare if the room is transparent or not.
        # if it is transparent, add it to the dictionary of the world
        # solid rooms are not stored.
        if x == None or y == None or z == None:
            x = y = z = self.n # set the starting coordinate
        if number == None:
            number = self.numberOfPlayers # set the number to iterate to
        self.n += number # set the new starting coordinate for next time.
        while x < number: # iterate from the starting coordinate to the iteration number for x
            coordinate = [x,y,z]
            for coord in self.permute(coordinate):
                # if bool(random.getrandbits(1)) or coord == list(self.playerSpawn):
                print(coord)
                self.world[coord] = self.Room(coord[0], coord[1], coord[2])
            x+=1
        # else:
            while y < number:
                coordinate = [x,y,z]
                for coord in self.permute(coordinate):
                    # if bool(random.getrandbits(1)) or coord == list(self.playerSpawn):
                    print(coord)
                    self.world[coord] = self.Room(coord[0], coord[1], coord[2])
                y+=1
            # else:
                while z < number:
                    coordinate = [x,y,z]
                    for coord in self.permute(coordinate):
                        # if bool(random.getrandbits(1)) or coord == list(self.playerSpawn):
                        print(coord)
                        self.world[coord] = self.Room(coord[0], coord[1], coord[2])
                    z+=1
                else:
                    coordinate = [x,y,z]
                    for coord in self.permute(coordinate):
                        # if bool(random.getrandbits(1)) or coord == list(self.playerSpawn):
                        print(coord)
                        self.world[coord] = self.Room(coord[0], coord[1], coord[2])
        # self.n = self.numberOfPlayers
        # self.playerSpawn = (self.n, self.n, self.n)

    def addPlayers(self, n=None, name=None, adventurerType=None, background=None):
        if n == None:
            n = 1
        for _ in range(n):
            new_player = self.Player(self.numberOfPlayers+_, name,adventurerType,background, self.world[self.playerSpawn])
            self.players[self.numberOfPlayers+_] = new_player
            self.world[self.playerSpawn].players[self.numberOfPlayers+_] = new_player
        self.numberOfPlayers += n
        self.addRooms()

    def testMove(self, player, direction):
        test = player.move(direction)
        test = tuple(test)
        if test in self.world:
            for room_occupant in player.room.players:
                if player.index == room_occupant:
                    # print(player.index)
                    del player.room.players[room_occupant]
                    break
            player.room = self.world[test]
            self.world[test].setDescription()
            self.world[test].players[player.index] = player
            return "You move " + direction + "."
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

    def addSays(self, content, speaker):
        for player in speaker.room.players:
            self.players[player].dialog.addNode(content, speaker)

    def addYells(self, content, speaker):
        for player in self.players:
            if self.players[player].quietMode == False:
                self.players[player].dialog.addNode(content,speaker)

    def addTell(self, content, listener, speaker):
        if listener in self.players:
            self.players[listener].dialog.addNode(content, speaker)

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
            else:
                print(self.description)

    class Player:
        def __init__(self, index, name, adventurerType, background, room):
            self.index = index
            self.name = name
            self.type = adventurerType
            self.background = background
            self.friends = {}
            self.room = room
            self.dialog = self.DialogList()
            self.quietMode = False

        def move(self, direction):
            direction_lookup = {"north":[0,1,0], "south":[0,-1,0], "east":[1,0,0], "west":[-1,0,0], "up":[0,0,1], "down":[0,0,-1]}
            test = direction_lookup[direction]
            for i, item in enumerate(self.room.coordinate):
                test[i] += item
            return test

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
                self.tail.next = None

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

newDungeon = Dungeon(10)
# newDungeon.addPlayers(10)

print(len(newDungeon.world)) # == 110, should be 1000 

for player in newDungeon.players:
    print(newDungeon.players[player].room.coordinate)
