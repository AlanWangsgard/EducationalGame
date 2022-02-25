from score.crud import CrudDB


class ScoreCrud(CrudDB):
    def __init__(self) -> None:
        super().__init__('scores')

    def addScore(self, player_id, score):
        try:
            super().insert('(player_id, score)', f"({player_id}, {score})")
            return True
        except:
            return False
    
    def updateScore(self, id, score):
        try:
            super().update(id, 'score', score)
            return True
        except:
            return False
if __name__ == "__main__":
    score = ScoreCrud()
    # score.updateScore(1, 3500)
    print(score.list())