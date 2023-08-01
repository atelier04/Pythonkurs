# Ein Array ist ein Behälter, der meherere Elemente aufnehmen kann.
# Zwar meherere variablen in eine zeile
a, b, c, d, e, f = 1, 2, 3, 4, 5, 6
# Dennoch bei vielen Variablen ( z.B 1000 und mehr) nicht mehr machbar.
# Daher verwendet man Arrays.
# Arrays sind in Python Listen
# Eine Liste ist eine datenstruktur, die wachsen und schrumpfen im Gegensatz zu einem Array kann.
# Eckiges Klammernpaar ist die Syntax für ein Array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(f"Die zahl ist {number} ")
städte = ["Wien", "New York", "Mailand", "Paris"]
"""
for stadt in städte:
    print(f"Die Stadt ist {stadt}")
"""
print(f"Die Stadt ist {städte[2]}")
# Es gibt ein und mehrdimensionale Arrays
# Eindimensional bedeutet, die Element eines Arrays sind Variablen wie int, float, str, object...
# Mehrdimensionale Arrays bedeutet, die Elemente sind wiederum Arrays
mehrdim_numbers = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5, 6, [3, 9, 11, 12]]
array_an_pos_sieben = mehrdim_numbers[7]
print(mehrdim_numbers[7])
print(array_an_pos_sieben[2])
print(f"Ist array_an_pos_sieben ein Array? {type(array_an_pos_sieben)}")
print(f"Ist array_an_pos_sieben ein Array? {type(mehrdim_numbers[7])}")

#print("range(1, 10)", range)
# range(1,10) ist ein sogenannter iterator. Ein Iterator ist ein Object, über das man iterieren( durchlaufen lassen)
# kann.
print(list(range(1,10)))
print(list(range(1,10))[0])
wort = "Monica"
for zeichen in wort:
    print(zeichen, sep="#");
satz = "hallo, wie gehts?"
for wort in satz:
    print(wort, end=" ")

