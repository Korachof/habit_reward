import json
import os

class DataBase:
  def __init__(self, user, db):
    self._user = user
    self._db = db

  def save_db(self):
    with open(f"{self._user}.json", "w") as outfile:
      json.dump(self._db, outfile)

  def load_db(self, user):
    if os.path.isfile(f"{user}.json") is False:
      return "The File Does Not Exist"
    save_file = open(f"{user}.json", "r")

    db_data = json.load(save_file)

    self._user = user
    self._db = db_data
    
    
      


    
    
  

  
