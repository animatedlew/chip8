"""CPU"""
# pylint: disable=C0103

class CPU:
    """This class holds registers, timers, and the stack"""

    # 16 8-bit registers
    R = {
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
        'PC': 0x200, # 16-bit program counter
        'SP': 0, # stack pointer

        # 8-bit timers decrease by 1 per tick of a 60Hz clock
        'DT': 0, # delay
        'ST': 0  # sound inactive when 0
    }

    # 8-bit stack pointer
    stack = [0] * 64 # 64-byte stack

    def popPC(self):
        "pops off values off stack"
        self.R['PC'] = self.stack[self.R['SP']]
        self.R['SP'] -= 1

    def pushPC(self):
        "pushes values onto the stack"
        self.R['SP'] += 1
        self.stack[self.R['SP']] = self.R['PC']
