"""
Operatoren

Definition: Vorschrift, die auf einen bestimmten Ausdruck angewendet wird, um ein bestimmtes Ergebnis zu bekommen
"""
# Arithmetischen Operatoren
zahl_zwei = 2
zahl_drei = 3
# Beispiel fü den + Operator
print("Die summe von zahl_zwei und zahl_drei ist ", zahl_zwei + zahl_drei)
# Beispiel für den Divisionsoperator
zahl_vier = 4
zahl_fünf = 5
print("Die Division von zahl_vier und zahl_fünf liefert  ", zahl_fünf / zahl_vier)
# Modulo Operator
# Beispiel
zahl_sechs = 6
zahl_sieben = 7
print("Die Modulo Operation von zahl_sechs und zahl_sieben ergibt   ", zahl_sechs % zahl_sieben)
zahl_sieben = 7
zahl_sechs = 6
print("Die Modulo Operation von zahl_sieben und zahl_sechs ergibt   ", zahl_sieben % zahl_sechs)
print(" Die ganzzahlige Division von zahl_sieben und zahl_zwei ergibt " , zahl_sieben // zahl_zwei )
# Vergleichsoperatoren , liefern immer einen logischen Ausdruck
# Bei einfachen Datentypen werden direkt die Inhalte(Werte) verglichen
# Beispiel für ganze Zahlen
zahl_acht = 8
zahl_neun = 9
print(" Der Vergleich von zahl_acht und zahl_neun ergibt ",zahl_acht == zahl_neun)#
# Beispiel für Strings
wort_eins = "Text1"
wort_zwei = "text1"
print("Der Vergleich von wort_eins mit wort_zwei ergibt", wort_eins == wort_zwei)
# Beispiel für Ungleich !=
print("Der Vergleich mit Ungleich(!=)  von wort_eins mit wort_zwei ergibt ",wort_eins!=wort_zwei)
# Beispiel zu and
logisch_var1= True
logisch_var2 = False
print("Die and Operation von logisch_var1 mit logisch_var2 ergibt  ",logisch_var1 and logisch_var2)
logisch_var1 =  True
logisch_var2 = False
print("Die or Operation von logisch_var1 mit logisch_var2 ergibt  ",logisch_var1 or logisch_var2)
zahl_neun_text = "9"
zahl_zehn= 2
# <= und >=
print(" zahl_zwei grösser oder gleich  zahl_zehn", zahl_zehn >= zahl_zwei)
print(" zahl_zwei grösser oder gleich  zahl_zehn",zahl_zehn <= zahl_zwei)
# Logische Operatoren
wetter_gut = True
sommer = True
print(" Wenn Wetter gut ist und Sommer ist, dann gehe ich schwimnmen ", wetter_gut != sommer)
# XOR Operator (Exclusives Oder, nur eines von beiden darf true sein, damit ergebnis true ist)
# Im Beispiel ist Ergebnis False, weil beide True sind
print(" Wenn Wetter gut ist und Sommer ist mit true operator, dann gehe ich schwimnmen ", wetter_gut ^ sommer)
#Beispiel dezimal in binär 65  Division durch 2 mit höchster Hochzahl 2^6=64  1000001 1* 2^6 0 0* 2^5 + 0 * 2^4 + 0 * 2^3 + 0 * 2^2 + 1* 2^1 + 1* 2^0
# Unicode Tabelle Erfassung aller Symbole und Schriftzeichen
# Bitopertoren Vergleich bit des einen Operanden mit dem jeweiligen bit des anderen operanden
# Beispiel zahl_fuenf ist binär 1*2^2 + 0 * 2^1 + 1*2^0 =5 ->  101   zahl_vier 1*2^2 + 0*2^1 +0 * 2^0 =4 -> 100
# bei xor -> 1 von zahl_fuenf mit 1 von zahl_vier ergibt 0, zweite bit von zahl_fuenf mit zweiten bit von zahl_vier ergebnis ist 0 , da zahl_fuenf an
# zweiter position  0 hat und zahl_vier auch 0 hat usw.. Insgesamt Ergebnis ist 001 Dezimal ist das 1

print("5 xor 4 ", 5 ^ 4)
# 5 | 4  5 -> 101 , 4 -> 100  Bit für Bit von links nach rechts 1 mit 1 ergibt 1, 0 mit 0 ergibt 0 , 1 mit 0 ergibt 1 -> 101 -> 1*2^2 + 0 * 2^1 + 1*2^0=5
print("5 or 4 ", 5 | 4)
# Übungsbeispiele 9 | 7 und 9 ^ 7 Ich kontrolliere streng , nein Scherz, jeder wie man mag
# ~ Hier werden die Bits geflippt(umgedreht). Aus 1 wird 0 und aus 0 wird 1
# Verschiebeoperatoren >> nach rechts werden die bits verschoben, links wird mit 0 aufgefüllt  <<  wird nach links verschoben
# Nach dem >> oder << Symbol schreibt man die Zahl, die angibt, um wieviel Positionen nach links oder rechts verschoben werden soll
# Beispiel  5 >> 2 oder 6 << 1
# Es gibt noch >>> . Der verschiebt auch nach rechts, aber Unterschied zu >> ist: es wird mit 1 von links aufgefüllt, wenn die zahl negativ ist
# wenn die zahl positiv ist, dann mit 0 (signed shift operator , der vorzeichen behaftete operator, das bedeutet, das Vorzeichen ändert sich nicht
# beim Verschieben) Erklärung: beim >> wird mit 0 von links aufgefüllt, das bedeutet, das Vorzeichen ändert sich, wenn man eine negative zahl hat,
# weil das erste linke bit gibt an, ob die Zahl negativ oder positiv ist. Wenn das erste Bit 1 ist, dann ist die Zahl negativ, bei 0 ist die zahl positiv.
# Anwendung hauptsächlich für Verschlüsselung ( z.B passwörter)

# Zuweisungsoperatoren
# Walrusoperator := sieht ein bisschen aus wie ein walrus ( Der Ausdruck rechts vom = wird ausgewertet und dann gleich der Variablen zugewiesen)
# Beispiel später bei den Funktionen
# Siehe Skript ** Operator Datenstruktur wird vervielfacht, kann angeben um wieviel. Hier Beispiel bei Zahlen,
# später noch andere Beispiele, bei Zahlen wird potenziert(mit Hochzahl gerechnet)
print("2**4", 2**4)
print ("2**5", 2**5)
# Stringverkettung
# Strings können direkt verkettet werden
print("wort_eins und wort_zwei untereinander verketten", wort_eins+wort_zwei)
wort_drei="Hallo "
wort_vier="Wie geht's?"
wort_fuenf = "wort_drei verkettet mit wort_vier ergibt "+(wort_drei+wort_vier)
# linksassoziativ wird ausgewertet, das bedeutet bei gleicher Operatorrangfolge von mindestens 2 Operatoren, wird immer von links
# nach rechts ausgewertet Beispiel a*b*c ist das gleiche wie (a*b)*c
print("Zuerst verkettung mit + und dann Speicherung in die variable)" ,wort_fuenf)
# Achtung Wenn einer der Datentypen kein String ist z.B ist int ist, dann muss bei der Verkettung mit +
# die Variable mit diesem Typ umgewandelt in ein string typ werden
# Umwandlung in string Typ mit str von zahl_neun
print("zahl_neun_text mit zahl_neun ",zahl_neun_text+str(zahl_neun))
# Rangfolge der Operatoren siehe https://www.delftstack.com/de/howto/python/order-of-operators-in-python/?utm_content=cmp-true
# Zu den Zuweisungsoperatoren +=, -= &= siehe Skriptum
zahl_elf = 11
zahl_elf += 9
# Dasselbe wie zahl_elf= zahl_elf+9
zahl_zwoelf = 12
zahl_zwoelf *= 2
# Dasselbe wie zahl_zwoelf = zahl_zwoelf * 2
wetter_gut &= sommer
# dasselbe wie wetter_gut= wetter_gut & sommer
# Übungsbeispiele
# W wetter_gut |= sommer und wetter_gut ^= sommer in der Langschreibweise.
# Dann Konkatenation von wetter_gut mit "Das Wetter ist gut" und Konkatenation von wetter_gut und sommer mit "Das Wetter ist gut un der Sommer"




