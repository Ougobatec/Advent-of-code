#!/usr/bin/env python3
# Solutions pour le jour 03 de l'Advent of Code 2025

from pathlib import Path
import re

def load_input():
    """Charge les données d'entrée."""
    return Path(__file__).parent.joinpath("input.txt").read_text()

def part1(data):
    """Résout la partie 1."""
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    return sum(int(x) * int(y) for x, y in matches)

def part2(data):
    """Résout la partie 2."""
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, data)
    
    result = 0
    enabled = True
    
    for match in matches:
        if match[0] and enabled:  # mul(x,y) et activé
            result += int(match[1]) * int(match[2])
        elif match[3]:  # do()
            enabled = True
        elif match[4]:  # don't()
            enabled = False
            
    return result

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
