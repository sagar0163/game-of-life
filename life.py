#!/usr/bin/env python3
"""
Conway's Game of Life - Terminal implementation
Author: Sagar Jadhav
"""

import os
import random
import time
import keyboard

WIDTH = 40
HEIGHT = 20
ALIVE = '██'
DEAD = '  '

class GameOfLife:
    def __init__(self, width=WIDTH, height=HEIGHT, randomize=True):
        self.width = width
        self.height = height
        self.generation = 0
        self.paused = False
        
        if randomize:
            self.grid = [[random.choice([True, False]) for _ in range(width)] for _ in range(height)]
        else:
            self.grid = [[False for _ in range(width)] for _ in range(height)]
    
    def count_neighbors(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = (x + dx) % self.width, (y + dy) % self.height
                if self.grid[ny][nx]:
                    count += 1
        return count
    
    def next_generation(self):
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                
                if self.grid[y][x]:
                    new_grid[y][x] = neighbors in [2, 3]
                else:
                    new_grid[y][x] = neighbors == 3
        
        self.grid = new_grid
        self.generation += 1
    
    def draw(self):
        os.system('clear')
        print("╔" + "═" * self.width * 2 + "╗")
        for row in self.grid:
            line = "║"
            for cell in row:
                line += ALIVE if cell else DEAD
            line += "║"
            print(line)
        print("╚" + "═" * self.width * 2 + "╝")
        print(f"Generation: {self.generation} | Space: pause | R: random | C: clear | Q: quit")
    
    def clear(self):
        self.grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.generation = 0
    
    def randomize(self):
        self.grid = [[random.choice([True, False]) for _ in range(self.width)] for _ in range(self.height)]
        self.generation = 0

PRESETS = {
    'glider': [(1, 1), (2, 2), (2, 3), (3, 1), (3, 2)],
    'blinker': [(5, 5), (5, 6), (5, 7)],
    'block': [(10, 10), (10, 11), (11, 10), (11, 11)],
    'lwss': [(0, 4), (0, 5), (0, 6), (0, 7), (1, 3), (1, 7), (2, 7), (3, 3), (3, 6), (4, 4), (4, 5), (4, 6)],
}

def main():
    game = GameOfLife()
    speed = 0.1
    
    while True:
        game.draw()
        
        if not game.paused:
            game.next_generation()
            time.sleep(speed)
        
        if keyboard.is_pressed('space'):
            game.paused = not game.paused
            time.sleep(0.2)
        elif keyboard.is_pressed('r'):
            game.randomize()
            time.sleep(0.1)
        elif keyboard.is_pressed('c'):
            game.clear()
            time.sleep(0.1)
        elif keyboard.is_pressed('q'):
            break

if __name__ == '__main__':
    main()
