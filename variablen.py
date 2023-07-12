""""
Dieser Kommetar geht über mehrere Zeilen
Hier kommt noch ein Text
Beispiel für mehrzeiliges Kommentar
"""
# Das ist ein einzeiliger Kommentar
""""
Erklärung zu Byte und Bit
Ein Byte ist eine Kombination von 8 Bit.
Ein Bit kann den Wert 0 oder 1 annehmen.
Beispiel für Byte:
10001011
Umrechnung von binär in dezimal an einem Beispiel:
101(binär) ist 1*2^2+0*2^1+1*2^0=5
Datentypen:
1) Zahlentypen
int ( ganze Zahlen) 1,2,3....
Wertebereich bei int -2^32-1  ..... 0 .... 2^31-1
float (Kommazahlen) 1.0, 2.48, 3.14, 7.9432423...
Komplexer Zahlentyp verwendet  so genannte imaginäre Einheit(j)
Beispiel: z = 2+ 3 * j
Für komplexe mathematische Operationen (Rechnen mit großen Zahlen) verwendet man Bibliotheken wie z.B numpy 

"""
# Boolscher Typ kann nur den Wert True oder False haben.
wahrheitsvariable = True
# Beachte True ist ein keyword und darf nicht der Name einer Variablen sein
print(" Die wahrheitsvariable ist vom typ  ", type(wahrheitsvariable))
zahl_eins=1
print("Die zahl_eins variable ist vom typ  ", type(zahl_eins))
float_var1 = 1.23
print("die float_var1 variable ist vom typ" ,type(float_var1 ))
# String (zeichenketten) typ ( text typ) unter '' oder  ""
wort_eins = "text1"
print(" Der inhalt von wort_eins ist ", wort_eins)
print("die wort_eins variable ist vom typ " , type(wort_eins))
# Alle Datentypen die wir bis jetzt besprochen haben, sind die sogenannten primitiven(einfachen) Datentypen
# das bedeutet, der Wert(Inhalt) kann direkt von der variablen ausgegeben durch den Vraiablennamen werden
# Unterscheidung zu sogenannten Referenztypen(Objekttypen). Mehr dazu im Kapitel objekttypen.
