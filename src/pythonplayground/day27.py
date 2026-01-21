"""practicing function parameters"""


# #### first exercise
def shortest_word(first, *args):
    """returns the shortest word from the given arguments"""

    # first gives a clear function signature.
    # at least one word is necessarry

    # shortest = args[0] # index error when args is empty
    shortest = first

    for argument in args:
        if len(argument) < len(shortest):
            shortest = argument

    return shortest


print(shortest_word("Max", "Moritz", "Monika", "Tim", "Jo"))


# #### second exercise

# ## second exercise - part 1
# with extra function
tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]


def sum_tuple(i):
    return i[0] + i[1]


tupels.sort(key=sum_tuple)

print(tupels)


# ## second exercise - part 2
# with lambda
tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]
tupels.sort(key=lambda i: i[0] + i[1])  # with lambda
print(tupels)


# ## second exercise - part 3
import math  # with math module
tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]
tupels.sort(key=math.fsum)
print(tupels)


# ## third exercise - part 1
# sortiere die Liste names mit Namen nach dem Nachnamen.
names = ["Elif Else","Sebastian Klarnamen","Anna Boa","Anton Adel","Conny Coder","Anne Wortmann","Willy Cordes"]

def receive_lastname(name):
    return name.split()[1]

names.sort( key = receive_lastname )

print(names)


# ## third exercise - part 2
names = ["Elif Else","Sebastian Klarnamen","Anna Boa","Anton Adel","Conny Coder","Anne Wortmann","Willy Cordes"]
names.sort(key=lambda x: x.split()[1])
print(names)


# ## third exercise - part 3
sentences = [
    "Sie liefen weiter den Strand entlang.",
    "Der Hund bellte laut.",
    "Er rutschte aus.",
    "Sie lachte.",
]

sentences.sort(key=lambda sentence: len(sentence.split()), reverse = True)

print(sentences)


l = ["o", "x", "o"]


def make_row(row):
    # create a copy of row
    new_row = row[:] # list slice: start to end
    # row = row[:] # working with row and create a new row
    # or: new_row = row.copy()
    # or: new_row = [i for i in row]

    new_row[2] = "x"

    print(new_row)

make_row(l)
print(l)


# EXTREM IMPORTANT!! Look at Learning Diary!!!!
def make_row2(row):
    # create a copy of row
    row = row[:] # working with row and create a new row

    row[2] = "x"

    print(row)

make_row2(l)
print(l)
