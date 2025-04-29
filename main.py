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
	


	
def deleteTask(id):
	
	try:
		with open(FILE_NAME, "r") as file:
			data = json.load(file)
		data['tareas'] = [task for task in data['tareas'] if task['id'] != int(id)]
		with open(FILE_NAME, "w") as file:
			json.dump(data, file, indent=4)
	except Exception as e:
		print(f"Error saving data to storage updatedata: {e}")




def updateTask(id, newName):
	
	try:
		with open(FILE_NAME, "r") as file:
			data = json.load(file)
		found = False
		for task in data['tareas']:
			if task['id'] == int(id):
				oldName = task['name']
				task['name'] = newName
				found = True 
				break
		if not found:
			print(f"Task with id '{id}' not found.")
			return

		with open(FILE_NAME, "w") as file:
			json.dump(data, file, indent=4)
		print(f"Task '{id}': ' {oldName}' updated to '{newName}'.")
	except Exception as e:
		print(f"Error saving data to storage updatedata: {e}")

def changeState(id, newState):
	try:
		with open(FILE_NAME, "r") as file:
			data = json.load(file)
		found = False
		for task in data['tareas']:
			if task['id'] == int(id):
				task['state'] = newState
				found = True 
				break
		if not found:
			print(f"Task with id '{id}' not found.")
			return

		with open(FILE_NAME, "w") as file:
			json.dump(data, file, indent=4)
		print(f"Task '{id}' marked as '{newState}'.")
	except Exception as e:
		print(f"Error saving data to storage change state: {e}")

	
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
				elif option == "IN-PROGRESS":
					if taskO.state == "IN-PROGRESS":
						print(taskO)
				elif option == "DONE":
					if taskO.state == "DONE":
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
	parser.add_argument("action", choices=["add", "delete", "update","mark-in-progress","mark-done","list"], help="Action to perform")
	parser.add_argument("-v","--value", help="Value for the action", required=False)
	parser.add_argument("-u","--updateValue", help="Value for the action", required=False)



	args = parser.parse_args()
	if args.action == "add":
		task = TASK(getCurrentId(),args.value, "TODO")
		addTask(task)
	if args.action == "update":
		updateTask(args.value, args.updateValue)

	if args.action == "delete":
		deleteTask(args.value)
		print(f"Task '{args.value}' deleted.")
	if args.action == "mark-in-progress":
		changeState(args.value, "IN-PROGRESS")

	if args.action == "mark-done":
		changeState(args.value, "DONE")

	if args.action == "list":
		listTasks(args.value)

	
	# Add your code here



if __name__ == "__main__":
	main()
