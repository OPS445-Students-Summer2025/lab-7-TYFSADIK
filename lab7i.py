#!/usr/bin/env python3
# Student ID: [162982235]

schoolName = "Seneca"

def function1():
    global schoolName
    schoolName = "SICT"
    print("print() in function1 on schoolName:", schoolName)

def function2():
    global schoolName
    schoolName = "SSDO"
    print("print() in function2 on schoolName:", schoolName)

print("print() in main on schoolName:", schoolName)
function1()
print("print() in main on schoolName:", schoolName)
function2()
print("print() in main on schoolName:", schoolName)
