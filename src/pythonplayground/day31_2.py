import os

# print(os.listdir("."))

# print(__file__)

working_folder = os.path.dirname(__file__)
print(working_folder)

with open( os.path.join(working_folder, "example_files/datei_namen.csv"), "r", encoding="utf-8") as file_data:
    for line in file_data:
        print(line)

print("\n-----------------------")
print("|" + "---> next <---".center(len("---> next <---") + 7, " ") + "|")
print("-----------------------")


folder = os.path.join(os.path.dirname(__file__), "example_files")
#folder = os.path.join(os.path.dirname(__file__), "..") # one folder up ↑

print(os.listdir(folder))

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isdir(file_path):
        print(f"'{file}' (Folder)")
    else:
        print(f"'{file}' (File)")

print("\n-----------------------")
print("|" + "---> next <---".center(len("---> next <---") + 7, " ") + "|")
print("-----------------------")

complete_folder_path = os.path.join(os.path.dirname(__file__), "example_files", "subfolder", "..", "subfolder", "myfile.txt")
print(complete_folder_path)

with open( complete_folder_path, "r", encoding="utf-8") as file_data:
    for line in file_data:
        print(line)
