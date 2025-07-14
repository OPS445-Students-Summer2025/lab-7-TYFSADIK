#!/usr/bin/env python3
from lab7c import *

t1 = Time(9, 50, 0)
print(time_to_sec(t1))

seconds = 35400
t2 = sec_to_time(seconds)
print(format_time(t2))
