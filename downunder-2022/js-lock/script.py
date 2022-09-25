#!/usr/bin/env python3

data = []
with open("array.txt", "r") as file:
    data = file.read()
    data = data.split(", ")


def path_to_pin(path):
    pin = ""
    for p in path:
        for _ in range(p):
            pin += str(1)
        pin += str(0)
    return pin

def get_int(d: str):
    v = ''
    for c in d:
        if c.isdigit():
            v += c
    return int(v)

def find(goal: int):
    path = []
    for d in data:
        o_b = d.count("[") # open bracket
        c_b = d.count("]") # close bracket

        value = get_int(d)

        if value == goal:
            path[-1] += 1
            for _ in range(o_b):
                path.append(0)
            # print(path)
            return path_to_pin(path)
        else:
            if "[" not in d and "]" not in d:
                path[-1] += 1
            else:
                try:
                    path[-1] += 1
                except:
                    pass
                for _ in range(o_b):
                    path.append(0)
                for _ in range(c_b):
                    path.pop()

if __name__ == "__main__":
    out = open("result.txt", "w")
    for i in range(1, 1338):
        out.write(find(i))
    out.close()