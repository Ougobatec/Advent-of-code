#!/usr/bin/env python3
# Solutions pour le jour 06 de l'Advent of Code 2025

from pathlib import Path

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

def load_input():
    """Charge les données d'entrée."""
    return Path(__file__).parent.joinpath("input.txt").read_text().strip().split('\n')

def find_guard_position(lines):
    for i, line in enumerate(lines):
        if "^" in line:
            return (i, line.index("^"))

def is_valid_position(pos, lines):
    return 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[0])

def simulate_guard_movement(lines, start_position, start_direction, obstacle_pos=None):
    pos, direction = start_position, start_direction
    visited = {}
    
    while True:
        if pos in visited and direction in visited[pos]:
            return True, visited
        visited.setdefault(pos, []).append(direction)
        next_pos = (pos[0] + DIRECTIONS[direction][0], pos[1] + DIRECTIONS[direction][1])
        if not is_valid_position(next_pos, lines):
            return False, visited
        is_obstacle = (lines[next_pos[0]][next_pos[1]] == "#" or (obstacle_pos and next_pos == obstacle_pos))
        if is_obstacle:
            direction = (direction + 1) % 4
        else:
            pos = next_pos

def find_loop_creating_obstacles(lines, start_position, start_direction, valid_positions):
    loop_obstacles = set()
    
    for pos in valid_positions:
        if pos == start_position or lines[pos[0]][pos[1]] == "#":
            continue
        is_loop, _ = simulate_guard_movement(lines, start_position, start_direction, pos)
        if is_loop:
            loop_obstacles.add(pos)
    
    return loop_obstacles

def part1(data):
    """Résout la partie 1."""
    lines = [list(line) for line in data]
    start_position = find_guard_position(lines)
    start_direction = NORTH
    is_loop, visited_positions = simulate_guard_movement(lines, start_position, start_direction)
    return len(visited_positions)

def part2(data):
    """Résout la partie 2."""
    lines = [list(line) for line in data]
    start_position = find_guard_position(lines)
    start_direction = NORTH
    _, visited_positions = simulate_guard_movement(lines, start_position, start_direction)
    candidate_positions = set(visited_positions.keys())
    loop_obstacles = find_loop_creating_obstacles(lines, start_position, start_direction, candidate_positions)
    return len(loop_obstacles)

if __name__ == "__main__":
    data = load_input()
    
    sol1 = part1(data)
    print("La première réponse est", sol1)
    
    sol2 = part2(data)
    print("La deuxième réponse est", sol2)
