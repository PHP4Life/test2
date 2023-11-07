def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def run():
    print(pattern())


def display_keys(data):
    for key in data.keys():
        print("The key is "+key)


def display_values(data):
    for value in data.values():
        print("The value is "+str(value))


def display_items(data):
    for key, value in data.items():
        print(f"The key is: {key}: {value}")


def run_task():
    data = pattern()
    run()
    display_keys(data)
    display_values(data)
    display_items(data)


run_task()
