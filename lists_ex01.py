#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys

start = -5
stop = 5
step = 0.1
xval = np.arange(start,stop,step)

argnumber = str(sys.argv[1])

if argnumber =="1":
    yval = xval

elif argnumber == "2":
    yval = np.sin(xval)

elif argnumber =="3":
    yval = np.cos(xval)

elif argnumber =="4":
    yval = np.tan(xval)


# get plot
plt.plot(xval,yval, alpha=0.5, color='red', linewidth=2)
plt.grid(True)
plt.xlabel('xval')
plt.ylabel('yval')
plt.tight_layout()
plt.show()
