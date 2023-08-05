# Created by Linzuyao
# The module provides the class related to map


class Map:
    pass


class Block:
    def __init__(self, dtype=None, dvalue=0, downer=None, dstat=None) -> None:
        self.dtype = dtype
        self.dvalue = dvalue
        self.downer = downer
        self.dstat = dstat
