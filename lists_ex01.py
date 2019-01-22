#!/usr/bin/env python

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys


if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "1 2 3 4 5 6 7 8\n1 y=f(x)\n2 y=f(x)**2\n3 "
    "y=f(x)**3\n4 y=exp(x)\n5 y=sqrt(|x|)\n6 y=sin(x)\n7 y=cos(x)\n8 y=tan(x)")
    sys.exit(0)


start = -3
stop = 3
step = 0.1
xval = np.arange(start,stop,step)

argnumber = str(sys.argv[1])

if argnumber =="1":
    yval = xval

elif argnumber =="2":
    yval = [i ** 2 for i in xval]

elif argnumber =="3":
    yval = [i ** 3 for i in xval]

elif argnumber == "4":
    yval = np.exp(xval)

elif argnumber == "5":
    yval = np.sqrt(abs(xval))

elif argnumber == "6":
    yval = np.sin(xval)

elif argnumber =="7":
    yval = np.cos(xval)

elif argnumber =="8":
    yval = np.tan(xval)

else:
    print("Wrong argument!")
    sys.exit(1)


# get plot
plt.plot(xval,yval, alpha=0.5, color='red', linewidth=2)
plt.grid(True)
plt.xlabel('xval')
plt.ylabel('yval')
plt.tight_layout()
plt.show()
