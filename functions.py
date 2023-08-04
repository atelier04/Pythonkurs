""" (mehrzeiliger Kommentar)
 Funktionen sind Anweisungsblöcke, die mindestens eine oder mehrere Anweisungen ausführen,
 und dann zum Schluss ein bestimmtes Ergebnis liefern.
 In den runden Klammern stehen die Parametervariablen(Ausgangsvariablen) drinnen.
"""


def add(number1, zahl2):
    return number1 + zahl2

# Funktion wird ausgeführt, indem man den Funktionsnamen schreibt mit den runden Klammern danach
# und in die runden Klammern kommen die Werte für die Funktionsparameter( Argumente)
# return bedeutet , gib das ergebnis an den Aufrufer der Funktion zurück, ist letzte Anweisung
# im Funktionsblock. Danach wird die Funktion verlassen, es geht nach dem Funktionsblock weiter

summe = add(1, 2)
print(f" Die Summe von add(1, 2) ist { summe}")


def multiply( zahl1, zahl2):
    ergebnis_local = zahl1 * zahl2
    return ergebnis_local


ergebnis_global = multiply(123, 4567)
# ergebnis_local nur innerhalb des Funktionsblocks gültig
# ergebnis_global = ergebnis_local
print(f"Die Multiplikation von multiply( zahl1, zahl2) ist {ergebnis_global}")



def calculate(zahl1, zahl2):
    return zahl1 + zahl2

def aussen_func(zahl1):
    zahl2 = 30
    return calculate(zahl1, zahl2)


print(f"Die Calculation ergab {aussen_func(10)}")

#  Funktionen ineinander verschachteln möglich

"""
def aussen_aussen_func(zahl1):

    def aussen_func2(zahl2):

        def calculate_innen( zahl1, zahl2, zahl3):
            #print(f"Das ergebnis  ist (zahl1 + zahl2 ) * zahl3 {(zahl1 + zahl2 ) * zahl3}")
            return (zahl1 + zahl2) * zahl3

        return calculate_innen(zahl1, zahl2, 10)
    return aussen_func2(20)


print(f" aussen_aussen_func(5) {aussen_aussen_func(5)} ")

"""

def aussen_aussen_func(zahl1):

    def aussen_func2(zahl2):

        def calculate_innen( zahl1, zahl2, zahl3):
            #print(f"Das ergebnis  ist (zahl1 + zahl2 ) * zahl3 {(zahl1 + zahl2 ) * zahl3}")
            return (zahl1 + zahl2) * zahl3

        return calculate_innen(zahl1, zahl2, 10)
    return aussen_func2


print(f" aussen_aussen_func(5) {aussen_aussen_func(5)} ")
aussen_func2 = aussen_aussen_func(5)
calculate_innen = aussen_func2(30)
calculate_innen(5, 30, 10)

def aussen_aussen_func(zahl1):

    def aussen_func2(zahl2):

        def calculate_innen( zahl1, zahl2, zahl3):
            print(f"Das ergebnis  ist (zahl1 + zahl2 ) * zahl3 {(zahl1 + zahl2 ) * zahl3}")
            return (zahl1 + zahl2) * zahl3

        return calculate_innen
    return aussen_func2


print(f" aussen_aussen_func(5) {aussen_aussen_func(5)} ")
aussen_func2 = aussen_aussen_func(5)
calculate_innen = aussen_func2(30)
calculate_innen(2, 1, 3)
