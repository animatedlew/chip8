"""ROM"""

ROM = [0] * 4096

# define chip-8 font
SPRITES = [0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
           0x20, 0x60, 0x20, 0x20, 0x70, # 1
           0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
           0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
           0x90, 0x90, 0xF0, 0x10, 0x10, # 4
           0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
           0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
           0xF0, 0x10, 0x20, 0x40, 0x40, # 7
           0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
           0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
           0xF0, 0x90, 0xF0, 0x90, 0x90, # A
           0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
           0xF0, 0x80, 0x80, 0x80, 0xF0, # C
           0xE0, 0x90, 0x90, 0x90, 0xE0, # D
           0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
           0xF0, 0x80, 0xF0, 0x80, 0x80] # F

# copy over sprites into ROM space
for i, n in enumerate(SPRITES):
    ROM[i] = n

# assert the burn was successful
assert ROM[:80] == SPRITES

# test jumps
# ROM[0x200] = 0x1202 # JP
# ROM[0x202] = 0x1206 # JP
# ROM[0x204] = 0x1208 # JP
# ROM[0x206] = 0x1204 # JP

# test SE Vx, kk
# ROM[0x200] = 0x3000 # SE V0, 0x00
# ROM[0x201] = 0x3102 # SE V1, 0x02
# ROM[0x202] = 0x1208 # JP

# test SNE Vx, kk
# ROM[0x200] = 0x4000 # SNE V0, 0x00
# ROM[0x201] = 0x4102 # SNE V1, 0x02
# ROM[0x202] = 0x1208 # JP

# test LD Vx, kk
# ROM[0x200] = 0x61EE # LD V1, 0xFF
# ROM[0x201] = 0x60EE # LD V0, 0xEE
# ROM[0x202] = 0x5020 # SE V0, V2
# ROM[0x203] = 0x5010 # SE V0, V1
# ROM[0x204] = 0x1200 # JP 0x204

# add vx, kk
# ROM[0x200] = 0x630A # LD V3, 0x0A
# ROM[0x201] = 0x72FF # ADD V2, 0xFF
# ROM[0x202] = 0x7305 # ADD V3, 0x05

# DRW X, Y, N
ROM[0x200] = 0xA000 # point to address 0, sprite 0
ROM[0x201] = 0x6000 # ld v0 = 0
ROM[0x202] = 0x6100 # ld v1 = 0
ROM[0x203] = 0xD015 # draw a 5-byte sprite at (0, 0)
ROM[0x204] = 0xA014 # point to address 0xA, sprite A
ROM[0x205] = 0x6008 # ld v0 = 8
ROM[0x206] = 0x6105 # ld v1 = 5
ROM[0x207] = 0xD015 # draw a 5-byte sprite at (1, 1)