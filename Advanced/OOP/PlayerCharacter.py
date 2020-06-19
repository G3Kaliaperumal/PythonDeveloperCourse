class PlayerCharacter:
    def __init__(self, name):
        self._name = name

    def getName(self):
        return(self._name)


class HK47(PlayerCharacter):
    def __init__(self, name, game):
        super().__init__(name)
        self._game = game

    def getGame(self):
        return(self._game)

    def printInfo(self):
        print(f'{super().getName()} got introduced in the game {self._game}')


player1 = PlayerCharacter('Christopher')
print(player1.getName())

killer_bot = HK47('Killerbot', 'Star Wars: Knights of the Old Republic')
killer_bot.printInfo()
