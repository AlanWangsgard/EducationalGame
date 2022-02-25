from datetime import datetime
from mimetypes import init
from crud import CrudDB


class GameStateCrud(CrudDB):
    def __init__(self) -> None:
        super().__init__('game_states')
    
    def saveGameState(self, player_id, level, score, lives):
        try:
            player_game_state = self.getGameStateByPlayerId(player_id)
            if player_game_state is None:
                super().insert('(player_id, level, score, lives, date)', f"({player_id}, {level}, {score}, {lives}, '{datetime.now()}')")
            else:
                return self.__updaetGameState(player_id, level, score, lives)
            return True
        except:
            return False

    def __updaetGameState(self, player_id, level, score, lives):
        try:
            super().update(query=f"UPDATE game_states SET level = {level}, score = {score}, lives = {lives}, date = '{datetime.now()}' WHERE player_id = {player_id}")
            return True
        except:
            return False
    
    def getGameStateByPlayerId(self, player_id):
        return super().getById(query=f"SELECT * FROM game_states WHERE player_id = {player_id}")

if __name__ == "__main__":
    gameState = GameStateCrud()
    print(gameState.saveGameState(1, 6, 14000, 20))
    # print(gameState.getGameStateByPlayerId(1))
    print(gameState.list())