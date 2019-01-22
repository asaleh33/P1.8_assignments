#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys

start = -3
stop = 3
step = 0.1
xval = np.arange(start,stop,step)

argnumber = str(sys.argv[1])

if argnumber =="1":
    yval = xval

