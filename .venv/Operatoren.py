import random

def operatoren(eingabe, runden):
    user_points = 0
    round_counter = 0
    if eingabe == "A" or "S" or "M" or "D":
        # Additionen
        if eingabe == "A":
            while round_counter < runden:
                x = random.randint(0, 10)
                y = random.randint(0, 10)
                r = x + y
                result = int(input("Was gibt {} + {}: ".format(x, y)))
                if result == r:
                    print("Die Antwort ist Richtig")
                    round_counter += 1
                    user_points += 1
                else:
                    print("Flasch! Das Ergebnis ist:", r)
                    round_counter += 1
            print("Sie haben", user_points, "von", runden, "Aufgaben richtig gelöst")
        # Subtraktionen
        if eingabe == "S":
            while round_counter < runden:
                x = random.randint(0, 10)
                y = random.randint(0, 10)
                r = x - y
                result = int(input("Was gibt {} - {}: ".format(x, y)))
                if result == r:
                    print("Die Antwort ist Richtig")
                    round_counter += 1
                    user_points += 1
                else:
                    print("Flasch! Das Ergebnis ist:", r)
                    round_counter += 1
            print("Sie haben", user_points, "von", runden, "Aufgaben richtig gelöst")

        # Multiplikation
        if eingabe == "M":
            while round_counter < runden:
                x = random.randint(0, 10)
                y = random.randint(0, 10)
                r = x * y
                result = int(input("Was gibt {} * {}: ".format(x, y)))
                if result == r:
                    print("Die Antwort ist Richtig")
                    round_counter += 1
                    user_points += 1
                else:
                    print("Flasch! Das Ergebnis ist:", r)
                    round_counter += 1
            print("Sie haben", user_points, "von", runden, "Aufgaben richtig gelöst")
        # Division
        if eingabe == "D":
            while round_counter < runden:
                x = random.randint(0, 10)
                y = random.randint(0, 10)
                r = x / y
                result = float(input("Was gibt {} / {}: ".format(x, y)))
                if result == r:
                    print("Die Antwort ist Richtig")
                    round_counter += 1
                    user_points += 1
                else:
                    print("Flasch! Das Ergebnis ist:", r)
                    round_counter += 1
            print("Sie haben", user_points, "von", runden, "Aufgaben richtig gelöst")