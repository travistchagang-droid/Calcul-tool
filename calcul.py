# calcul.py - Calculatrice simple

def calculer(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Erreur : division par zéro"
    else:
        return "Opération invalide"

a = 6
b = 3
operation = "+"

resultat = calculer(a, b, operation)
print(f"Résultat : {a} {operation} {b} = {resultat}")
