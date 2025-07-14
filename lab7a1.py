#!/usr/bin/env python3
# Student ID: [162982235]
from lab7a import Time, sum_times, format_time

if __name__ == "__main__":
    time1 = Time(9, 50, 0)
    time2 = Time(1, 1, 1)
    timeSum = sum_times(time1, time2)
    print(format_time(timeSum))
