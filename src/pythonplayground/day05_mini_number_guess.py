# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string

# Kleine Übungen
# Highscore schreibe, lesen, zurücksetzen

# 1. Spielen
# 2. highscore anzeigen
# 3. highscore zurücksetzen


import sys
import os
import random
from datetime import datetime
from pythonplayground.day05_highscore_utils import load_scores, save_scores, print_score

highscore_csv_path = "example_files/day05_mini_number_guess_highscore.csv"


def user_number_input(question) -> int:
    """Function asks user for a number input with a given question string."""

    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Bitte eine ganze Zahl eingeben!")


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
