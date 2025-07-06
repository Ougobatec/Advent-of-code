#!/usr/bin/env python3
# Solutions pour le jour 08 de l'Advent of Code 2025

from pathlib import Path
from typing import Dict, List, Set, Tuple
from itertools import combinations

def load_input():
    """Charge les données d'entrée."""
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')

def parse_antennas(grid: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    antennas = {}
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char != ".":
                antennas.setdefault(char, []).append((row, col))
    return antennas

def is_in_bounds(pos: Tuple[int, int], grid: List[str]) -> bool:
    row, col = pos
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def calculate_antinodes_part1(antenna1: Tuple[int, int], antenna2: Tuple[int, int]) -> List[Tuple[int, int]]:
    r1, c1 = antenna1
    r2, c2 = antenna2
    dr, dc = r1 - r2, c1 - c2
    return [
        (r1 + dr, c1 + dc),
        (r2 - dr, c2 - dc)
    ]

def calculate_antinodes_part2(antenna1: Tuple[int, int], antenna2: Tuple[int, int], grid: List[str]) -> List[Tuple[int, int]]:
    r1, c1 = antenna1
    r2, c2 = antenna2
    dr, dc = r1 - r2, c1 - c2
    antinodes = []
    n = 0
    while True:
        pos = (r1 + n * dr, c1 + n * dc)
        if not is_in_bounds(pos, grid):
            break
        antinodes.append(pos)
        n += 1
    n = 1
    while True:
        pos = (r2 - n * dr, c2 - n * dc)
        if not is_in_bounds(pos, grid):
            break
        antinodes.append(pos)
        n += 1
    return antinodes

def part1(data):
    """Résout la partie 1."""
    lines = data
    freq = {}
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char != ".":
                freq.setdefault(char, []).append((x, y))
    antinodes = set()
    
    for frequencies in freq:
        antennas = freq[frequencies]
        for a in antennas:
            for b in antennas:
                if a != b:
                    vect = (a[0] - b[0], a[1] - b[1])
                    antinode = (a[0] + vect[0], a[1] + vect[1])
                    if 0 <= antinode[0] < len(lines) and 0 <= antinode[1] < len(lines[0]):
                        antinodes.add(antinode)
    return len(antinodes)

def part2(data):
    """Résout la partie 2."""
    lines = data
    freq = {}
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char != ".":
                freq.setdefault(char, []).append((x, y))
    antinodes = set()
    
    for frequencies in freq:
        antennas = freq[frequencies]
        for a in antennas:
            for b in antennas:
                if a != b:
                    vect = (a[0] - b[0], a[1] - b[1])
                    for n in range(len(lines)):
                        p1 = (a[0] + n*vect[0], a[1] + n*vect[1])
                        p2 = (b[0] - n*vect[0], b[1] - n*vect[1])
                        for p in (p1, p2):
                            if 0 <= p[0] < len(lines) and 0 <= p[1] < len(lines[0]):
                                antinodes.add(p)
    return len(antinodes)

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
