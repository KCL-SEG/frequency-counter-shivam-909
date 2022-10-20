"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    l = lambda x: str(x)
    items = list(map(l, items))

    for x in range(0, len(items)):
        frequencies[str(items[x])] = items.count(items[x])
    return frequencies
