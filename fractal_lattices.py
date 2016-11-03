# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 17:43:04 2016

@author: cdperlada
"""

import numpy as np
import matplotlib.pyplot as plt

def mid(p1, p2):
    return (p1 + p2) /2.0

points = 10000


p = np.array(([np.random.randint(0,50),np.random.randint(0,50)],[np.random.randint(0,50),np.random.randint(0,50)] , [np.random.randint(0,50),np.random.randint(0,50)]))
q = np.array([0,0])
xlist = []
ylist = []
for n in range(points):
    r = np.random.randint(0,3)
    q = (q + p[r])/2.
    xlist.append(q[0])
    ylist.append(q[1])
plt.plot(xlist, ylist,'k.')
#plt.axis('off')
plt.show()


    
p = np.array(([0,0], [1,0],[0.5,0.5]))

def tri(p, count = 0, iterate = 5):
    if count < iterate:
        count += 1
        for i in xrange(len(p)):
            corner = [p[i]]
            for j in xrange(len(p)):
                x1 = mid(p[i], p[j])
                corner.append(x1)
                z = zip(p[i], x1)
                plt.plot(z[0], z[1])
            tri(corner, count)

tri(p)

        

    