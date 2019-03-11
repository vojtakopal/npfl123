#!/usr/bin/env python
import sys
import csv

(_, *csv_files) = sys.argv

counter = 0
for path in csv_files:
    with open(path, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            line = row[9]
            print(line)
            words = line.split(' ')
            counter += len(words)
            if counter > 10000:
                sys.exit()
