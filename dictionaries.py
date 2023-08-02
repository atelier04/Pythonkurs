# Dictionaries sind datenstrukturen(Objekte), die  sogenannnte Schlüssel Werte Paare sind
mein_dict = {"name": "Dominique", "charakter": "guter Mensch", "hobbies": ["Kochen", "Kunst", "Schwimmen"]}
# mein_dict ist iterable und veränderbar
for element in mein_dict:
    print(f"element {element}")  # nur Ausgabe der Schlüsseln
    """element name
    element charakter
    element hobbies
    """
for key, value in mein_dict.items():
    if key == "hobbies":
        print(f" Die hobbies sind {value}")
        print(f" Das 2.te Hobby ist {value[1]}")
    #print(f" Der Schlüssel ist {key} und der Wert ist {value}")
