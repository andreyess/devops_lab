#!/bin/bash python

input_string = input()

if input_string == ''.join(reversed(input_string)):
    print('yes')
else:
    print('no')
