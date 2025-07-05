#!/usr/bin/env python3
# Solutions pour le jour 05 de l'Advent of Code 2025

from pathlib import Path
from collections import defaultdict
from functools import cmp_to_key

def load_input():
    """Charge les données d'entrée."""
    data = Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')

    sep_index = data.index("")
    rules = defaultdict(set)
    for line in data[:sep_index]:
        before, after = map(int, line.split('|'))
        rules[before].add(after)
    updates = [list(map(int, line.split(","))) for line in data[sep_index + 1:] if line.strip()]
    
    return dict(rules), updates

def is_correct_order(update, rules):
    position = {page: i for i, page in enumerate(update)}
    
    for before_page in update:
        if before_page in rules:
            for after_page in rules[before_page]:
                if after_page in position:
                    if position[after_page] < position[before_page]:
                        return False
    return True

def sort_update(update, rules):
    def compare_pages(a, b):
        if a in rules and b in rules[a]:
            return -1
        if b in rules and a in rules[b]:
            return 1
        return 0
    
    return sorted(update, key=cmp_to_key(compare_pages))

def part1(data):
    """Résout la partie 1."""
    rules, updates = data
    return sum(update[len(update) // 2] for update in updates if is_correct_order(update, rules))

def part2(data):
    """Résout la partie 2."""
    rules, updates = data
    total = 0
    for update in updates:
        if not is_correct_order(update, rules):
            sorted_update = sort_update(update, rules)
            total += sorted_update[len(sorted_update) // 2]
    return total

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
