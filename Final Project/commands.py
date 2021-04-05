from commandWords import *
from rooms import *
from player import *

class Commands(object):

    def __init__(self):
        self._r1 = RoomOne()
        self._r2 = RoomTwo()
        self._r3 = RoomThree()
        self._r4 = RoomFour()
        self._r5 = RoomFive()
        self._r6 = RoomSix()
        self._r7 = RoomSeven()
        self._r8 = RoomEight()
        self._r9 = RoomNine()
        self._r10 = RoomTen()
        self._current = 1
        self._p = Player()

    def move(self, command):
        self._p.addToScore()
        if self._current == 1:
            self._current = self._r1.move(command)
            return self._current
        elif self._current == 2:
            self._current = self._r2.move(command)
            return self._current
        elif self._current == 3:
            self._current = self._r3.move(command)
            return self._current
        elif self._current == 4:
            self._current = self._r4.move(command)
            return self._current
        elif self._current == 5:
            self._current = self._r5.move(command)
            return self._current
        elif self._current == 6:
            self._current = self._r6.move(command)
            return self._current
        elif self._current == 7:
            self._current = self._r7.move(command)
            return self._current
        elif self._current == 8:
            self._current = self._r8.move(command)
            return self._current
        elif self._current == 9:
            self._current = self._r9.move(command)
            return self._current
        elif self._current == 10:
            self._current = self._r10.move(command)
            return self._current

    def look(self):
        if self._current == 1:
            self._r1.roomDesc()
        elif self._current == 2:
            self._r2.roomDesc()
        elif self._current == 3:
            self._r3.roomDesc()
        elif self._current == 4:
            self._r4.roomDesc()
        elif self._current == 5:
            self._r5.roomDesc()
        elif self._current == 6:
            self._r6.roomDesc()
        elif self._current == 7:
            self._r7.roomDesc()
        elif self._current == 8:
            self._r8.roomDesc()
        elif self._current == 9:
            self._r9.roomDesc()
        elif self._current == 10:
            self._r10.roomDesc()

    def score(self):
         self._p.displayScore()

    def takeItem(self):
        if self._current == 1:
            self._p.addToInv(self._r1.take())
        elif self._current == 2:
            self._p.addToInv(self._r2.take())
            postAction = open('Room2PostAction.txt', 'r')
            print('\n' + postAction.read() + '\n')
        elif self._current == 3:
            self._p.addToInv(self._r3.take())
        elif self._current == 4:
            self._p.addToInv(self._r4.take())
            postAction = open('Room4PostAction.txt', 'r')
            print('\n' + postAction.read() + '\n')
        elif self._current == 5:
            self._p.addToInv(self._r5.take())
        elif self._current == 6:
            self._p.addToInv(self._r6.take())
        elif self._current == 7:
            self._p.addToInv(self._r7.take())
            postAction = open('Room7PostAction.txt', 'r')
            print('\n' + postAction.read() + '\n')
        elif self._current == 8:
            self._p.addToInv(self._r8.take())
            postAction = open('Room8PostAction.txt', 'r')
            print('\n' + postAction.read() + '\n')
        elif self._current == 9:
            self._p.addToInv(self._r9.take())
        elif self._current == 10:
            self._p.addToInv(self._r10.take())
            postAction = open('Room10PostAction.txt', 'r')
            print('\n' + postAction.read() + '\n')


    def dropItem(self, item):
        if self._current == 1:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r1.drop(item)
        elif self._current == 2:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r2.drop(item)
        elif self._current == 3:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r3.drop(item)
        elif self._current == 4:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r4.drop(item)
        elif self._current == 5:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r5.drop(item)
        elif self._current == 6:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r6.drop(item)
        elif self._current == 7:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r7.drop(item)
        elif self._current == 8:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r8.drop(item)
        elif self._current == 9:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r9.drop(item)
        elif self._current == 10:
            temp = self._p.removeFromInv(item)
            if temp == True:
                self._r10.drop(item)

    def inventory(self):
        self._p.displayInv()

    def isWinner(self):
        if self._r1.isWinner() == True:
            return True


def main():
    m = Movement()
    m.move()


if __name__ == '__main__':
    main()
