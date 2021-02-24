#!/bin/bash python


def reverse_string(input_string):
    return ' '.join([''.join(reversed(word)) for word in input_string.split()])


print(reverse_string(input()))
