import os
import random

def create_users():
    # create 3 folders
    for i in range(3):
        dir_name = input("Enter username (folder name): ")

        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print(f"Directory '{dir_name}' already exists.")

        # create 3 random files in each folder
        for u in range(3):
            filename = f"file{random.randint(1, 1000)}.txt"
            full_path = os.path.join(dir_name, filename)

            try:
                with open(full_path, "w"):
                    pass
                print(f"Created file: {full_path}")
            except IOError as e:
                print(f"Error writing to file {full_path}: {e}")


if __name__ == "__main__":
    create_users()

