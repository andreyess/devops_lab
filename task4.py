#!/bin/bash python


def find_q(N):
    # Values 1 and 0 can't be processed by next loop, and we need to process
    # those critical situation before it
    if N == 1:
        return 1
    elif N == 0:
        return -1

    multiply_list = []
    for i in range(9, 1, -1):
        while N % i == 0:
            N /= i
            multiply_list.append(i)

    if N != 1:
        # It means we can't get expected value multiplying numbers from 1 to
        return -1
    else:
        # Sort the list of values we got to get the minimal value from it
        multiply_list.sort()
        return int(''.join([str(i) for i in multiply_list]))


N = int(input())
print(find_q(N))
