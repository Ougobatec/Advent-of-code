#!/usr/bin/env python3
"""
Script utilitaire pour exécuter facilement les solutions Advent of Code.

Usage:
    ./run.py --latest     # Exécute la dernière solution implémentée
    ./run.py --list 2015  # Liste les solutions implémentées pour 2015
    ./run.py 2015 1       # Exécute la solution du jour 1 de l'année 2015
"""

import os
import sys
import argparse

# Codes couleurs ANSI
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

def is_template(file_path):
    """Vérifie si un fichier est encore un template."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return 'TODO: Implémenter la solution' in content
    except:
        return True

def get_implemented_solutions(year):
    """Retourne la liste des solutions implémentées pour une année."""
    if not os.path.exists(str(year)):
        return []
    
    implemented = []
    for day in range(1, 26):
        solution_path = f"{year}/{day:02d}/solutions.py"
        if os.path.exists(solution_path) and not is_template(solution_path):
            implemented.append(day)
    return implemented

def find_latest_solution():
    """Trouve la dernière solution implémentée."""
    years = sorted([int(d) for d in os.listdir('.') if d.isdigit() and os.path.isdir(d)], reverse=True)
    
    for year in years:
        implemented = get_implemented_solutions(year)
        if implemented:
            return year, max(implemented)
    return None, None

def list_solutions(year):
    """Liste les solutions implémentées pour une année."""
    implemented = get_implemented_solutions(year)
    
    if not os.path.exists(str(year)):
        print(f"{BOLD}[!] {RED}L'année {year} n'existe pas.{RESET}")
        return
    
    if implemented:
        print(f"{BOLD}[*] Solutions implémentées pour {year}: {GREEN}{', '.join(map(str, implemented))}{RESET}")
        return
    else:
        print(f"{BOLD}[!] {RED}Aucune solution implémentée pour {year}{RESET}")
        return

def run_solution(year, day):
    """Exécute une solution."""
    solution_path = f"{year}/{day:02d}/solutions.py"
    
    if not os.path.exists(solution_path):
        print(f"{BOLD}[!] {RED}{solution_path} n'existe pas.{RESET}")
        return
    
    if is_template(solution_path):
        print(f"{BOLD}[!] {RED}La solution {year} jour {day} n'est pas encore implémentée (template vide).{RESET}")
        return
    
    print(f"{BOLD}[*] {CYAN}{year} - Jour {day}{RESET}")
    
    original_cwd = os.getcwd()
    try:
        # Aller dans le répertoire de la solution et charger le module
        os.chdir(f"{year}/{day:02d}")
        
        import importlib.util
        spec = importlib.util.spec_from_file_location("solution", "solutions.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Exécuter
        data = module.load_input()
        sol1 = module.part1(data)
        sol2 = module.part2(data)
        
        # Afficher
        print(f"\n=== Résultats ===")
        print(f"{BOLD}{GREEN}Partie 1:{RESET} {sol1}")
        print(f"{BOLD}{GREEN}Partie 2:{RESET} {sol2}")
        
        return
        
    except Exception as e:
        print(f"{BOLD}[!] {RED}Erreur: {e}{RESET}")
        return
    finally:
        os.chdir(original_cwd)

def main():
    parser = argparse.ArgumentParser(description="Exécuter les solutions Advent of Code")
    parser.add_argument('year', nargs='?', type=int, help='Année')
    parser.add_argument('day', nargs='?', type=int, help='Jour')
    parser.add_argument('--latest', action='store_true', help='Dernière solution implémentée')
    parser.add_argument('--list', type=int, metavar='YEAR', help='Liste les solutions pour une année')
    
    args = parser.parse_args()
    
    if args.list:
        list_solutions(args.list)
        return
    
    if args.latest:
        year, day = find_latest_solution()
        if year is None:
            print(f"{BOLD}[!] {RED}Aucune solution implémentée trouvée.{RESET}")
            return
    elif args.year and args.day:
        year, day = args.year, args.day
    else:
        parser.print_help()
        return
    
    if not run_solution(year, day):
        return


if __name__ == "__main__":
    sys.exit(main())
