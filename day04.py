# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name


# ### functions ###

# system function
print("hallo Welt")

#custom function
def myPrint(name, repetition):
    '''nur eine Testfunktion der einfachsten Art'''
    for step in range(0, repetition):
        print(f'{name} ({step})')


myPrint('Ben', 10)


def maximum(a, b):
    ''' maximun von zwei Zahlen '''
    if a < b:
        return b
    else:
        return a

result = maximum(4, 5)
print(result)


# object functionen
liste = [1, 2, 3]
liste.append(4)

print(liste)



# etwas sehr viel wilder: simple higher order function
def apply_twice(func, value):
    ''' higher order function. ruft die übergebene function zweimal auf  '''
    return func(func(value))

def square(x):
    ''' Übergabe Function '''
    return x * x

result = apply_twice(square, 2)
print(result)



# typing/typ hints examples 01
from typing import Optional

def greet(name: str, times: int = 1, suffix: Optional[str] = " Alaaf!\n") -> str:
    ''' testfunktion die eibeb gruß erstellt und zurück gibt '''
    # name: Pflichtparameter vom Typ str
    # times: optional, Standardwert 1
    # suffix: optional, darf str oder None sein
    text = (name + (suffix or "")) * times
    #return 1243  #gibt keinen Fehler obwohl return als str definiert wurde
    return text


print( greet( name = "Kölle", times = 3, suffix=" Alaaf!!!\n" ) )

# #### KEINE TYPSICHERHEIT IN PYTHON, WÄREND DER LAUFZEIT!!!!
# Fehler kommt erst contanieren von name und suffix, weil name vom typ int ist
# print( greet( name = 1234, times = 3, suffix=", alaf!!!\n" ) )

print( greet( name = "Kölle", times = 3 ) )



# Typisierung ist nur als hint gedacht um mögliche Parameter
# besser zu dokumentieren.
# Type Hints (PEP 484) !!!

# mögliche Lösung: Manuell mit isinstance() :D....NEIN!

# Besser mit zusätzlichen Python Bibliotheken Prüfung implementieren.
# Beispiel: Pydantic oder beartype
# Simon hat Pydantic als Lerninhalt genannt. 
# Also machen...
