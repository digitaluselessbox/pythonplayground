# pylint: disable=invalid-name

"""test for day05_1.py"""

import math
import pytest
from pythonplayground.day05_1 import area_circle, user_number_input, user_number_multiplication

def test_area_circle():
    """Testet eine bekannte Fläche (Radius 1 => π)"""
    assert area_circle(1) == pytest.approx(expected=math.pi, rel=1e-6)


def test_area_circle_zero():
    """Randfall: Radius 0"""
    assert area_circle(0) == 0


def test_area_circle_4():
    """Testfall: 4"""
    # rel nimmt expected und multipliziert es mit rel, das ist die erlaubte Abweichung
    # abs nimmt genau den gegebenen wert als Abweichung
    assert area_circle(4) == pytest.approx(expected=50.26, abs=0.006)


def test_user_number_input(monkeypatch):
    """Simuliert Benutzereingabe "42" """
    monkeypatch.setattr("builtins.input", lambda _: "42")

    assert user_number_input("Gib eine Zahl ein: ") == 42


def test_user_number_multiplication(monkeypatch):
    """Simuliert Benutzereingabe von 7*6 = 42"""

    # ACHTUNG Imput Mocks müssen immer String sein
    user_input_mock = iter(["7", "6"])

    monkeypatch.setattr("builtins.input", lambda _: next(user_input_mock))

    assert user_number_multiplication("Gib eine Zahl ein: ") == 42
