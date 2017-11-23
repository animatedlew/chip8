"""ROM"""

ROM = [0] * 4096

# define chip-8 font
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
    ROM[i+5] = n

for i, n in enumerate(SPRITES[2]):
    ROM[i+10] = n

for i, n in enumerate(SPRITES[3]):
    ROM[i+15] = n

for i, n in enumerate(SPRITES[4]):
    ROM[i+20] = n

for i, n in enumerate(SPRITES[5]):
    ROM[i+25] = n

for i, n in enumerate(SPRITES[6]):
    ROM[i+30] = n

for i, n in enumerate(SPRITES[7]):
    ROM[i+35] = n

# assert the burn was successful
assert ROM[:8*5] == sum(SPRITES, [])

# test jumps
ROM[0x200] = 0x1202 # JP
ROM[0x202] = 0x1206 # JP
ROM[0x204] = 0x1208 # JP
ROM[0x206] = 0x1204 # JP
