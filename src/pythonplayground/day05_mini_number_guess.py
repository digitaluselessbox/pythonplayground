# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string

# Kleine Übungen
# Highscore schreibe, lesen, zurücksetzen

# 1. Spielen
# 2. highscore anzeigen
# 3. highscore zurücksetzen


import csv
import sys
import os
import random
from datetime import datetime
from pathlib import Path
from typing import Dict, List

highscore_csv_path = "example_files/day05_mini_number_guess_highscore.csv"


def user_number_input(question) -> int:
    """Function asks user for a number input with a given question string."""

    number_input = ""

    while not number_input.isnumeric():
        number_input = input(f"{question}")

    return int(number_input)


def print_score(highscore: list[dict]):
    """this function print the complete highscore"""

    print("\n-------------------------------------------")
    print("|" + "Highscore".center(len("Highscore") + 32, " ") + "|")
    print("-------------------------------------------")

    for index, item in enumerate(iterable=highscore, start=0):
        if index > 10:
            break

        print(
            f"| {item['name'][:11]:.<11} | "
            + f"{item['points']:>6} | "
            + f"{
                datetime
                    .strptime(
                        item['date'],
                        '%Y-%m-%d %H:%M:%S'
                    )
                    .strftime('%d.%m.%Y %H:%M')
                } |"
        )

    print("-------------------------------------------")
    print(f"{'*Kissy Kissy': >43}")


def sort_scores(score_data: list[dict]):
    """sorting the score list for point descanding and dates ascending"""
    score_data.sort(
        key=lambda x: (
            -int(x["points"]),
            datetime.strptime(x["date"], "%Y-%m-%d %H:%M:%S").timestamp(),
        )
    )

    return score_data


def load_scores(path: str) -> List[Dict[str, str]]:
    """
    Lädt Highscores aus einer CSV-Datei.

    Args:
        path: Pfad zur CSV-Datei

    Returns:
        Liste von Dicts mit Keys: "name", "points", "date"
    """
    result = []

    file = Path(path)

    if not file.exists():
        return result  # leere Liste zurück, wenn Datei fehlt

    with file.open(mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            # Score als int konvertieren
            row["points"] = int(row["points"])
            result.append(row)

    result = sort_scores(score_data=result)

    return result


def save_scores(path: str, score_data: List[Dict[str, str]]) -> None:
    """
    Speichert Highscores in eine CSV-Datei.

    Args:
        path: Pfad zur CSV-Datei
        scores: Liste von Dicts mit Keys: "name", "score", "date"
    """
    sort_scores(score_data=score_data)

    file = Path(path)

    # Spaltenüberschriften fix definieren
    fieldnames = ["name", "points", "date"]

    with file.open(mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

        # Kopfzeile schreiben
        writer.writeheader()

        # Alle Zeilen schreiben
        for row in score_data:
            writer.writerow(
                {
                    "name": row["name"],
                    "points": int(row["points"]),  # sicherstellen, dass es int ist
                    "date": row["date"],
                }
            )

def play_game() -> dict:
    """ this function represents the game play of number gussing """

    secret_number = random.randrange(1, 20)

    number_guessed = False
    guessing_attempts = 0
    highscore_name = ""  # Initialize to avoid unbound error

    print("Willkommen zu Zahlenraten. Viel Spaß!")
    print(
        "Spielregeln: Ich wähle jetzt eine Zahl zwischen 1 und 20."
        + "Du versucht die Zahl zu erraten. Liegst du daneben, sage"
        + "ich dir, ob du zu hoch oder zu niedrig bist. Dann kannst"
        + "du nochmal raten, bis du die Zahl hast."
    )

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

            number_guessed = True  # Ensure loop exits after correct guess

            return {"name": highscore_name, "guessing_attempts": guessing_attempts}

        if user_guess > secret_number:
            print("Es tut mir Leid, Dein Tip war leider zu hoch.")
        elif user_guess < secret_number:
            print("Es tut mir Leid, Dein Tip war leider zu niedrig.")

    # Fallback return to satisfy all code paths
    return {"name": highscore_name, "guessing_attempts": guessing_attempts}


programm_choice = input(
    "Was möchtest du machen? ("
    + "1: Zahlenraten spielen,"
    + "2: Highscore ansehen,"
    + "3: kill Highscore):"
)


if programm_choice == "1":
    # play game

    game_result = play_game()

    # Update scores and save highscore
    scores = load_scores(highscore_csv_path)

    scores.append(
        {
            "name": game_result["name"],
            "points": str(10000 - (game_result["guessing_attempts"] * 1000)),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

    save_scores(path=highscore_csv_path, score_data=scores)

    sys.exit()

elif programm_choice == "2":
    # highscore ansehen

    scores = []

    scores = load_scores(highscore_csv_path)

    print_score(highscore=scores)

elif programm_choice == "3":
    choice_validate_user_choice = user_number_input(
        "Wirklich löschen??? (42=ja, alles andere: nein)"
    )
    if choice_validate_user_choice == 42:
        os.remove(highscore_csv_path)

        print("Yeah, alles auf Anfang. Jeder kann Erster sein! Wirst DU es sein?")

        sys.exit()

    print("Puuuhhhh! Das war knapp! Mein lieber Scholli!!!")
else:
    print(
        "Ok, du triffst deine eigene Wahl. Du sagst wo es lang geht. Dann bis zum nächsten Mal."
    )
