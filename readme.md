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

# Op Codes
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