def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here\n")
        print("File 'my_file.txt' created successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Additional line 1\n")
            file.write("67890\n")
            file.write("One more line added\n")
        print("File 'my_file.txt' appended successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
