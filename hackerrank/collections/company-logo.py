#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    count = Counter(sorted(s))
    logo = count.most_common(3)
    for l in logo:
        print(*l)