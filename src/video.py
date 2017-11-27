"""VIDEO MODULE"""
# pylint: disable=W0603

import pygame
from pygame.locals import *

FRAMEBUFFER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] * 64 # 128x64 1-bit frame buffer

Hz = 60
clock = pygame.time.Clock()

def clear():
    "cls"
    global FRAMEBUFFER
    FRAMEBUFFER = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] * 64
