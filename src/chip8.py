"""Chip-8 Interpreter"""
# pylint: disable=C0103

from cpu import CPU
from rom import ROM
import video
import random

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
            if group == 0x00:
                if op == 0x00E0: # CLS
                    video.clear()
                elif op == 0x00EE: # RET
                    cpu.popPC()

            elif group == 0x01: # JP
                cpu.R['PC'] = address
                continue

            elif group == 0x02: # CALL nnn
                cpu.pushPC()
                cpu.R['PC'] = address
                continue

            elif group == 0x03: # SE Vx, kk
                # decode 3xkk, skip next instruction if Vx = kk.
                if cpu.R[vx] == lsb:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0x04: # SNE Vx, kk
                # decode 4xkk, skip next instruction if Vx != kk.
                if cpu.R[vx] != lsb:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0x05: # SE Vx, Vy
                # decode 5xy0, skip next instruction if Vx = Vy.
                if cpu.R[vx] == cpu.R[vy]:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0x06: # LD Vx, kk
                # decode 6xkk, set Vx = kk.
                cpu.R[vx] = lsb

            elif group == 0x07: # ADD Vx, kk
                # decode 7xkk - set Vx = Vx + kk.
                cpu.R[vx] += lsb

            elif group == 0x08:
                kind = op & 0x000F

                if (kind == 0):     # 8xy0 - LD Vx, Vy
                    cpu.R[vx] = cpu.R[vy]
                elif (kind == 1):   # 8xy1 - OR Vx, Vy
                    cpu.R[vx] |= cpu.R[vy]
                elif (kind == 2):   # 8xy2 - AND Vx, Vy
                    cpu.R[vx] &= cpu.R[vy]
                elif (kind == 3):   # 8xy3 - XOR Vx, Vy
                    cpu.R[vx] ^= cpu.R[vy]
                elif (kind == 4):   # 8xy4 - ADD Vx, Vy
                    cpu.R[vx] += cpu.R[vy]
                    cpu.R['VF'] = 1 if cpu.R[vx] > 0xFF else 0
                    cpu.R[vx] %= 0xFF
                elif (kind == 5):   # 8xy5 - SUB Vx, Vy
                    cpu.R['VF'] = 1 if cpu.R[vx] > cpu.R[vy] else 0
                    cpu.R[vx] -= cpu.R[vy]
                elif (kind == 6):   # 8xy6 - SHR Vx {, Vy}
                    cpu.R['VF'] = 1 if cpu.R[vx] & 0x01 == 1 else 0
                    cpu.R[vx] >>= 1
                elif (kind == 7):   # 8xy7 - SUBN Vx, Vy
                    cpu.R['VF'] = 1 if cpu.R[vy] > cpu.R[vx] else 0
                    cpu.R[vx] = cpu.R[vy] - cpu.R[vx]
                elif (kind == 0xE): # 8xyE - SHL Vx {, Vy}
                    cpu.R['VF'] = 1 if cpu.R[vx] & 0x80 == 1 else 0
                    cpu.R[vx] *= 2

            elif group == 0x09: # 9xy0 - SNE Vx, Vy
                # decode 9xy0, skip next instruction if Vx != Vy.
                if cpu.R[vx] != cpu.R[vy]:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0x0A: # Annn - LD I, addr
                cpu.R['I'] = address

            elif group == 0x0B: # Bnnn - JP V0, addr
                cpu.R['PC'] = cpu.R['V0'] + address
                continue

            elif group == 0x0C: # Cxkk - RND Vx, kk
                cpu.R[vx] = random.randint(0, 255) & lsb

            elif group == 0x0D: # Dxyn - DRW Vx, Vy, nibble
                nibble = op & 0x000F
                '''
                Display n-byte sprite starting at memory
                location I at (Vx, Vy), set VF = collision.

                The interpreter reads n bytes from memory,
                starting at the address stored in I. These
                bytes are then displayed as sprites on screen
                at coordinates (Vx, Vy). Sprites are XORed onto
                the existing screen. If this causes any pixels
                to be erased, VF is set to 1, otherwise it is
                set to 0. If the sprite is positioned so part
                of it is outside the coordinates of the display,
                it wraps around to the opposite side of the screen.
                '''
            else:
                return op

            cpu.R['PC'] += 1

# manual print testing FTW
chip8 = Chip8()
print(cpu)
