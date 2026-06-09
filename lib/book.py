#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        # Initializing via the setter property ensures validation occurs immediately
        self.page_count = page_count
        
    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count
    
    # Setter for page_count (Handles validation)
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            # Set to None or a safe default if required, or keep it unmodified
            self._page_count = None 
        else:
            self._page_count = value