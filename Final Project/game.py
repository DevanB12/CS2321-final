from commands import *
from commandWords import *
from player import *

class Game():

    def __init__(self):
        self._welcome = open('Enterance.txt', 'r')
        self._welcome = self._welcome.read()
        self._m = Commands()
        
    def play(self):
        print(self._welcome + '\n')
        while True:
            if self._m.isWinner() == True:
                break
            command = input('What would you like to do? ')
            command = command.lower()
            checkCommand = CommandWords(command)
            if checkCommand.checkCommand() == True:
                print('Input a valid command')
            elif 'north' in command or 'south' in command or 'west' in command or 'east' in command:
                self._m.move(command)
                self._m.look()
            elif 'look' == command:
                self._m.look()
            elif 'score' == command:
                self._m.score()
            elif 'take' == command:
                self._m.takeItem()
            elif 'drop' in command:
                item = input('What item would you like to drop?')
                item = item.lower()
                if item == 'frog':
                    item = 'toe'
                self._m.dropItem(item)
            elif 'inventory' == command:
                self._m.inventory()
            elif 'quit' == command:
                break
   
def main():
    g = Game()
    g.play()
    

if __name__ == '__main__':
    main()
