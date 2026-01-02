import argparse
import json

parser = argparse.ArgumentParser(prog="tasks",
                                 description="A simple to-do list CLI tool by Kalan Roye. Made in 2026.",
                                 epilog="Thanks for trying %(prog)s! :D")

parser.add_argument("-a", "--add", nargs="+")
parser.add_argument("-p", "--priority")
parser.add_argument("-l", "--list", action="store_true")

args = parser.parse_args()

listTasks = args.list

if listTasks:
    try:
        with open("todos.json", 'r', encoding="utf-8") as file:
            data = json.load(file)
            tasks = data["tasks"]

            print("+++ Your To-do List +++")

            for task in tasks:
                print(f"Task: {task["task"]} | Priority: {task["priority"]}")
            exit(0)
    except:
        print("There was an error opening your to-do list. Does it exist yet?\nTry adding a task with tasks.py -a [task]")
        exit(1)

tasks = args.add
priority = args.priority

if tasks:
    print(f"Adding task(s) '{tasks}' with priority '{priority}'")
    try:
        with open("todos.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"tasks": []}
    
    for task in tasks:
        data["tasks"].append({
            "task": task,
            "priority": priority
        })
    
    with open("todos.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
