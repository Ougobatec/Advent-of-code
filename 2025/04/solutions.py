#!/usr/bin/env python3
# Solutions pour le jour 04 de l'Advent of Code 2025

from pathlib import Path

def load_input():
    """Charge les données d'entrée."""
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')

def is_valid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def part1(data):
    """Résout la partie 1."""
    rows, cols = len(data), len(data[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    word = "XMAS"
    
    def check_word(start_r, start_c, dr, dc):
        return all(
            is_valid(start_r + i * dr, start_c + i * dc, rows, cols) and
            data[start_r + i * dr][start_c + i * dc] == word[i]
            for i in range(4)
        )
    
    return sum(
        check_word(i, j, dr, dc)
        for i in range(rows)
        for j in range(cols)
        if data[i][j] == 'X'
        for dr, dc in directions
    )

def part2(data):
    """Résout la partie 2."""
    rows, cols = len(data), len(data[0])
    
    def check_x_mas(center_r, center_c):
        if data[center_r][center_c] != 'A':
            return False
        
        corners = [
            (center_r - 1, center_c - 1),  # top-left
            (center_r - 1, center_c + 1),  # top-right
            (center_r + 1, center_c - 1),  # bottom-left
            (center_r + 1, center_c + 1)   # bottom-right
        ]
        
        if not all(is_valid(r, c, rows, cols) for r, c in corners):
            return False
        
        tl, tr, bl, br = [data[r][c] for r, c in corners]
        
        diag1, diag2 = tl + 'A' + br, tr + 'A' + bl
        return diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}
    
    return sum(
        check_x_mas(i, j)
        for i in range(1, rows - 1)
        for j in range(1, cols - 1)
    )

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
