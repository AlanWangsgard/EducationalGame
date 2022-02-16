from crud import CrudDB


class PlayerCRUD(CrudDB):
    def __init__(self) -> None:
        super().__init__('players')

    def addPlayer(self, name):
        try:
            player = self.getPlayerByName(name)
            if player is not None:
                print('Player not added because there is already a player with the same name.')
                return
            super().insert('(name)', f"('{name}')")
            return True
        except:
            return False

    def updatePlayerName(self, id, newName):
        try:
            super().update(id, 'name', f"'{newName}'")
            return True
        except:
            return False
    
    def getPlayerByName(self, name):
        return super().getByField('name', f"'{name}'")

player = PlayerCRUD()
player.addPlayer('Daniell')