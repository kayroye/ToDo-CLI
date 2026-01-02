import argparse

parser = argparse.ArgumentParser(prog="tasks")

parser.add_argument("add")
parser.add_argument("-p", "--priority")

args = parser.parse_args()

task = args.add
priority = args.priority

print(f"Adding task '{task}' with priority '{priority}'")