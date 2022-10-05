#!/usr/bin/env python3

class Line:
    def __init__(self, color, data):
        self.color = color
        self.data = data


objs = []
max_length = 0
with open("SEKAI.sus", "r") as file:
    lines = file.readlines()
    for l in lines:
        data = l.split(":")
        objs.append(Line(data[0], data[1]))
        if len(data[1]) > max_length:
            max_length = len(data[1])

print(objs)
print(max_length)
