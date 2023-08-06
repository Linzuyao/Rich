# Created by Linzuyao
# The module provides the class related to map

from colorama import Fore
import sys


class Map:
    def __init__(self) -> None:
        self.blocks = [Block(dloc=x, downer="A") for x in range(70)]

    def draw(self):
        for column in range(70):
            self.blocks[column].draw_block()
        print("\nCompleted Map Draw!")


class Block:
    def __init__(self, dloc, downer=None, dstat=None) -> None:
        # self.dtype = dtype
        # self.dvalue = dvalue
        self.downer = downer  # The block's owner
        self.dstat = dstat  # The block's status,jsut for item using
        self.dloc = dloc  # The block's location on the map,0~69
        self.level = 0
        # Map is static,so the type and value of the block is decided by its location
        if 0 <= self.dloc <= 13:
            self.dtype = str(self.level)
            self.dvalue = 100
        elif self.dloc == 14:
            self.dtype = "H"
        else:
            self.dtype = "$"

    def draw_block(self):
        # column is column number,y is row number
        if 0 <= self.dloc <= 27:
            column = self.dloc
            row = 0
        elif 28 <= self.dloc <= 35:
            column = 28
            row = self.dloc - 27
        elif 36 <= self.dloc <= 63:
            column = 61 - self.dloc
            row = 5
        else:
            column = 0
            row = 70 - self.dloc

        choose_role_color = {
            "Q": Fore.GREEN,
            None: Fore.WHITE,
            "A": Fore.RED,
            "J": Fore.BLUE,
        }
        print(choose_role_color[self.downer] + self.dtype + Fore.RESET)


if __name__ == "__main__":
    # test = Map()
    # test.draw()
    # print("        H", end="")
    # print("Q")
    # print()
    print()
