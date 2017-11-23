class CPU:
    """This class holds registers, timers, and the stack"""

    # 16 8-bit registers
    regs = {
        'V0': 0,
        'V1': 0,
        'V2': 0,
        'V3': 0,
        'V4': 0,
        'V5': 0,
        'V6': 0,
        'V7': 0,
        'V8': 0,
        'V9': 0,
        'VA': 0,
        'VB': 0,
        'VC': 0,
        'VD': 0,
        'VE': 0,
        'VF': 0, # freq used for storing carry values from subtraction or addition
                 # also specifies if a pixel is to be drawn

        'I':  0, # 16-bit index register
        'PC': 0, # 16-bit program counter
        'SP': 0  # stack pointer
    }

    # 8-bit stack pointer
    stack = [0] * 64 # 64-byte stack

    # 8-bit timers decrease by 1 per tick of a 60Hz clock
    timers = {
        'delay': 0,        
        'sound': 0
    }

    def __init__(self):
        # programs start at 0x200, identity: int(hex(512), 16)
        pass
