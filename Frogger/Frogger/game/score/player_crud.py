from crud import CrudDB


class PlayerCRUD(CrudDB):
    def __init__(self) -> None:
        super().__init__('players')

player = PlayerCRUD()
print(player.list())