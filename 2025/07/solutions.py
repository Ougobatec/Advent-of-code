#!/usr/bin/env python3
# Solutions pour le jour 07 de l'Advent of Code 2025

from pathlib import Path
import itertools

def load_input():
    """Charge les données d'entrée."""
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')

def calculate(nums, op, size, p2):
    ans = nums[0]
    for j in range(size):
        if op[j] == "0": 
            ans += nums[j+1]
        elif op[j] == "1": 
            ans *= nums[j+1]
        elif p2 and op[j] == "2": 
            ans = int(f"{ans}{nums[j+1]}")
    return ans

def part1(data):
    """Résout la partie 1."""
    res1 = 0
    for line in data:
        val = int(line.split(":")[0])
        nums = list(map(int, line.split(":")[1].split()))
        size = len(nums) - 1
        for op in itertools.product("01", repeat=size):
            if calculate(nums, op, size, False) == val:
                res1 += val
                break
    return res1

def part2(data):
    """Résout la partie 2."""
    res2 = 0
    for line in data:
        val = int(line.split(":")[0])
        nums = list(map(int, line.split(":")[1].split()))
        size = len(nums) - 1
        for op in itertools.product("012", repeat=size):
            if calculate(nums, op, size, True) == val:
                res2 += val
                break
    return res2

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
