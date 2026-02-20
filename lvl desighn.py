# https://drive.google.com/drive/folders/1YW_zdCwxjftvLXRHMnyMpEJlpuUF8Swy
import pygame.display
from PIL.ImageChops import offset
from pygame import *

init()

size = 1000, 700
window = display.set_mode(size)
clock = time.Clock()


class Block:
   def __init__(self, img_path, width, height):
       global blocks
       self.image = transform.scale(image.load(img_path), (width, height))
       self.width = width
       self.height = height
       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = 0
       blocks.append(self)

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
       draw.rect(window, (255, 0, 0), self.rect, 2)

blocks = []
block1 = Block('kartinki/medium_rock.png', 850, 850)
block1.reset()

select_block = None
offsetx = 0
offsety = 0

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            x, y = e.pos
            if block1.rect.collidepoint(x, y):
                select_block = block1
                offsetx = block1.rect.x
                offsety = block1.rect.y
                break

        if e.type == MOUSEBUTTONUP:
            select_block = None

        if e.type == MOUSEMOTION and select_block:
            x, y = e.pos
            select_block.rect.x = x - offsetx
            select_block.rect.y = y - offsety

    window.fill((255,255,255))
    block1.reset()
    pygame.display.update()
    clock.tick(60)