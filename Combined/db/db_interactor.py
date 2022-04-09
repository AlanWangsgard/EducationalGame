# Used to interact with Firebase.
import firebase_admin
from firebase_admin import credentials, firestore

class DB_Interactor():
    # These are the names of my top-level collections in Firestore.
    COLLECTION = u"high_scores"
    DOCUMENT_KEY = u"score"
    __db = None

    def __init__(self, filepath):
        # filepath is the path to the json certificate for firebase.
        assert filepath
        self.__db = self.__get_database_ref(filepath)

    def __get_database_ref(self, filepath):
        # filepath is the path to the json certificate for firebase.
        cred = credentials.Certificate(filepath)
        firebase_admin.initialize_app(cred)
        database = firestore.client()
        return database

    def is_ready(self):
        # If the database reference is set up, then this Interactor is ready.
        return not self.__db == None

    def get_all_scores(self):
        # Gets all score documents in the database in order.
        score_collection = self.__db.collection(self.COLLECTION)
        score_docs = [*score_collection.order_by(u"score").get()]
        if not score_docs:
            print("No scores found")
        score_dicts = []
        for score_doc in score_docs:
            score_dicts = [score_doc.to_dict()["score"]] + score_dicts
        return score_dicts

    def add_score(self, score):
        # Adds a score to the database.
        self.__db.collection(self.COLLECTION).add({self.DOCUMENT_KEY: score})

    def update_scores(self, score):
        # Determine where the user's score fits in to the cloud database and update the cloud scores.
        scores = self.get_all_scores()
        num_high_scores = len(scores)
        scores.append(score)
        scores = sorted(scores, reverse = True)
        for score_index in range(num_high_scores):
            self.__db.collection(self.COLLECTION).document(str(score_index+1)).update({self.DOCUMENT_KEY: scores[score_index]})