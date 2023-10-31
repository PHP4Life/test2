# Week 6 -  csv Files

def export(path, num_items):
    print("Exporting...")
    with open(path, "a") as file:
        for count in range(num_items):
            item_id = int(input("Please enter the item id: "))
            item_name = input("Please enter the item name: ")
            item_colour = input("Please enter the item colour: ")

            data = f"{item_id},{item_name},{item_colour}\n"
            file.write(data)
    print("Done!")


def run_program():
    item_input = int(input("Enter how many items you want to input: "))
    export("items/exported_items.csv", item_input)


run_program()
