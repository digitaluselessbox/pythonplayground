# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

# Exercise inheritance in Python
#
# 1. Create a file reader that reads a
# file and outputs the read data as a list.
#
# 2. Create a CSV reader that reads a file,
# processes the lines as CSV data, and splits
# them into a new list at the comma.


class FileReader:
    def __init__(self, filePath):
        self.fileContent = []

        with open(filePath, "r", encoding="utf-8") as file:
            for row in file:
                self.fileContent.append(row.strip())

    def lines(self):
        return self.fileContent



class CsvReader(FileReader):
    # unneeded super init delegation.
    # super init is used automatically
    #
    # def __init__(self, filePath):
    #     super().__init__(filePath)

    def lines(self):
        csv_data = []
        lines = super().lines()

        for line in lines:
            csv_data.append(line.split(","))

        return csv_data


# read file
f = FileReader("./example_files/datei.csv")
print("Zeilen der Datei als Liste:")
print(f.lines())

print("\n")

# read file as csv data
print("Zeilen der Datei als Liste von CSV Daten:")
c = CsvReader("./example_files/datei.csv")
print(c.lines())
