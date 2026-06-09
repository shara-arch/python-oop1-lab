#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        # Initializing via the setter property ensures validation occurs immediately
        self.page_count = page_count
