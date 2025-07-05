#!/usr/bin/env python3
# Solutions pour le jour 04 de l'Advent of Code 2019

from pathlib import Path

def load_input():
    """Charge les données d'entrée."""
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')

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
