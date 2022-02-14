from datetime import datetime
from mimetypes import init
from crud import CrudDB


class GameStateCrud(CrudDB):
    def __init__(self) -> None:
        super().__init__('game_states')
    
    def saveGameState(self, player_id, level, score, lives):
        try:
            super().insert('(player_id, level, score, lives, date)', f"({player_id}, {level}, {score}, {lives}, '{datetime.now()}')")
            return True
        except:
            return False

gameState = GameStateCrud()
# gameState.saveGameState(3, 2, 5000, 4)
print(gameState.list())