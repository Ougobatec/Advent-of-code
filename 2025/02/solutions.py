#!/usr/bin/env python3
# Solutions pour le jour 02 de l'Advent of Code 2025

from pathlib import Path

def load_input():
    """Charge les données d'entrée."""
    data = Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')
    return [list(map(int, line.split())) for line in data if line.strip()]

def is_safe(levels):
    if not (levels == sorted(levels) or levels == sorted(levels, reverse=True)):
        return False
    return all(1 <= abs(levels[i] - levels[i+1]) <= 3 for i in range(len(levels) - 1))

def part1(data):
    """Résout la partie 1."""
    return sum(1 for report in data if is_safe(report))

def part2(data):
    """Résout la partie 2."""
    def is_safe_with_dampener(report):
        return is_safe(report) or any(
            is_safe(report[:i] + report[i+1:]) 
            for i in range(len(report))
        )
    
    return sum(1 for report in data if is_safe_with_dampener(report))

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
