# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string

import csv

from datetime import datetime
from pathlib import Path
from typing import Dict, List


def print_score(highscore: list[dict]):
    """this function print the complete highscore"""

    print("\n-------------------------------------------")
    print("|" + "Highscore".center(len("Highscore") + 32, " ") + "|")
    print("-------------------------------------------")

    for index, item in enumerate(iterable=highscore, start=0):
        if index >= 10:
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
            int(x["points"]),
            datetime.strptime(x["date"], "%Y-%m-%d %H:%M:%S").timestamp(),
        ),
        reverse=True,
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
