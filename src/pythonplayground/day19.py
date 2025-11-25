import csv

with open("src/pythonplayground/example_files/datei_namen.csv", newline='', encoding="utf-8") as file:
    csv_file = csv.reader(file, delimiter=",", )
    for row in csv_file:
        print(row)

with open("src/pythonplayground/example_files/fromexcel.csv", newline='', encoding="utf-8") as file:
    csv_file = csv.reader(file, delimiter=";", quotechar='"' )
    for row in csv_file:
        print(row)
