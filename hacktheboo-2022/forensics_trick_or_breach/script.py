#!/usr/bin/env python3

import csv

outfile = open("out.zip", "wb")

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    headers = next(reader)
    for row in reader:
        hstr = row[6].split(".")[0]
        o = bytes(bytearray.fromhex(hstr))
        print(o)
        outfile.write(o)

        next(reader)

outfile.close()