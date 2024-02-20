import pygame as pg



class Motor:
    def __init__(self, x, y, w, h, Surface) -> None:
        """x and y are the center coordinates of the motor in the local frame"""
        self.x = x
        self.y = y
        self.image = pg.Surface((w, h))
        self.image.fill('black')
        self.rect = self.image.get_rect(center=(x, y))

        Surface.blit(self.image, self.rect)
        
        self.radius = w/2
        self.angular_speed = 5 # rad/s
      

    def get_speed(self, direction):
        """direction is either 1 or -1"""
        return direction * self.angular_speed * self.radius
    