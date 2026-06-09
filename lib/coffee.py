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

    # Setter for size (Handles validation)
    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            self._size = None
        else:
            self._size = value