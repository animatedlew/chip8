"""Chip-8 Interpreter"""
# pylint: disable=C0103

from cpu import CPU
from rom import ROM
import video

cpu = CPU()

class Chip8:
    """interpreter"""
    def __init__(self):
        "setup"
        self.execute()

    def fetch(self):
        "fetch"
        return ROM[cpu.R['PC']]

    def execute(self):
        """programs start at 0x200, identity: int(hex(512), 16)"""
        print('\n addr:code\n-----------')
        # FIXME: 0xA instructions
        for _ in range(10):

            op = self.fetch()

            print(' %04X:%04X' % (cpu.R['PC'], op))

            # decode
            group = (op & 0xF000) >> 12
            address = op & 0x0FFF
            lsb = (op & 0xFF)
            msb = (op & 0xFF00) >> 8
            vx = 'V%X' % ((op & 0x0F00) >> 8)
            vy = 'V%X' % ((op & 0x00F0) >> 4)

            # execute
            if group == 0:
                if op == 0x00E0: # CLS
                    video.clear()
                elif op == 0x00EE: # RET
                    cpu.popPC()
            elif group == 1: # JP
                cpu.R['PC'] = address
                continue
            elif group == 2: # CALL nnn
                cpu.pushPC()
                cpu.R['PC'] = address
                continue
            elif group == 3: # SE Vx, kk
                # decode 3xkk, skip next instruction if Vx = kk.
                if cpu.R[vx] == lsb:
                    cpu.R['PC'] += 2
                    continue
            elif group == 4: # SNE Vx, kk
                # decode 4xkk, skip next instruction if Vx != kk.
                if cpu.R[vx] != lsb:
                    cpu.R['PC'] += 2
                    continue
            elif group == 5: # SE Vx, Vy
                # decode 5xy0, skip next instruction if Vx = Vy.
                if cpu.R[vx] == cpu.R[vy]:
                    cpu.R['PC'] += 2
                    continue
            elif group == 6: # LD Vx, kk
                # decode 6xkk, set Vx = kk.
                cpu.R[vx] = lsb
            elif group == 7: # ADD Vx, kk
                # decode 7xkk - set Vx = Vx + kk.
                cpu.R[vx] += lsb
            else:
                return op

            cpu.R['PC'] += 1

# manual print testing FTW
chip8 = Chip8()
print(cpu)
