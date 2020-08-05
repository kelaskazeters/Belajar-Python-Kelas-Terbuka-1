#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:39:56 2019

@author: rafliano
"""

from collections import deque

queues = deque([1,2,3,4,5])

print('data sekarang: ',queues)

# menambahkan data
queues.append(6)
print('data masuk: ',6)
print('data sekarang',queues)

queues.append(7)
print('data masuk: ',7)
print('data sekarang',queues)

# mengurangi antrian
out = queues.popleft()
print('data keluar: ',out)
print('data sekarang: ',queues)

out = queues.popleft()
print('data keluar: ',out)
print('data sekarang: ',queues)

out = queues.popleft()
print('data keluar: ',out)
print('data sekarang: ',queues)

queues.append(8)
print('data masuk: ',8)
print('data sekarang',queues)

