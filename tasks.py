import argparse

parser = argparse.ArgumentParser(prog="tasks")

parser.add_argument("add")
parser.add_argument("-p", "--priority")

args = parser.parse_args()

item = args.add

print(f"Adding {item}...\nDone!")