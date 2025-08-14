#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple test script
"""

def hello_world():
    """Return a simple greeting."""
    return "Hello, World!"

def add_numbers(a, b):
    """Add two numbers together."""
    return a + b

if __name__ == "__main__":
    print(hello_world())
    print(f"5 + 3 = {add_numbers(5, 3)}")