#Langschreibweise zu wetter_gut |= sommer und wetter_gut ^= sommer
wetter_gut = True
sommer = True
wetter_gut = wetter_gut | sommer
print("wetter_gut | sommer ", wetter_gut)
wetter_gut = wetter_gut ^ sommer
print("wetter_gut ^ sommer ",wetter_gut)
# Wichtig string umwandlung mit str nicht vergessen, sonst Fehler
print ("Das Wetter ist gut " + str(wetter_gut))
# Bitte selbst experementieren, das heißt in dem Fall verschiedene Operatoren nehmen z.B | ^ & und true oder false verschieden setzen
# 1.Lösung  Beide variablen in str umwandeln
print( "Das Wetter ist gut un der Sommer " + str(wetter_gut) + str(sommer))
#´2.Lösung str(wetter_gut+sommer) Zuerst beide verketten und dann in string umwandeln
# Hier wird gleich in die numerische Darstellung umgewandelt zuerst addiert und dann sofort in string umgewandelt. 1 bedetut True
# 0, 0.0 , "" wird zu False ausgewertet.
print("Das Wetter ist gut un der Sommer "+str(wetter_gut + sommer))
