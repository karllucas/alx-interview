#!/usr/bin/python3
"""
Write a method that determines if a given
data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    i = 0
    while i < len(data):
        # Get the number of leading 1 bits in the first byte
        num_bytes = 0
        for j in range(7, -1, -1):
            if data[i] & (1 << j) != 0:
                num_bytes += 1
            else:
                break
        # If the number of leading 1 bits is 0, this is a single-byte character
        if num_bytes == 0:
            i += 1
        # If the number of leading 1 bits is 1, this is an invalid UTF-8 character
        elif num_bytes == 1:
            return False
        # Otherwise, this is a multi-byte character, so check the following bytes
        else:
            for j in range(1, num_bytes):
                if i + j >= len(data) or (data[i + j] & (1 << 7)) == 0 or (data[i + j] & (1 << 6)) != 0:
                    return False
            i += num_bytes
    return True
