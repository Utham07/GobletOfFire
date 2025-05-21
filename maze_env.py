import random
import pygame

class MazeEnvironment:
    def __init__(self, maze_file, num_death_eaters=1):
        self.load_maze(maze_file)
        self.num_death_eaters = num_death_eaters
        self.reset()

    def load_maze(self, maze_file):
        with open(maze_file, 'r') as f:
            self.maze = [list(line.strip()) for line in f.readlines()]

        self.height = len(self.maze)
        self.width = len(self.maze[0])
        self.walls = set()
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 'X':
                    self.walls.add((y, x))

    def find_random_empty_cell(self, exclude=set()):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            pos = (y, x)
            if pos not in self.walls and pos not in exclude:
                return pos

    def reset(self):
        self.harry_pos = self.find_random_empty_cell()
        used_positions = {self.harry_pos}

        self.death_eaters_pos = []
        for _ in range(self.num_death_eaters):
            pos = self.find_random_empty_cell(exclude=used_positions)
            self.death_eaters_pos.append(pos)
            used_positions.add(pos)

        self.cup_pos = self.find_random_empty_cell(exclude=used_positions)
        self.done = False
        return self.harry_pos

    def step(self, action):
        if self.done:
            return self.harry_pos, 0, True

        y, x = self.harry_pos
        new_y, new_x = y, x

        if action == 0: new_y = max(0, y - 1)
        elif action == 1: new_y = min(self.height - 1, y + 1)
        elif action == 2: new_x = max(0, x - 1)
        elif action == 3: new_x = min(self.width - 1, x + 1)

        if (new_y, new_x) not in self.walls:
            self.harry_pos = (new_y, new_x)

        # Optional: slip chance
        if random.random() < 0.1:
            y, x = self.harry_pos
            slip_y, slip_x = y, x
            if action == 0: slip_y = max(0, y - 1)
            elif action == 1: slip_y = min(self.height - 1, y + 1)
            elif action == 2: slip_x = max(0, x - 1)
            elif action == 3: slip_x = min(self.width - 1, x + 1)
            if (slip_y, slip_x) not in self.walls:
                self.harry_pos = (slip_y, slip_x)

        if self.harry_pos == self.cup_pos:
            self.done = True
            return self.harry_pos, 10, True

        new_death_positions = []
        for (dy, dx) in self.death_eaters_pos:
            target_y, target_x = dy, dx
            hy, hx = self.harry_pos

            if dy < hy and (dy + 1, dx) not in self.walls:
                target_y += 1
            elif dy > hy and (dy - 1, dx) not in self.walls:
                target_y -= 1

            if dx < hx and (target_y, dx + 1) not in self.walls:
                target_x += 1
            elif dx > hx and (target_y, dx - 1) not in self.walls:
                target_x -= 1

            new_death_positions.append((target_y, target_x))

            if (target_y, target_x) == self.harry_pos:
                self.done = True
                return self.harry_pos, -10, True

        self.death_eaters_pos = new_death_positions
        return self.harry_pos, -1, False

    def render(self, screen):
        cell_size = 40
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                color = (0, 0, 0) if (y, x) in self.walls else (255, 255, 255)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        hy, hx = self.harry_pos
        harry_rect = pygame.Rect(hx * cell_size, hy * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (0, 255, 0), harry_rect)

        for dy, dx in self.death_eaters_pos:
            rect = pygame.Rect(dx * cell_size, dy * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 0, 0), rect)

        cy, cx = self.cup_pos
        cup_rect = pygame.Rect(cx * cell_size, cy * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 255, 0), cup_rect)

        pygame.display.update()
