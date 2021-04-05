from rooms import *

class Player(object):

    def __init__(self):
        self._playerInv = []
        self._score = 0
    

    def addToScore(self):
        self._score += 1

    def displayScore(self):
        print('Your score is ' + str(self._score))

    def addToInv(self, item):
        if item ==  '':
            pass
        else:
            self.addToScore()
            #item = [list]
            self._playerInv = self._playerInv + list(item)

    def removeFromInv(self, item):
        temp = ''
        for i in range(len(self._playerInv)):
            if item == self._playerInv[i]:
                temp = True
                temp2 = i
                break
            else:
                temp = False
        if temp == True:
            self._playerInv.remove(self._playerInv[temp2])
            return True
        else:
            print('That item is not in your inventory.')
            return False
            
    def displayInv(self):
        print('Your inventory: ' + str(self._playerInv))
                
