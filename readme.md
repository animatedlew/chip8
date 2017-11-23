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
- 1nnn - jp addr - set pc to nnn
- 2nnn - call addr - inc stack ptr then puts current PC on top of the stack, PC is set to nnn
- ...

# Chip-8 Font
```python
SPRITES = [[0xF0, 0x90, 0xF0, 0X90, 0XF0], # 8
           [0xF0, 0x90, 0xF0, 0x10, 0xF0], # 9
           [0xF0, 0x90, 0x90, 0x90, 0xF0], # 0
           [0x20, 0x60, 0x20, 0x20, 0x70], # 1
           [0xF0, 0x90, 0xF0, 0x90, 0x90], # A
           [0xE0, 0x90, 0xE0, 0x90, 0xE0], # B
           [0xF0, 0x10, 0xF0, 0x80, 0xF0], # 2
           [0xF0, 0x10, 0xF0, 0x10, 0xF0]] # 3
           ...
```

# Python Reqs
 - Python v3
 - pygame
 - virtualenv

# Sample Run
```bash
$ python3 src/chip8.py
0x200: OP: 0x1202
0x202: OP: 0x1206
0x206: OP: 0x1204
0x204: OP: 0x1208
0x208: OP: 0x0
0x209: OP: 0x0
0x20a: OP: 0x0
0x20b: OP: 0x0
0x20c: OP: 0x0
0x20d: OP: 0x0
 ```
 
 # Resources
 - http://devernay.free.fr/hacks/chip8/C8TECH10.HTM
 - https://en.wikipedia.org/wiki/CHIP-8
 - https://web.archive.org/web/20130903145938/http://chip8.com/?page=84
 - http://www.geocities.co.jp/Playtown-Yoyo/6130/chip8.htm
 - https://johnearnest.github.io/Octo/
