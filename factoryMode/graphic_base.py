# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 上午11:56
# @Author  : chaos
# @FileName: graphic_base.py
# @Software: PyCharm
import pygame


class Shape(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        raise NotImplementedError()

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        if direction == 'down':
            self.y += 4
        if direction == 'left':
            self.x -= 4
        if direction == 'right':
            self.x += 4

    @staticmethod
    def factory(type):
        if type == 'Circle':
            return Circle(100, 100, screen)
        if type == "Square":
            return Square(100, 100, screen)
        assert 0, "Bad type requested" + type

class Square(Shape):
    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x, self.y, 20, 20))
        print(self.screen)
        print(self.x)
        print(self.y)


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 10)
        print(self.screen)
        print(self.x)
        print(self.y)


if __name__ == "__main__":
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)

    # square = Square(100, 100, screen)
    obj = Shape.factory('Circle')
    player_quits = False

    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                obj.move('up')
            if pressed[pygame.K_DOWN]:
                obj.move('down')
            if pressed[pygame.K_LEFT]:
                obj.move('left')
            if pressed[pygame.K_RIGHT]:
                obj.move('right')

            screen.fill((0, 0, 0))
            obj.draw()

        pygame.display.flip()
