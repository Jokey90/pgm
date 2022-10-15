import pygame
from tiles import Player, Rock
from settings import *


class Level:
    def __init__(self) -> None:

        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self) -> None:
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'x':
                    Rock((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self) -> None:
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
