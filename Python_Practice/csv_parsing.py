import csv

file_open = open("test.csv")

file_reader = csv.reader(file_open)

for row in file_reader:
    print(row)

import csv

with open("test.csv") as csv_file:  #using with safely opens and closes test.csv so there are no memory leaks
    reader = csv.reader(csv_file) #parses rows into lists
    for row in reader:
        device = row[0]
        ip = row[1]
        manufacturer = row[2]
        print(f'{device} has an ip address of {ip} and manufacturer {manufacturer}')
