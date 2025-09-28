# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string

# Kleine Übungen
# Mach mindestens eine der folgenden Mini-Aufgaben (oder alle, wenn du Lust hast):

# 1. Zahlenraten:
# - Programm wählt zufällige Zahl 1–20 (import random).
# - Benutzer rät, bis er richtig liegt.
# - Gib nach jedem Versuch aus, ob zu hoch oder zu niedrig.

# 2. Multiplikationstabelle:
# - Benutzer gibt eine Zahl ein.
# - Gib das 1-bis-10-Einmaleins dafür aus.

# 3. Countdown:
# - Starte bei einer Zahl n und zähle mit while oder for bis 0 herunter.

def user_number_input( question ):
    """Function asks user for a number input with a given question string."""

    number_input = ""

    while not number_input.isnumeric():
        number_input = input(f"{question}")

    return int( number_input )



programm_choice = input("Welche Spaß möchtest du machen? ("
                        + "1: Zahlenraten,"
                        + "2: Multiplikationstabelle,"
                        + " 3: Countdown):" )

print( isinstance(programm_choice, str) )

if programm_choice == "1":
    import random

    print("Du hast Zahlenraten ausgesucht. Eine hervorragende Wahl!")
    print("Spielregeln: Ich wähle jetzt eine Zahl zwischen 1 und 20."
          + "Du versucht die Zahl zu erraten. Liegst du daneben, sage"
          + "ich dir, ob du zu hoch oder zu niedrig bist. Dann kannst"
          + "du nochmal raten, bis du die Zahl hast.")

    secret_number = random.randrange(1,20)

    print()
    number_guessed = False
    guessing_attempts = 0

    while not number_guessed:
        guessing_attempts += 1

        user_guess = user_number_input( "Bitte gib deinen Tip(Ganzzahl) ab: " )

        if user_guess == secret_number:
            print("Das war richtig! Glückwunsch!")

            if guessing_attempts == 1:
                print(f"Du hast direkt die richtige Zahl({secret_number}) gefunden.")
            elif guessing_attempts < 3:
                print(f"Du bist gut! Du hast die richtige Zahl({secret_number})"
                      + "nach {guessing_attempts} Versuchen gefunden.")
            else:
                print(f"Nach {guessing_attempts} Versuchen gefunden. Besser spät als nie!"
                      + "Die richtige Zahl ist {secret_number}.")

            break

        if user_guess > secret_number:
            print("Es tut mir Leid, Dein Tip war leider zu hoch.")
        elif user_guess < secret_number:
            print("Es tut mir Leid, Dein Tip war leider zu niedrig.")
elif programm_choice == "2":
    print("Ich hätte keine besser wahl treffen können. Du willst dich"
          + "also Fortbilder. Gute Einstellung! Gibt mir eine Zahl, ich"
          + "gebe Dir das 1x1 zu der Zahl.")

    user_guess = user_number_input( question = "Bitte gib mir deine Zahl: ")

    max_multipli_result_length = len( str( user_guess * 10 ) )

    for multiplier in range( 1, 11 ):
        multipli_result = user_guess * multiplier

        # with f-String: f'{multiplier:>2} x {user_guess}:
        # {multipli_result:>{max_multipli_result_length}}'
        print(
            '{:>2}'.format( multiplier) 
            + f' x {user_guess} : '
            + '{:{}{}}'.format( multipli_result, '>', max_multipli_result_length )
        )

elif  programm_choice == "3":
    print("Jetzt wird's aber richtig wild! Kikeriki!")

    countdown = user_number_input("Sag mir eine Nummer ich zähle bis 0 runter. Was ein Spaß! ")
    max_countdown_length = len( str( countdown ) )

    while countdown != 0:
        # with f-string: print(f"{countdown:>{max_countdown_length}}")
        print('{:{}{}}'.format( countdown, '>', max_countdown_length ) )
        countdown -= 1

    print("Das war's auch schon. Huiiiiihhhh!")

else:
    print("Ok, du triffst deine eigene Wahl. Du sagst wo es lang geht. Dann bis zum nächsten Mal.")
