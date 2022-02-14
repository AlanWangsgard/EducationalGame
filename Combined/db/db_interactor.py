# Used to interact with Firebase.
import firebase_admin
from firebase_admin import credentials, firestore
# Get current directory. Helps for file access.
from pathlib import Path
# Gets the current directory
DIR = str(Path(__file__).resolve().parent)

class DB_Interactor():
    # These are the names of my top-level collections in Firestore.
    COLLECTION = u"high_scores"
    DOCUMENT_KEY = u"score"
    __db = None

    def __init__(self, filepath):
        # filepath is the path to the json certificate for firebase.
        assert filepath
        self.__db = self.get_database_ref(filepath)

    def get_database_ref(self, filepath):
        # filepath is the path to the json certificate for firebase.
        cred = credentials.Certificate(filepath)
        firebase_admin.initialize_app(cred)
        database = firestore.client()
        return database

    def is_ready(self):
        # If the database reference is set up, then this Interactor is ready.
        return not self.__db == None

    def display_doc_list(self, doc_list):
        # Tries to print a list of docs prettily.
        dict_list = [doc.to_dict() for doc in doc_list]
        if not dict_list:
            print("No songs found")
        else:
            # Print header
            print("Score:")
            # Print all the scores
            for entry in dict_list:
                print("\t", entry[self.DOCUMENT_KEY])

    def get_all_scores(self, display = False):
        # Gets all song documents in the database, in alphabetical order.
        score_collection = self.__db.collection(self.COLLECTION)
        score_docs = [*score_collection.order_by(u"score").get()]
        if not score_docs:
            print("No songs found")
        elif display:
            self.display_doc_list(score_docs)
        return score_docs

    def add_score(self, score):
        # Adds a score to the database.
        self.__db.collection(self.COLLECTION).add({self.DOCUMENT_KEY: score})

    def update_scores(self, score):
        # Determine where the user's score fits in to the cloud database and update the cloud scores.
        # Process:
        #   Get all the scores from the database and store them in a list.
        #   Add the user's score to the list.
        #   Sort the list highest to lowest.
        #   FOR THE TOP 5 SCORES ONLY:
        #       update document 1 with the highest score.
        #       update document 2 with the second highest score.
        #       Update doc 3 w 3rd, doc 4 w 4th, and doc 5 w 5th.
        #   End

        # This line of code gets a document and updates the score. Put it in a loop.
        self.__db.collection(self.COLLECTION).document(document_id_should_be_1_to_5).update({self.DOCUMENT_KEY: score_it_should_be})