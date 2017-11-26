# Chip-8 Spec
 - 64x32 1-bit frame buffer
 - all sprites are 8xN
 - 4k ROM layout
 - font - 0x000:0x080
 - code/data - 0x200:0xFFF
 - 64x32 1-bit frame buffer
 - 16 general purpose registers: V0-VF
 - 64-byte stack
 - one delay timer, one 1-bit sound timer
 - programs start at 0x200
 - big-endian instructions
 - first byte of each instructin needs to be on even address

# Op Codes - 36 different 16-bit instructions
- 0nnn sys addr jump - NOT IMPLEMENTED
- 00E0 - cls
- 00EE - ret: set pc to top of stack, then -1 from stack ptr
- 1nnn - jp addr: set pc to nnn
- 2nnn - call addr: inc stack ptr then puts current PC on top of the stack, PC is set to nnn
- 3xkk - SE Vx, byte: skip next instruction if vx == byte
- 4xkk - SNE Vx, byte: skip next instruction if vx != byte
- 5xy0 - SE Vx, Vy: skip next instruction if vx == vy
- 6xkk - LD Vx, byte: set vx = byte
- 7xkk - ADD Vx, byte: add byte to vx
- 8xy0 - LD Vx, Vy
- 8xy1 - OR Vx, Vy
- 8xy2 - AND Vx, Vy
- 8xy3 - XOR Vx, Vy
- 8xy4 - ADD Vx, Vy
- 8xy5 - SUB Vx, Vy
- 8xy6 - SHR Vx {, Vy}
- 8xy7 - SUBN Vx, Vy
- 8xyE - SHL Vx {, Vy}
- SNE Vx, Vy
- Annn - LD I, addr
- Bnnn - JP V0, addr
- Cxkk - RND Vx, kk
- Dxyn - DRW Vx, Vy, nibble
- ...

# Chip-8 Font
```python
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

```

# Python Reqs
 - Python v3
 - pygame
 - virtualenv

# Sample Run
```bash
$ python3 src/chip8.py

 addr:code
-----------
 0200:630A
 0201:72FF
 0202:7305
 0203:0000
 0204:0000
 0205:0000
 0206:0000
 0207:0000
 0208:0000
 0209:0000

 CPU Regs
----------
 V0: 0000
 V1: 0000
 V2: 00FF
 V3: 000F
 V4: 0000
 V5: 0000
 V6: 0000
 V7: 0000
 V8: 0000
 V9: 0000
 VA: 0000
 VB: 0000
 VC: 0000
 VD: 0000
 VE: 0000
 VF: 0000
  I: 0000
 PC: 020A
 SP: 0000
 DT: 0000
 ST: 0000
 ```
 
 # Resources
 - http://devernay.free.fr/hacks/chip8/C8TECH10.HTM
 - https://en.wikipedia.org/wiki/CHIP-8
 - https://web.archive.org/web/20130903145938/http://chip8.com/?page=84
 - http://www.geocities.co.jp/Playtown-Yoyo/6130/chip8.htm
 - https://johnearnest.github.io/Octo/
