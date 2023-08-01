aussen = 5
"Dreieck normal"
for zeile in range(aussen):

    for space in range(aussen - (zeile + 1)):
        print(" ", end="")
    for stern in range(0, 2 * (zeile + 1) - 1):
        print("*", end="")

    print()
"Dreieck verkehrt"
print("-----------Dreieck verkehrt------")
for zeile in range(aussen):
    for space in range(1, zeile + 1):
        print(" ", end="")
    for stern in range(0, 2 * (aussen - zeile) - 1):
        print("*", end="")
    print()

for x in range(1, 5):
    if x == 3:
        print("x ist 3")
else:
    print("In else of for")
x = 1
while x < 10:
    print("x is less than 10")
    x += 1
else:
    print("x is not less than 10")

# Sternendreieck
# ähnliche Lösung
startzeile = 1
endzeile = 6
for zeile in range(startzeile, endzeile,1):

    for space in range(1, endzeile-(zeile-1)):
        print("#", end="")

    for star in range(0,2 * zeile -1,1):
                print("*",end="")

    print()




#ungerade zahlen in mathematik
# Formel: 2 * zeile - 1




