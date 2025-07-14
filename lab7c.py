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

def time_to_sec(time_obj):
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def sec_to_time(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)

def format_time(time_obj):
    return f"{time_obj.hour:02d}:{time_obj.minute:02d}:{time_obj.second:02d}"
