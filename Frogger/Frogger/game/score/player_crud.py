from crud import CrudDB


class PlayerCRUD(CrudDB):
    def __init__(self) -> None:
        super().__init__('players')

    def addPlayer(self, name):
        try:
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

player = PlayerCRUD()
print(player.list())