class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return(self.name)


player1 = PlayerCharacter('Christopher')
print(player1.getName())
