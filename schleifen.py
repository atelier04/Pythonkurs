# Schleife:
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# Wenn Code sich wiederholt( sich nur mehr eine Kleinigkeit ändert), dann Schleife machen
start=4
end=1
count=0
for zahl in range(start,end,-2):

    count=count+1
    print("schleifendurchlauf",count)
    print("zahl",zahl)
    print(zahl**2)
else:
    print("In else von for in")
#Übungsbeispiel Berechne mit einer for in schleife die summe der ersten 100 Zahlen und lasse die Summe ausgeben
# Der Benutzer soll eine Zahl eingeben, die soll größer als 1 sein, ansonsten meldung an den benutzer. Wenn größer als Eins, dann
# soll die Summe bis zu der zahl berechnet werden.
# Beispiel Benutzer gibt 10 ein, dann soll 1+2+3+4+5+6+7+8+9+10.... +100  Trick(Formel): 100/2 *101=5050 10*11/2=55
for x in range(20,1,-3):
    print("Die zahl ist ",x)
    if x == 11:

        print("in if von x=11")
        break

    print("Innerhalb der Schleife  ausserhalb von x gleich 11 ")
else:
    print(" innerhalb von else der for in Schleife ")
print("nach break")
# while schleife
# while bedingung:
x = 5
print ("-----------------------------------------------------------")
while x < 10:
    print("zahl ist ", x)

    print("zahl ist kleiner als 10 ", x)
    x = x+1
    if x == 9:
        x = x-4
        print("in if von x=9 ", x)
        break
else:
    x = x+3
    print("In else von while, die zahl x ist ", x)
print("ausserhalb von while else ",x)




