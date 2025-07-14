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

def change_time(time_obj, seconds):
    total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second + seconds
    if total_seconds < 0:
        total_seconds = 0
    hour = total_seconds // 3600
    total_seconds %= 3600
    minute = total_seconds // 60
    second = total_seconds % 60
    time_obj.hour = hour
    time_obj.minute = minute
    time_obj.second = second
    return time_obj

def format_time(time_obj):
    return f"{time_obj.hour:02d}:{time_obj.minute:02d}:{time_obj.second:02d}"
