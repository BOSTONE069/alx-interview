#!/usr/bin/env python3

def pascal_triangle(n):
    """
    We start with a list containing a single list of 1, and then for each row we add a 1 to the beginning and end of the
    previous row, and then for each element in the middle of the row we add the two elements above it

    :param n: the number of rows in the triangle
    :return: A list of lists.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
