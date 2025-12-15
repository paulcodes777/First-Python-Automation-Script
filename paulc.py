import os
import random

# create 3 folders
for i in range(3):
    dir = input("Enter username (folder name): ")

    try:
        os.mkdir(dir)
    except FileExistsError:
        print(f"Directory '{dir}' already exists.")

    # create 3 random files in each folder
    for u in range(3):
        filename = "file.txt"
        full_path = os.path.join(dir, filename)

        try:
            with open(full_path, "w") as file:
                pass
            print(f"Created file: {full_path}")
        except IOError as e:
            print(f"Error writing to file {full_path}: {e}")
