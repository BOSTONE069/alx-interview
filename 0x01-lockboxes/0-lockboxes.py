#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    n = len(boxes)
    myList = [0]
    for i in myList:
        for j in boxes[i]:
            if j not in myList:
                if j < n:
                    myList.append(j)
    if len(myList) == n:
        return True
    return False
