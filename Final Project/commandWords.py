class CommandWords(object):

    def __init__(self, command):
        self._command = command
        self._commandList = ['quit', 'take', 'drop', 'hair', 'eye', 'toe', 'frog', 'leg', 'wing', 'inventory', 'look', 'score', 'go', 'move', 'north', 'go north', 'go south', 'go west', 'go east', 'move north', 'move south', 'move east', 'move west', 'south', 'east', 'west']
    def checkCommand(self):
        while True:
            if self._command in self._commandList:
                return False
            else:
                return True
    def getLastCommand(self):
        return self._command

    def newCommand(self):
        self._command = input('What command would you like to do?')
        return self._command
