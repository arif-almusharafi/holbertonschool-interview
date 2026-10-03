#!/usr/bin/python3
"""Lockboxes problem"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else False"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = {0}      # الصندوق 0 مفتوح من البداية
    to_check = [0]    # الصناديق التي لم نفحص مفاتيحها بعد

    while to_check:
        box = to_check.pop()
        for key in boxes[box]:
            if 0 <= key < n and key not in opened:
                opened.add(key)
                to_check.append(key)

    return len(opened) == n
