#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if 2 <= n and n <= 6:
            print('Not Weird')
        elif 6 <= n and n <= 21:
            print('Weird')
        elif n > 20:
            print('Not Weird')
    else:
        print('Weird')
