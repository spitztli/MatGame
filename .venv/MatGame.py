import random
from Operatoren import operatoren


# Mathe spiel das stets erweitert wird

print("Herzlich Willkommen und viel Spass beim spiel!")
benutzer = input("Bitte geben Sie ihren Name ein: ")
print("Hallo", benutzer)
runden = int(input("Wie viel runden möchten sie spielen? "))
eingabe = input("Welche Operatoren Aufgaben möchten sie machen?\nAdditionen = A\nSubtraktionen = S\nMultiplikationen = M\nDivisionen = D\n: ")

user_points = 0
round_counter = 0
#operatoren_wahl = [["Additionen", "A"], ["Subtraktionen", "S"], ["Multiplikationen", "M"], ["Divisionen", "D"]]

operatoren(eingabe, runden)

print("Ende")



