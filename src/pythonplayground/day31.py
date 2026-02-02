import sys

print(sys.argv)
print( len(sys.argv) )

if len(sys.argv) == 2:
    file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as file_data:
            counter = 0
            for index, row in enumerate(iterable=file_data, start=0):
                counter = counter + 1

        print(f"Die Datei {file_path} hat {counter} Zeilen.")
    except FileNotFoundError:
        print("Datei konnte nicht gefunden werden!")
else:
    print("Bitte gib einen Dateipfad an.")
