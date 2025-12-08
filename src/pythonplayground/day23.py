"""testing datatyp sets"""

my_set = {"hallo", "welt"}

my_set.add("Hallo")
my_set.add("hallo")
my_set.add("Mars")

print(my_set)

if "Mars" in my_set:
    print("'Mars' ist im Set enthalten!")

if not "mars" in my_set:
    print("'mars' NICHT im Set enthalten!")



text = "Online-Betrüger geben sich immer häufiger als Banken und Sparkassen aus. In WhatsApp-Gruppen versprechen sie die Chance aufs große Geld und zocken ihre Opfer ab. Polizei und Verbraucherschützer warnen."
words = set()
for word in text.split(" "):
    words.add(word)

print(f"Anzahl verschiedene Worte im Text:{ len(words) }")



import csv

names = set()

with open("src/pythonplayground/example_files/names.csv", newline='', encoding="utf-8") as file_opened :
    csv_file = csv.reader(file_opened, delimiter=",")
    for row in csv_file:
        # print(row)
        names.add( row[1] )

print( len(names) )
