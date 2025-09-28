# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name

marvel_villains = [
    "Thanos",
    "Loki",
    "Venom",
    "Magneto",
    "Red Skull",
    "Ultron",
    "Doctor Doom",
    "Kingpin",
]

for index, villain in enumerate(iterable=marvel_villains, start=0):
    if index > 5:
        print(str(index) + " Bösewichte reichen! Schluss!")
        break

    if villain == "Venom":
        print("Nenene, Venom is nicht böse, nur etwas ungehobelt. ;)")
        continue



# Gib aus der Liste continents nur die bewohnten Kontinente aus.
# Hinweis:: Antarktis ist nicht bewohnt.
# Diesen Kontinent kannst du also bei der Ausgabe einfach überspringen.

continents = [
    "Afrika",
    "Antarktis",
    "Asien",
    "Australien und Ozeanien",
    "Europa",
    "Nordamerika",
    "Südamerika",
]

for continent in continents:
    #v1
    if continent == "Antarktis":
        continue
    print(continent)

    #v2
    if continent != "Antarktis":
        print(continent)



# Gib aus der Liste stuff nur die Kontinente aus.

stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]
continents = [
    "Afrika",
    "Antarktis",
    "Asien",
    "Australien und Ozeanien",
    "Europa",
    "Nordamerika",
    "Südamerika",
]

for item in stuff:
    if item in continents:
        print(item)



# Wie viele Kontinente sind in der Liste stuff enthalten?

stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]
continents = [
    "Afrika",
    "Antarktis",
    "Asien",
    "Australien und Ozeanien",
    "Europa",
    "Nordamerika",
    "Südamerika",
]
counter = 0

for item in stuff:
    if item in continents:
        counter += 1

print(counter)

# v2

countinente = []

for item in stuff:
    if item in continents:
        countinente.append(item)

print(len(countinente))





# Berechne für jeden der alten Preise aus der Liste prices die passenden
# reduzierten Preise und speichere sie in der neuen Liste new_prices.
# Gib diese Liste schließlich aus.

prices = [2, 50, 70, 30]
new_prices =[]

for price in prices:
    if price <= 20:
        price *= 0.8
    elif price <= 50:
        price *= 0.6
    else:
        price *= 0.4

    new_prices.append(price)

print(new_prices)



# Die Mathemagierin überreicht dir mit zitternden Händen die Liste _chaos_,
# in der neue und alte Preise gemischt sind! Angesichts dieser undurchdachten
# Arbeit schlägst du dir die Hände vor dem Kopf zusammen, aber es hilft ja
# nichts: Nur du kannst hier wieder Ordnung schaffen, indem du alles
# zusammenbringst, was du schon gelernt hast!
#
# Gehe die Elemente in der Liste _chaos_ durch. Bei einem neuen Preis ziehst
# du bloß den neuen Wert aus dem String und hängst ihn der Liste _order_ an.
# Bei einem alten Preis hingegen holst du dir den alten Wert, berechnest den
# neuen Preis und hängst diesen Wert an die Liste _order_.
#
# Schließlich gibst du die vollständige Liste _order_ aus, in der nur noch
# neue Preise drinstehen (und nur noch Zahlen!).

chaos = [
    "old price: 40",
    "new price: 21",
    "old price: 29",
    "old price:",
    "completly wrong universe"
    "old price: 50",
    "new price: 101",
]
order = []

# hier schreibst du deinen Code hinein
for chaos_price in chaos:

    _, _, num = chaos_price.partition(": ")

    if not num.isnumeric():
        continue


    price = int(num)
    # price = int(chaos_price.split(": ")[1])

    if not "old" in chaos_price:
        order.append(price)
        continue


    # convert old price
    if price <= 20:
        price *= 0.8
    elif price <= 50:
        price *= 0.6
    else:
        price *= 0.4

    order.append(price)

print(order)
