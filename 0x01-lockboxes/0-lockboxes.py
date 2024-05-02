#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.
    """

    # If there are no boxes, returns True
    if len(boxes) == 0:
        return True

    # Initializes sets to keep track of keys
    keys = set()
    new_keys = set(boxes[0])

    # Loops until there are no more new keys to explore
    while len(new_keys):
        # Adds new keys to the key set
        keys = keys | new_keys
        new_keys = set()

        # Checks if all boxes can be opened
        if keys & set(range(1, len(boxes))) == set(range(1, len(boxes))):
            return True

        # Uses current keys to find new keys
        for x in keys:
            # Checks if the key corresponds to a valid box index
            if x < len(boxes):
                # Adds keys found in the current box to new_keys
                for y in boxes[x]:
                    if y not in keys:
                        new_keys.add(y)

    # If the loop completes without finding a solution, returns False
    return False
