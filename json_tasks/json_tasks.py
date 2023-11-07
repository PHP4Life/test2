import json


def read(path):
    with open(path) as file:
        data = json.load(file)
        location = data["location"]
        population = data["population"]
    print(f"Place Name: {location} \n")


def run_task():
    read("futurama.json")


run_task()
