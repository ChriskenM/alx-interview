#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for num in data:
        # Get the least significant 8 bits of the number
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) == 0:
                num_bytes = 0
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
