# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string

# Kleine Übungen
# Highscore schreibe, lesen, zurücksetzen

# 1. Spielen
# 2. highscore anzeigen
# 3. highscore zurücksetzen


from datetime import datetime
import sys


# print(scores)


def user_number_input(question):
    """Function asks user for a number input with a given question string."""

    number_input = ""

    while not number_input.isnumeric():
        number_input = input(f"{question}")

    return int(number_input)


programm_choice = input(
    "Was möchtest du machen? ("
    + "1: Zahlenraten spielen,"
    + "2: Highscore ansehen,"
    + "3: kill Highscore):"
)


if programm_choice == "1":
    # play game

    import random

    print("Willkommen zu Zahlenraten. Viel Spaß!")
    print(
        "Spielregeln: Ich wähle jetzt eine Zahl zwischen 1 und 20."
        + "Du versucht die Zahl zu erraten. Liegst du daneben, sage"
        + "ich dir, ob du zu hoch oder zu niedrig bist. Dann kannst"
        + "du nochmal raten, bis du die Zahl hast."
    )

    secret_number = random.randrange(1, 20)

    number_guessed = False
    guessing_attempts = 0

    while not number_guessed:
        guessing_attempts += 1

        user_guess = user_number_input("Bitte gib deinen Tip(Ganzzahl) ab: ")

        if user_guess == secret_number:
            print("Das war richtig! Glückwunsch!")

            if guessing_attempts == 1:
                print(f"Du hast direkt die richtige Zahl({secret_number}) gefunden.")
            elif guessing_attempts < 3:
                print(
                    f"Du bist gut! Du hast die richtige Zahl({secret_number})"
                    + f"nach {guessing_attempts} Versuchen gefunden."
                )
            else:
                print(
                    f"Nach {guessing_attempts} Versuchen gefunden. Besser spät als nie!"
                    + f"Die richtige Zahl ist {secret_number}."
                )

            highscore_name = input("Bib deinen Namen für die Highscores ein: ")

            print(f"Danke {highscore_name}. Wir sehen uns...")

            scores = [
                {
                    "name": highscore_name,
                    "points": 10000 - (guessing_attempts * 1000),
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ]

            with open(
                "example_files/day05_mini_number_guess_highscore.csv",
                "r",
                encoding="utf-8",
            ) as highscore_csv:

                for index, row_highscore in enumerate(iterable=highscore_csv, start=0):
                    # csv_data.write(f"{index:>2}: {row.strip().split(";")} \n")
                    highscore = row_highscore.strip().split(";")
                    scores.append(
                        {
                            "name": highscore[0].strip().strip('"'),
                            "points": int(highscore[1]),
                            "date": highscore[2].strip().strip('"'),
                        }
                    )

                # scores.sort(key = compare_points)

            scores.sort(
                key=lambda x: (
                    -int(x["points"]),
                    datetime.strptime(x["date"], "%Y-%m-%d %H:%M:%S").timestamp(),
                )
            )

            with open(
                "example_files/day05_mini_number_guess_highscore.csv",
                "w",
                encoding="utf-8",
            ) as highscore_csv:
                for score in scores:
                    highscore_csv.write(
                        f"{score['name']};"
                        + f"{score['points']};"
                        + f"{datetime.strptime(score['date'], "%Y-%m-%d %H:%M:%S")}\n"
                    )
            sys.exit()

        if user_guess > secret_number:
            print("Es tut mir Leid, Dein Tip war leider zu hoch.")
        elif user_guess < secret_number:
            print("Es tut mir Leid, Dein Tip war leider zu niedrig.")
elif programm_choice == "2":
    # highscore ansehen

    scores = []

    with open(
        "example_files/day05_mini_number_guess_highscore.csv", "r", encoding="utf-8"
    ) as highscore_csv:

        for index, row_highscore in enumerate(iterable=highscore_csv, start=0):
            # csv_data.write(f"{index:>2}: {row.strip().split(";")} \n")
            highscore = row_highscore.strip().split(";")
            scores.append(
                {
                    "name": highscore[0].strip().strip('"'),
                    "points": int(highscore[1]),
                    "date": highscore[2].strip().strip('"'),
                }
            )

    # key=lambda x: (-int(x["points"]), datetime.strptime(x["date"], "%Y-%m-%d %H:%M:%S"))

    scores.sort(
        key=lambda x: (
            -int(x["points"]),
            datetime.strptime(x["date"], "%Y-%m-%d %H:%M:%S").timestamp(),
        )
    )

    print("\n-------------------------------------------")
    print("|" + "Highscore".center(len("Highscore") + 32, " ") + "|")
    print("-------------------------------------------")

    for index, score in enumerate(iterable=scores, start=0):
        if index > 5:
            break

        print(
            f"| {score['name'][:11]:.<11} | "
            + f"{score['points']:>6} | "
            # + f"{datetime.strptime(score['date'], "%Y-%m-%d %H:%M:%S")} |"
            + f"{
                datetime
                    .strptime(
                        score['date'],
                        '%Y-%m-%d %H:%M:%S'
                    )
                    .strftime('%d.%m.%Y %H:%M')
                } |"
        )

    print("-------------------------------------------")
    print(f"{'*Kissy Kissy': >43}")
elif programm_choice == "3":
    choice_validate_user_choice = user_number_input(
        "Wirklich löschen??? (42=ja, alles andere: nein)"
    )
    if choice_validate_user_choice == 42:
        with open(
            "example_files/day05_mini_number_guess_highscore.csv", "w", encoding="utf-8"
        ) as highscore_csv:
            highscore_csv.write("")

        print("Yeah, alles auf Anfang. Jeder kann Erster sein! Wirst DU es sein?")

        sys.exit()

    print("Puuuhhhh! Das war knapp! Mein lieber Scholli!!!")
else:
    print(
        "Ok, du triffst deine eigene Wahl. Du sagst wo es lang geht. Dann bis zum nächsten Mal."
    )
