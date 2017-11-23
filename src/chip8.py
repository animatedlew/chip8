"""Chip-8 Interpreter"""
# pylint: disable=C0103

from rom import ROM
from cpu import CPU
import vram

class Chip8:
    """interpreter"""
    def __init__(self, cpu):
        "setup"
        self.cpu = cpu
        self.execute()

    def fetch(self):
        "fetch/decode"
        return ROM[self.cpu.R['PC']]

    def execute(self):
        """programs start at 0x200, identity: int(hex(512), 16)"""
        # FIXME: 0xA instructions
        for _ in range(10):

            op = self.fetch()

            print("{}: OP: {}".format(hex(self.cpu.R['PC']), hex(op)))

            group = (op & 0xF000) >> 12
            address = op & 0x0FFF

            if group == 0:
                if op == 0x00E0: # CLS
                    vram.clear()
                elif op == 0x00EE: # RET
                    self.cpu.popPC()
            elif group == 1: # JP
                self.cpu.R['PC'] = address
                continue
            elif group == 2: # CALL nnn
                self.cpu.pushPC()
                self.cpu.R['PC'] = address
                continue
            else:
                return op

            self.cpu.R['PC'] += 1

chip8 = Chip8(CPU())



