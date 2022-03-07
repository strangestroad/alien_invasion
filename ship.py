import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,s,screen):
        super(Ship,self).__init__()
        self.screen=screen
        self.s=s

        self.image=pygame.image.load('image/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #store a decimal value for the ship's center
        self.center=float(self.rect.centerx)

        #Movement flag
        self.moving_right=False
        self.moving_left=False
    def update(self):
        """Update the ship's position based on the movemnet flag"""
        #update the ship's center value, not the rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.s.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.s.ship_speed_factor
        #update rect object from self.center
        self.rect.centerx=self.center

    def center_ship(self):
        """Center the ship on the screen"""
        self.center=self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image,self.rect)
