#!/usr/bin/env python3
# Solutions pour le jour 01 de l'Advent of Code 2025

from pathlib import Path

def load_input():
    """Charge les données d'entrée."""
    data = Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')
    pairs = [list(map(int, line.split())) for line in data if line.strip()]
    return [pair[0] for pair in pairs], [pair[1] for pair in pairs]

def part1(data):
    """Résout la partie 1."""
    list1, list2 = data
    return sum(abs(a - b) for a, b in zip(sorted(list1), sorted(list2)))

def part2(data):
    """Résout la partie 2."""
    list1, list2 = data
    return sum(num * list2.count(num) for num in list1)

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
