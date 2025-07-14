#!/usr/bin/env python3
# Student ID: [162982235]

class Time:
    def __init__(self, hour, minute, second):
        if not (isinstance(hour, int) and isinstance(minute, int) and isinstance(second, int)):
            raise Exception("All arguments must be integers")
        if hour < 0 or minute < 0 or second < 0:
            raise Exception("Time values cannot be negative")
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        total_seconds = (self.hour * 3600 + self.minute * 60 + self.second +
                         other.hour * 3600 + other.minute * 60 + other.second)
        hour = total_seconds // 3600
        total_seconds %= 3600
        minute = total_seconds // 60
        second = total_seconds % 60
        return Time(hour, minute, second)

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
