class HabitAction:
  def __init__(self, name, paired_action, action_conversion, reward_time):
    self._name = name
    self._paired_action = paired_action
    self._action_conversion = round(action_conversion, 2)   
    self._reward_time = reward_time

  def set_paired_action(self, new_paired_action):
    self._old_paired_action = self._paired_action
    self._paired_action = new_paired_action
    return f"Paired Action changed from {self._old_paired_action} to {self._paired_action}"

  def set_action_conversion(self, new_action_conversion):
    self._old_action_conversion = self._action_conversion
    self._action_conversion = new_action_conversion
    return f"Action Conversion changed from {self._old_action_conversion} to {self._action_conversion}"

  def add_reward_time(self, habit_time):
    self._new_reward_time = round(habit_time * self._action_conversion, 1)
    self._old_reward_time = self._reward_time
    self._reward_time += self._new_reward_time
    return f"{self._new_reward_time} added to {self._old_reward_time}. New Reward Time: {self._reward_time}"

  def get_name(self):
    return self._name

  def get_paired_action(self):
    return self._paired_action

  def get_action_conversion(self):
    return self._action_conversion

  def get_reward_time(self):
    return self._reward_time
    
    
