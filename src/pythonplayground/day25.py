""" perform an exercise with csv, dictionary, PriorityQueue, counting """

import csv
import queue

names = {}

with open("src/pythonplayground/example_files/names.csv", newline='', encoding="utf-8") as file_opened :
    csv_file = csv.reader(file_opened, delimiter=",")
    for row_index,row in enumerate(iterable=csv_file, start=0):
        if row_index == 0:
            continue

        # Id,Name,Year,Gender,State,Count
        name_count = int(row[5])
        name = row[1]

        if name in names:
            names[name] = names[name] + name_count
        else:
            names[name] = name_count

print(f"Anzahl Namen: {len(names)}")

priority_names = queue.PriorityQueue()

for name, priority in names.items():
    priority_names.put((-priority, name))

print("")
print("---→ Top 5 Names ←---")
for i in range(0,5):
    amount, name = priority_names.get()
    print(f"Platz {i+1}: {name} ({amount*-1})")
