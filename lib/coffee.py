#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Initializing via the setter property ensures validation occurs immediately
        self.size = size
        self.price = price

    # Getter for size
    @property
    def size(self):
        return self._size

