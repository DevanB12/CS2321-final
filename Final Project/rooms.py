from commandWords import *
from player import *

class RoomOne(object):

    def __init__(self):
        self._description = open('room1.txt', 'r')
        self._description = self._description.read()
        self._roomInv = []
        self._p = Player()

    def move(self, command):
        if 'north' in command:
            return 3
        elif 'east' in command:
            return 6
        elif 'south' in command:
            return 8
        elif 'west' in command:
            return 5

    def roomDesc(self):
        print('\n' + self._description + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

    def isWinner(self):
        if 'eye' in self._roomInv and 'wing' in self._roomInv and 'toe' in self._roomInv and 'hair' in self._roomInv and 'leg' in self._roomInv:
            winningText = open('WinningText.txt', 'r')
            print(winningText.read())
            return True
        else:
            return False

class RoomTwo(object):

    def __init__(self):
        self._description = open('Room2.txt', 'r')
        self._description = self._description.read()
        self._roomInv = ['eye']
        

    def move(self, command):
        if 'north' in command:
            print('OUCH! I bumped into a wall!')
            return 2
        elif 'east' in command:
            return 3
        elif 'south' in command:
            return 2
        elif 'west' in command:
            return 2

    def roomDesc(self):
        print('\n' + self._description + '\n')
        if 'eye' in self._roomInv:
            temp = open('Room2PreAction.txt', 'r')
            print('\n' + temp.read() + '\n')
        else:
            temp = open('Room2PostAction.txt', 'r')
            print('\n' + temp.read() + '\n')
    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

class RoomThree(object):

    def __init__(self):
        self._description = open('Room3.txt', 'r')
        self._description = self._description.read()
        self._roomInv = []

    def move(self, command):
        if 'north' in command:
            print('OUCH! I bumped into a wall!')
            return 3
        elif 'east' in command:
            return 4
        elif 'south' in command:
            return 1
        elif 'west' in command:
            return 2

    def roomDesc(self):
        print('\n' + self._description + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

class RoomFour(object):

    def __init__(self):
        self._description = open('Room4.txt', 'r')
        self._description = self._description.read()
        self._roomInv = ['leg']

    def move(self, command):
        if 'north' in command:
            print('OUCH! I bumped into a wall!')
            return 4
        elif 'east' in command:
            return 6
        elif 'south' in command:
            return 6
        elif 'west' in command:
            print('The entrance closed up behind me!')
            return 4

    def roomDesc(self):
        print('\n' + self._description + '\n')
        if 'leg' in self._roomInv:
            temp = open('Room4PreAction.txt', 'r')
            print('\n' + temp.read() + '\n')
        else:
            temp = open('Room4PostAction.txt', 'r')
            print('\n' + temp.read() + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item
        
class RoomFive(object):

    def __init__(self):
        self._description = open('Room5.txt', 'r')
        self._description = self._description.read()
        self._roomInv = []

    def move(self, command):
        if 'north' in command:
            print('OUCH! I bumped into a wall!')
            return 5
        elif 'east' in command:
            return 1
        elif 'south' in command:
            print('OUCH! I bumped into a wall!')
            return 5
        elif 'west' in command:
            return 7

    def roomDesc(self):
        print('\n' + self._description + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

class RoomSix(object):

    def __init__(self):
        self._description = open('Room6.txt', 'r')
        self._description = self._description.read()
        self._roomInv = []

    def move(self, command):
        if 'north' in command:
            return 4
        elif 'east' in command:
            return 9
        elif 'south' in command:
            return 8
        elif 'west' in command:
            return 1

    def roomDesc(self):
        print('\n' + self._description + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

class RoomSeven(object):

    def __init__(self):
        self._description = open('Room7.txt', 'r')
        self._description = self._description.read()
        self._roomInv = ['toe']

    def move(self, command):
        if 'north' in command:
            return 2
        elif 'east' in command:
            print('OUCH! I bumped into a wall!')
            return 7
        elif 'south' in command:
            print('OUCH!, I bumped into a wall!')
            return 7
        elif 'west' in command:
            return 5

    def roomDesc(self):
        print('\n' + self._description + '\n')
        if 'toe' in self._roomInv:
            temp = open('Room7PreAction.txt', 'r')
            print('\n' + temp.read() + '\n')
        else:
            temp = open('Room7PostAction.txt', 'r')
            print('\n' + temp.read() + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

class RoomEight(object):

    def __init__(self):
        self._description = open('Room8.txt', 'r')
        self._description = self._description.read()
        self._roomInv = ['wing']

    def move(self, command):
        if 'north' in command:
            print('OUCH! I bumped into a wall!')
            return 8
        elif 'east' in command:
            return 6
        elif 'south' in command:
            print('OUCH! I bumped into a wall!')
            return 8            
        elif 'west' in command:
            return 1

    def roomDesc(self):
        print('\n' + self._description + '\n')
        if 'wing' in self._roomInv:
            temp = open('Room8PreAction.txt', 'r')
            print('\n' + temp.read() + '\n')
        else:
            temp = open('Room8PostAction.txt', 'r')
            print('\n' + temp.read() + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

class RoomNine(object):

    def __init__(self):
        self._description = open('Room9.txt', 'r')
        self._description = self._description.read()
        self._roomInv = []

    def move(self, command):
        if 'north' in command:
            return 6
        elif 'east' in command:
            print('OUCH! I bumped into a wall!')
            return 9
        elif 'south' in command:
            print('OUCH! I bumped into a wall!')
            return 9
        elif 'west' in command:
            return 10

    def roomDesc(self):
        print('\n' + self._description + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item

class RoomTen(object):

    def __init__(self):
        self._description = open('Room10.txt', 'r')
        self._description = self._description.read()
        self._roomInv = ['hair']

    def move(self, command):
        if 'north' in command:
            print('OUCH! I bumped into a wall!')
            return 10
        elif 'east' in command:
            return 9
        elif 'south' in command:
            print('OUCH! I bumped into a wall!')
            return 10
        elif 'west' in command:
            print('OUCH! I bumped into a wall!')
            return 10

    def roomDesc(self):
        print('\n' + self._description + '\n')
        if 'hair' in self._roomInv:
            temp = open('Room10PreAction.txt', 'r')
            print('\n' + temp.read() + '\n')
        else:
            temp = open('Room10PostAction.txt', 'r')
            print('\n' + temp.read() + '\n')

    def take(self):
        if [] == self._roomInv:
            print('There is nothing in this room.')
            return ''
        else:
            a = self._roomInv
            self._roomInv = []
            return a

    def drop(self, item):
        item = [item]
        self._roomInv = self._roomInv + item
