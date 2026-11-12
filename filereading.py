import json
import os

# with open("notes.txt", "w", encoding="utf-8") as f:
#     f.write("I am learning Python\n")
#     f.write("I am learning file handling\n")
#     f.write("I want to become an AI engineer\n")
    
# with open("notes.txt","a",encoding="utf-8") as f:
#     text =f.write(" baisvb sb bibsc")
# print(text)

# data ={
#     "Python":2,
#     "love":1
# }

# with open("data.json",'w', encoding="utf-8") as f:
#     json.dump(data,f,indent=2)
# with open("data.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)

# print(loaded)


# # Exercise 1: Write three lines to a file using "w"

# with open("test.txt", "w", encoding="utf-8") as f:
#     f.write("First line\n")
#     f.write("Second line\n")
#     f.write("Third line\n")

# print("Three lines written successfully!")


# # Exercise 1 (continued): Append three more lines using "a"

# with open("test.txt", "a", encoding="utf-8") as f:
#     f.write("Fourth line\n")
#     f.write("Fifth line\n")
#     f.write("Sixth line\n")

# print("Three more lines appended!")


# # Exercise 2: Read the complete file using read()

# print("\n--- Reading using read() ---")

# with open("test.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#     print(text)


# # Exercise 2 (continued): Read using a for loop

# print("--- Reading using a for loop ---")

# with open("test.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


# # Exercise 3: Handle a missing file

# print("\n--- Testing missing file ---")

# try:
#     with open("missing.txt", "r", encoding="utf-8") as f:
#         text = f.read()
#         print(text)

# except FileNotFoundError:
#     print("Error: The file does not exist!")


# # Exercise 4: Handle invalid number conversion

# print("\n--- Testing invalid number ---")

# try:
#     number = int("abc")
#     print(number)

# except ValueError:
#     print("Error: That is not a valid number!")




def load_notes(path):
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            notes = json.load(file)

        return notes

    except json.JSONDecodeError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)


def main():
    path = "notes.json"
    notes = load_notes(path)

    while True:
        print("\n--- NOTES MENU ---")
        print("1) Add note")
        print("2) List notes")
        print("3) Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            note = input("Write your note: ")
            notes.append(note)
            save_notes(path, notes)
            print("Note saved!")

        elif choice == "2":
            print("\nYour notes:")

            for note in notes:
                print("-", note)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
