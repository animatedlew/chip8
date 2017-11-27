"""Chip-8 Interpreter"""
# pylint: disable=C0103

from cpu import CPU
from rom import ROM
import video
import pygame, sys, random
from pygame.locals import *
import sys

cpu = CPU()

class Chip8:
    """interpreter"""
    def __init__(self):
        "setup"
        self.init_video()
        self.execute()

    def fetch(self):
        "fetch"
        return ROM[cpu.R['PC']]

    def execute(self):
        """programs start at 0x200, identity: int(hex(512), 16)"""
        print('\n addr:code\n-----------')
        # while True:
        for _ in range(10): # testing

            self.quit()

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
            if group == 0x0:
                if op == 0x00E0: # CLS
                    video.clear()
                elif op == 0x00EE: # RET
                    cpu.popPC()

            elif group == 0x1: # JP
                cpu.R['PC'] = address
                continue

            elif group == 0x2: # CALL nnn
                cpu.pushPC()
                cpu.R['PC'] = address
                continue

            elif group == 0x3: # SE Vx, kk
                # decode 3xkk, skip next instruction if Vx = kk.
                if cpu.R[vx] == lsb:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0x04: # SNE Vx, kk
                # decode 4xkk, skip next instruction if Vx != kk.
                if cpu.R[vx] != lsb:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0x5: # SE Vx, Vy
                # decode 5xy0, skip next instruction if Vx = Vy.
                if cpu.R[vx] == cpu.R[vy]:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0x6: # LD Vx, kk
                # decode 6xkk, set Vx = kk.
                cpu.R[vx] = lsb

            elif group == 0x7: # ADD Vx, kk
                # decode 7xkk - set Vx = Vx + kk.
                cpu.R[vx] += lsb

            elif group == 0x8:
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

            elif group == 0x9: # 9xy0 - SNE Vx, Vy
                # decode 9xy0, skip next instruction if Vx != Vy.
                if cpu.R[vx] != cpu.R[vy]:
                    cpu.R['PC'] += 2
                    continue

            elif group == 0xA: # Annn - LD I, addr
                cpu.R['I'] = address

            elif group == 0xB: # Bnnn - JP V0, addr
                cpu.R['PC'] = cpu.R['V0'] + address
                continue

            elif group == 0xC: # Cxkk - RND Vx, kk
                cpu.R[vx] = random.randint(0, 255) & lsb

            elif group == 0xD: # Dxyn - DRW Vx, Vy, n
                n = op & 0x000F
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
                sprite = [ROM[cpu.R['I'] + n] for n in range(n)]
                x = cpu.R[vx]
                y = cpu.R[vy]
                for i in range(n):
                    # TODO: this currently banks the sprite to byte aligned columns.
                    # update this to allow drawing across column borders
                    video.FRAMEBUFFER[(y + i) * 0x10 + (x // 8)] = sprite[i]
                print(list(map(hex, sprite)))
            else:
                return op

            cpu.R['PC'] += 1

            self.draw_buffer()
            pygame.display.update()
            video.clock.tick(video.Hz)
            print(cpu)

        input()
        self.terminate()

    def init_video(self):

        pygame.init()
        self.screen = pygame.display.set_mode((128, 64))
        pygame.display.set_caption('Chip-8')

        self.pos = 64
        self.prev = self.pos
        self.dir = 1

    def draw_buffer(self):
        # 128x64
        pixels = pygame.PixelArray(self.screen)
        o = ''
        for row in range(64): # rows of 16-bytes
            for pos in range(0x10): # bytes
                cell = video.FRAMEBUFFER[(row * 0x10) + pos]
                o += '%0.2X ' % cell
                for col in range(8): # 8-bits
                    isSet = cell & (0x80 >> col)
                    if isSet:
                        # TODO: add VF flag collision logic @ sprite level
                        current_pixel = pixels[(pos * 8) + col][row]
                        pixel = ((0xFF if isSet else 0x00) ^ current_pixel) & 0xFF
                        pixels[(pos * 8) + col][row] = (pixel, pixel, pixel)
            o += '\n'
        print('-----------------------------------------------')
        print('|               Frame Buffer                  |')
        print('-----------------------------------------------\n%s' % o)

    def quit(self):
        for event in pygame.event.get(QUIT):
            self.terminate()

    def terminate(self):
        pygame.quit()
        sys.exit()

chip8 = Chip8()

