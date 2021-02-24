#!/bin/bash python

'''
EXPLANATION: We don't need to save all the matrix, becouse the only thing we do with matrix
is sum of diagonal values. It is simple to do when reading matrix rows line per line.
'''

size = int(input())
main_diagonal, sub_diagonal = 0, 0

for i in range(size):
    row = [ int(val) for val in input().split()]
    main_diagonal += row[i]
    sub_diagonal += row[size-i-1]

print(abs(main_diagonal - sub_diagonal))
