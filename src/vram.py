"""VIDEO MODULE"""
# pylint: disable=W0603

FRAMEBUFFER = [[0] * (64//8)] * 32 # 64x32 1-bit frame buffer

def clear():
    "cls"
    global FRAMEBUFFER
    FRAMEBUFFER = [[0] * (64//8)] * 32
