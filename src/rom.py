"""ROM"""

ROM = [0] * 4096

# define chip8 font
SPRITES = [[0xF0, 0x90, 0xF0, 0X90, 0XF0], # 8
           [0xF0, 0x90, 0xF0, 0x10, 0xF0], # 9
           [0xF0, 0x90, 0x90, 0x90, 0xF0], # 0
           [0x20, 0x60, 0x20, 0x20, 0x70], # 1
           [0xF0, 0x90, 0xF0, 0x90, 0x90], # A
           [0xE0, 0x90, 0xE0, 0x90, 0xE0], # B
           [0xF0, 0x10, 0xF0, 0x80, 0xF0], # 2
           [0xF0, 0x10, 0xF0, 0x10, 0xF0]] # 3

# copy over sprites into ROM space
for i, n in enumerate(SPRITES[0]):
    ROM[i] = n

for i, n in enumerate(SPRITES[1]):
    ROM[i+8] = n

for i, n in enumerate(SPRITES[2]):
    ROM[i+16] = n

for i, n in enumerate(SPRITES[3]):
    ROM[i+24] = n

for i, n in enumerate(SPRITES[4]):
    ROM[i+32] = n

for i, n in enumerate(SPRITES[5]):
    ROM[i+40] = n

for i, n in enumerate(SPRITES[6]):
    ROM[i+48] = n

for i, n in enumerate(SPRITES[7]):
    ROM[i+56] = n
