import pygame
import os

class Mario(pygame.sprite.Sprite):
    """ player controlled Mario """
    def __init__(self, y, x):
        """ instantiate instance attributes """
        super().__init__()
        image = pygame.image.load_extended(os.path.join('sprites', 'mario.png'))
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


    def update(self, y, x):
        """ moves mario to the specified x, y coordinates """
        self.rect.y = y
        self.rect.x = x


class OneUp(pygame.sprite.Sprite):
    """ 1up mushroom item randomly found in maze """
    def __init__(self, y, x):
        """ instantiate instance attributes """
        super().__init__()
        self._image = pygame.image.load(os.path.join('sprites', '1up.png'))
        self.image = pygame.transform.scale(self._image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


    def update(self, y, x):
        """ moves 1up mushroom to the specified x, y coordinates """
        self.image = pygame.transform.scale(self._image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class FireFlower(pygame.sprite.Sprite):
    """ fire flower item randomly found in maze """
    def __init__(self, y, x):
        """ instantiate instance attributes """
        super().__init__()
        self._image = pygame.image.load(os.path.join('sprites', 'fire_flower.png'))
        self.image = pygame.transform.scale(self._image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


    def update(self, y, x):
        """ moves fire flower to the specified x, y coordinates """
        self.image = pygame.transform.scale(self._image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Mushroom(pygame.sprite.Sprite):
    """ mushroom item randomly found in maze """
    def __init__(self, y, x):
        """ instantiate instance attributes """
        super().__init__()
        self._image = pygame.image.load(os.path.join('sprites', 'mushroom.png'))
        self.image = pygame.transform.scale(self._image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self, y, x):
        """ moves mushroom to the specified x, y coordinates and shrinks it """
        self.image = pygame.transform.scale(self._image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Star(pygame.sprite.Sprite):
    """ star item randomly found in maze """
    def __init__(self, y, x):
        """ instantiate instance attributes """
        super().__init__()
        self._image = pygame.image.load(os.path.join('sprites', 'star.png'))
        self.image = pygame.transform.scale(self._image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


    def update(self, y, x):
        """ moves star to the specified x, y coordinates and shrinks it """
        self.image = pygame.transform.scale(self._image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Brick(pygame.sprite.Sprite):
    """ wall that surrounds the items and player """
    def __init__(self, y, x):
        super().__init__()
        image = pygame.image.load(os.path.join('sprites', 'brick.png'))
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Pipe(pygame.sprite.Sprite):
    """ the exit the player must reach """
    def __init__(self, y, x):
        """ instantiate instance attributes """
        super().__init__()
        image = pygame.image.load(os.path.join('sprites', 'pipe.png'))
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x