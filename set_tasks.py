# Week 7 - Sets & Dictionaries

# Task 1 - Sorting Sets

def observed_items():
    observations = []
    for count in range(5):
        print("Please enter an observation: ")
        observations.append(input())
    return observations


def remove_observations(obs_list):
    running = True

    while running:
        remove = input("Do you wish to remove an observation? (y/n): ")

        if remove == "y":
            obs = input("Please enter what you wish to remove? ")
            obs_list.remove(obs)
        else:
            running = False


def run_task3():
    observations = observed_items()
    remove_observations(observations)
    observations_set = set()

    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)

    for data in sorted(observations_set):
        print(f"{data[0]} observed {data[1]} times.")


run_task3()
