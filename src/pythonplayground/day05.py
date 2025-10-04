# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

# ### Dateien ###

# open a file

print("--------------------\ncsv open a file\n--------------------")
file = open("example_files/lesen.txt", "r")
for row in file:
    print(row[-1] == "\n")
    print(row.strip())

file.close()


## write
# file = open("example_files/schreiben.txt", "w")

# file.write("asdfasdf")

# file.close()


# append
marvel_villains = [
    "Thanos",
    "Loki",
    "Venom",
    "Magneto",
    "Red Skull",
    "Ultron",
    "Doctor Doom",
    "Kingpin",
    "Kang der Eroberer",
    "Baron Mordo",
    "Erik Killmonger",
    "Kingpin",
]


file = open("example_files/schreiben.txt", "a")

for index, villain in enumerate(iterable=marvel_villains, start=0):
    # file.write(f"{index}:{villain}")
    file.write("{:>2}".format(index) + ": " + villain + "\n")

file.close()


## with construct
print("--------------------\ncsv with construct\n--------------------")
with open("example_files/schreiben.txt", "a", encoding="utf-8") as file:
    for index, villain in enumerate(iterable=marvel_villains, start=0):
        file.write(f"{index:>2}: {villain} \n")
        print(f"{index:>2}: {villain}")


# csv Datei auslesen
print("--------------------\ncsv csv auslesen\n--------------------")
with open("example_files/csv_datei.csv", "r", encoding="utf-8") as csv_data:
    for index, row in enumerate(iterable=csv_data, start=0):
        # csv_data.write(f"{index:>2}: {row.strip().split(";")} \n")
        line = row.strip().split(";")

        print(f"{line[0]}: {line[1]}")


# csv Datei auslesen
print("--------------------\ncsv csv auslesen extended \n--------------------")
with open("example_files/csv_datei.csv", "r", encoding="utf-8") as csv_data:
    print("-------\nnur BER,BUD \n-------")
    for index, row in enumerate(iterable=csv_data, start=0):
        # csv_data.write(f"{index:>2}: {row.strip().split(";")} \n")
        line = row.strip().split(";")  #

        if line[2] == "BER" or line[2] == "BUD":
            print(f"{line[0]}: {line[1]}")

with open("example_files/csv_datei.csv", "r", encoding="utf-8") as csv_data:
    print("-------\nnur mehr als 2 Mio. \n-------")
    for index, row in enumerate(iterable=csv_data, start=0):
        # csv_data.write(f"{index:>2}: {row.strip().split(";")} \n")
        line = row.strip().split(";")

        if int(line[1]) > 1800000:
            print(f"{line[0]}: {line[1]}")

with open("example_files/csv_datei.csv", "r", encoding="utf-8") as csv_data:
    print("-------\nnur mehr als 2 Mio. v2 \n-------")
    for index, row in enumerate(iterable=csv_data, start=0):
        # csv_data.write(f"{index:>2}: {row.strip().split(";")} \n")
        line = row.strip().split(";")

        if int(line[1]) < 1600000:
            continue

        if line[2] == "BUD":
            continue

        print(f"{line[0]}: {line[1]}")
