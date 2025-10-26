# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

# Übungsaufgabe Dictonaries & Schleifen:
# Welcher Name kommt am häufigsten vor?
# example_files/names.csv

# Id,Name,Year,Gender,State,Count
# 1,Mary,1910,F,AK,14

line_counter = 0
allNames = {}


with open(
    "src/pythonplayground/example_files/names.csv", "r", encoding="utf-8"
) as csv_data:

    for index, row in enumerate(iterable=csv_data, start=0):
        # csv_data.write(f"{index:>2}: {row.strip().split(";")} \n")

        if index < 1:
            continue

        # if index > 1000:
        #     break

        line = row.strip().split(",")

        key_name = line[1]
        value_count = int(line[5])

        if key_name not in allNames:
            allNames[key_name] = value_count
            continue

        if key_name in allNames:
            allNames[key_name] += value_count

print(f"We have found {len(allNames)} different names!!!")

most_common_name_of_all_time = ""
tmp_counter = 0

for name, counter in allNames.items():
    if tmp_counter < counter:
        tmp_counter = counter
        most_common_name_of_all_time = name

print(f"The most common name of all time has a total count of {tmp_counter}!")
print(f"The name is >>> {most_common_name_of_all_time} <<< !!!"
)
