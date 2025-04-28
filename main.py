import sys
from Task import TASK
import argparse
import json
import os

INITIAL_DATA = {'tareas': []}
FILE_NAME = "tareasStorage.json"

def saveToJson(task:TASK):
	"""
	Save the task to a JSON file.

	Args:
		task (TASK): The task to be saved.
	"""

	try:
		#verify if the file exists 
		if not os.path.exists("tareasStorage.json"):
			print("File does not exist, creating a new one")
			with open(FILE_NAME, "w") as file:
				json.dump(INITIAL_DATA, file)
		with open(FILE_NAME, "r") as file:
			data = json.load(file)
		data['tareas'].append(task.__dict__())
		with open(FILE_NAME, "w") as file:
			print(data)
			json.dump(data, file, indent=4)
		print(f"Task '{task.name}' saved to {FILE_NAME}.")
	except Exception as e:
		print(f"Error saving data to storage saveToJson: {e}")

		
	


def addTask(task:TASK):
	"""
	Add a task to the list of tasks.

	Args:
		task (TASK): The task to be added.
	"""
	saveToJson(task)
	print(f"Task '{task.name}' added.")
	


	
def deleteTask(task):
	print(f"Task '{task}' deleted.")
def updateTask(old, newTask):
	print(f"Task '{old}' updated to '{newTask}'.")
def markInProgress(task):
	print(f"Task '{task}' marked as in progress.")
def markDone(task):
	print(f"Task '{task}' marked as done.")
def listTasks(option):
	print("Listing all tasks ")
	try:
		with open(FILE_NAME, "r") as file:
			data = json.load(file)
			for task in data['tareas']:

				taskO = TASK()
				taskO.parseFromDict(task)
				if not option:
					print(taskO)
				elif option == "TODO":
					if taskO.state == "TODO":
						print(taskO)
				else:
					print(f"Error: Invalid state '{option}'.")
					break
					

	except Exception as e:
		print(f"Error loading data from storage listTask: {e}")
	
	
def getCurrentId():
	try:
		with open(FILE_NAME, "r") as file:
			data = json.load(file)
		tareas = data['tareas']
		return  tareas[-1]['id']+1 if len(tareas) >0 else 1
	except Exception as e:
		print(f"Error loading data from storage getCurrentID: {e}")


def main():
	parser = argparse.ArgumentParser(description="Task Manager")
	parser.add_argument("action", choices=["add", "delete", "update","list"], help="Action to perform")
	parser.add_argument("-v","--value", help="Value for the action", required=False)
	parser.add_argument("-u","--updateValue", help="Value for the action", required=False)



	args = parser.parse_args()
	if args.action == "add":
		task = TASK(getCurrentId(),args.value, "TODO")
		addTask(task)
		

	if args.action == "list":
		listTasks(args.value)


	print("Hello, World!")
	# Add your code here



if __name__ == "__main__":
	main()
