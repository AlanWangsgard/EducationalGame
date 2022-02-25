from pathlib import Path
from db.db_interactor import DB_Interactor as DBI

DIR = str(Path(__file__).resolve().parent)
CERT_FILE_PATH = DIR + "\\" + "cert.json" ##### REPLACE WITH YOUR ADMIN SDK CERT FILENAME.


# Do stuff wth the DBI to test it out