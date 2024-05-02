#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened."""
    if not boxes:
        return False

    # Initializes a set to keep track of opened boxes
    opened_boxes = {0}

    # Initializes a list to keep track of keys
    keys = boxes[0]

    # Loops through the keys and boxes
    while keys:
        # Gets the next key
        key = keys.pop(0)

        # Checks if the key can open a new box
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    # Checks if all boxes are opened
    return len(opened_boxes) == len(boxes)

