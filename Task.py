class TASK :
	def __init__(self, id=-1, name='', state='TODO'):
		self.id = id
		self.name = name
		self.state = state
	def parseFromDict(self, task):
		"""
		Initialize a Task object with the given task dictionary.

		Args:
			task (dict): A dictionary containing task attributes.
		"""
		self.id = task.get("id")
		self.name = task.get("name")
		self.state = task.get("state")


	def __repr__(self):
		"""
		Provide a string representation of the Task object.

		Returns:
			str: A string in the format "TASK(id, name, description)" where
				 `id`, `name`, and `description` are the attributes of the Task object.
		"""
		return f"TASK({self.id}, {self.name}, {self.state})"

	def __str__(self):
		"""
		Returns a string representation of the Task object.

		The string includes the task's ID, name, and description in a formatted manner.

		Returns:
			str: A formatted string containing the task's ID, name, and description.
		"""
		return f"Task ID: {self.id}, Name: {self.name}, State: {self.state}"
	

	def __dict__(self):
		"""
		Returns a dictionary representation of the Task object.

		The dictionary includes the task's ID, name, description, and state.

		Returns:
			dict: A dictionary containing the task's attributes.
		"""
		return {
			"id": self.id,
			"name": self.name,
			"state": self.state
		}
	