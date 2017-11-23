"""Chip-8 Interpreter"""
# pylint: disable=C0103

from rom import ROM
from cpu import CPU

class Chip8:
    """interpreter"""
    def __init__(self, cpu):
        "setup interpreter"
        self.cpu = cpu
        self.interpret()

    def fetch(self):
        "fetch/decode"
        return ROM[self.cpu.R['PC']]

    def interpret(self):
        """programs start at 0x200, identity: int(hex(512), 16)"""
        print("interpreting...")
        op = self.fetch()
        print("OP: {}".format(op))
        # execute
        while False:
            pass

chip8 = Chip8(CPU())
