# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

# lists
#  Thanos, Loki, Magneto, Red Skull, Venom, Ultron und Doctor Doom.
#  Weitere sind Kang der Eroberer, Baron Mordo, Erik Killmonger, Kingpin

marvel_villains = [
    "Thanos",
    "Loki",
    "Magneto",
    "Red Skull",
    "Venom",
    "Ultron",
    "Doctor Doom",
    "Kang der Eroberer",
    "Baron Mordo",
    "Erik Killmonger",
    "Kingpin",
]

marvel_villains_string = ", ".join(marvel_villains)
print("Marvel Schurken: " + marvel_villains_string)

marvel_villains_string = "Thanos, Loki, Magneto, Red Skull, Venom, Ultron"

marvel_villains = marvel_villains_string.split(", ")
# print( marvel_villains )

# append Green Goblin to list
marvel_villains.append("Green Goblin")

# insert Mystic in the middle of the list
marvel_villains.insert(len(marvel_villains) // 2, "Mystic")

# prepend Proxima Midnight to list
marvel_villains.insert(0, "Proxima Midnight")

# list concatenation
# marvel_villains = ["Mystic"] + marvel_villains


# remove the second item in the list
marvel_villains.pop(1)
# remove the second last item in the list
marvel_villains.pop(-2)

last_vilian_removed_from_list = marvel_villains.pop()
print(f"Letzter Marvel Schurke entfernt von der Liste: {last_vilian_removed_from_list}")


amount_of_villains = len(marvel_villains)
print(f"Anzahl der Marvel Schurken in der Liste: {amount_of_villains}")


print()

# if / elif / else – bedingte Ausführung
# comparison operators: <, >, <=, >=, ==, !=

if amount_of_villains < 5:
    print("Weniger als 5 Schurken in der Liste.")
elif amount_of_villains < 10:
    print("Weniger als 10 Schurken in der Liste.")
elif amount_of_villains < 15:
    print("Weniger als 15 Schurken in der Liste.")
else:
    print("15 oder mehr Schurken in der Liste.")


if amount_of_villains == 6:
    print(f"Genau 6 Schurken in der Liste: { ', '.join( marvel_villains ) }")

print()

# while-Schleife
while amount_of_villains > 0:
    removed_villain = marvel_villains.pop()
    print(f"Marvel Schurke entfernt: {removed_villain}")
    amount_of_villains = len(marvel_villains)
    print(f"Noch {amount_of_villains} Schurken in der Liste.")

if amount_of_villains == 0:
    print("Keine Schurken mehr in der Liste.")
else:
    print(f"Schurken übrig in der Liste: {', '.join( marvel_villains ) }")


print()


# for-Schleife

marvel_villains_string = (
    "Thanos, Loki, Magneto, Red Skull,"
    "Venom, Red Skull, Ultron, Doctor Doom, Kang der Eroberer,"
    "Baron Mordo, Erik Killmonger, Kingpin"
)

marvel_villains = marvel_villains_string.split(", ")

for index, villain in enumerate(iterable=marvel_villains, start=0):
    # position des Schurken mit ausgeben. Achtung Red Skull kommt zweimal vor!

    # Variante 1 mit ermittlung der Position über suche in der Liste.
    # Funktioniert nicht bei mehrfach vorkommenden Namen!!!
    # print(f"Marvel Schurke an Position {marvel_villains.index(villain)+1}: {villain}")

    # Variante 2 mit einer extra Variable die die Position mitzählt!
    print(f"Marvel Schurke an Position {index}: {villain}")
