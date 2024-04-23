import json
import os

class DataBase:
  def __init__(self, user, db):
    self._user = user
    self._db = db
    self._paired_actions = []

  def save_db(self):
    with open(f"{self._user}.json", "w") as outfile:
      json.dump(self._db, outfile)

    outfile.close()

  def load_db(self, user):
    if os.path.isfile(f"{user}.json") is False:
      return "The File Does Not Exist"
    save_file = open(f"{user}.json", "r")

    db_data = json.load(save_file)

    self._user = user
    self._db = db_data

    save_file.close()

  def add_action_to_db(self, action_name: str, paired_action: str, conversion_rate: float, reward_time: int, reward_time_history: int):
    self._db[action_name] = {"Paired Action" : paired_action, "Action Conversion Rate" : conversion_rate, "Reward Time" : reward_time, "Total Reward Time Earned" : reward_time_history}
    return action_name

  def convert_reward_Time(self, action_name: str, time_spent: int):
    convert = self._db[action_name]["Action Conversion Rate"] * time_spent
    return convert

  def add_reward_time(self, action_name: str, reward_time_add: int):
    self._db[action_name]["Reward Time"] += reward_time_add
    self._db[action_name]["Total Reward Time Earned"] += reward_time_add
    return self._db[action_name]["Reward Time"]

  def use_reward_time(self, action_name: str, reward_time_used: int):
    self._db[action_name]["Reward Time"] -= reward_time_used
    return self._db[action_name]["Reward Time"]
  
  def convert_time_to_hours(self, mins):
    hours = 0

    if -60 > mins < 0:
      hours = mins // 60
      if mins % 60 != 0:
        hours += 1

    if mins > 60:
      hours = mins // 60
    
    mins_remain = mins % 60

    if hours < 0:
      mins_remain = 60 - mins_remain

    return [hours, mins_remain]
    
  def reward_hours_remain(self, action_name):
    hours_list = self.convert_time_to_hours(self._db[action_name]["Reward Time"])

    return f"{hours_list[0]} hours and {hours_list[1]} minutes"
  
  def get_all_time_reward_hours(self, action_name):
    hours_list = self.convert_time_to_hours()

  def print_action_info(self, action_name):

    paired_action = self._db[action_name]["Paired Action"]
    conversion_rate = self._db[action_name]["Action Conversion Rate"]
    total_reward_hours = korachof.convert_time_to_hours(korachof._db[action_name]["Total Reward Time Earned"])
    print_string = f"Action Name: {action_name}"
    print_string += f"\nPaired Action: {paired_action}"
    print_string += f"\nConversion Rate: x{conversion_rate}"
    print_string += f"\nReward Hours Remaining: {korachof.reward_hours_remain(action_name)}"
    print_string += f"\nAll Time Reward Hours Earned: {total_reward_hours[0]} hours and {total_reward_hours[1]} minutes"
    print(print_string)


test_dictionary = {}


test_dictionary["Schoolwork"] = {"Paired Action" : "Video Games", "Action Conversion Rate" : 0.1, "Reward Time" : 0}

korachof = DataBase("Korachof", test_dictionary)

korachof.save_db()

korachof.load_db("Korachof")

korachof.add_action_to_db("Personal Projects", "Video Games", 0.3, 0, 0)

korachof.add_action_to_db("Schoolwork", "Video Games", 2, 0, 0)

korachof.add_action_to_db("Reading", "Phone Time", 2, 0, 0)

converted_time = korachof.convert_reward_Time("Personal Projects", 240)
korachof.add_reward_time("Personal Projects", converted_time)
print(korachof._db["Personal Projects"]["Reward Time"])
korachof.reward_hours_remain("Personal Projects")
korachof.use_reward_time("Personal Projects", 70)
print(korachof._db["Personal Projects"]["Reward Time"])
korachof.reward_hours_remain("Personal Projects")
print(korachof._db["Personal Projects"]["Reward Time"])
korachof.reward_hours_remain("Personal Projects")
korachof.print_action_info("Personal Projects")

save_list = list(korachof._db.keys())

for action in save_list:
  print(action)

for File in os.listdir("."):
    if File.endswith(".json"):
        file_split = File.split(".")
        print(file_split[0])

korachof.save_db()

    
    
      


    
    
  

  
