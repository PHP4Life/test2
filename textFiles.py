# Week 6 -  txt Files

# Task 1 - Book sorting program
def search_books(path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    with open(path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("Done!")

    return f"{sections}\n\n{books}"


def save_books(path, data):
    print("Saving...")
    with open(path, "w") as file:
        file.write(data)
    print("Done!")


def run_program():
    data = search_books("library/books.txt")
    save_books("library/exported_books", data)


run_program()
