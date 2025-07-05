#!/usr/bin/env python3
"""
Script pour générer la structure de dossiers pour l'Advent of Code.
Ce script crée les dossiers pour chaque année et jour, ainsi que les fichiers
`solutions.py` et `input.txt` pour chaque jour.
"""

import os
import datetime

# Codes couleurs ANSI
GREEN = '\033[92m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

print(f"{BOLD}[*] {CYAN}Configuration de l'environnement Advent of Code...{RESET}")

created_count = 0

def create_solution_template(year, day):
    """Crée le template de solution."""
    return f'''#!/usr/bin/env python3
# Solutions pour le jour {day:02d} de l'Advent of Code {year}

from pathlib import Path

def load_input():
    """Charge les données d'entrée."""
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\\n')

def part1(data):
    """Résout la partie 1."""
    # TODO: Implémenter la solution
    return 0

def part2(data):
    """Résout la partie 2."""
    # TODO: Implémenter la solution
    return 0

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
'''

now = datetime.datetime.now().year

for year in range(2015, now + 1):
    os.makedirs(str(year), exist_ok=True)
    
    for day in range(1, 26):
        path = f"{year}/{day:02d}"
        os.makedirs(path, exist_ok=True)
        
        solutions_path = f"{path}/solutions.py"
        input_path = f"{path}/input.txt"

        if not os.path.exists(solutions_path):
            with open(solutions_path, 'w', encoding='utf-8') as f:
                f.write(create_solution_template(year, day))
            created_count += 1
        
        if not os.path.exists(input_path):
            open(input_path, 'w').close()
            created_count += 1

print(f"{BOLD}[*] {GREEN}Structure générée - {created_count} fichiers créés{RESET}")
print("")
print("Commandes utiles :")
print(f"  {BOLD}./run.py --latest{RESET}         # Dernière solution")
print(f"  {BOLD}./run.py --list 2015{RESET}      # Solutions de 2015")
print(f"  {BOLD}./run.py 2015 1{RESET}           # Solution spécifique")