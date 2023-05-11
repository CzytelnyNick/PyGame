import pygame
import time

class Enemy:
    def __init__(self, player_x, player_y, enemy_x, enemy_y):
        
        self.player_x = player_x
        self.player_y = player_y
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
    # def walkSwordAttack(self):
        
    
    def samurai(self, screen, enemy_x, player_x):
        print(self.enemy_x)
        enemy_x+=1
        


