import csv

print("Add a router to this list:\n")
hostname = input("Enter the hostname: ")
ip_address = input("Enter the IP address: ")
manufacturer = input("Enter the manufacturer: ")

router = [hostname, ip_address, manufacturer]

with open("test.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(router)

with open("test.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        device = row[0]
        ip = row[1]
        manu = row[2]
        print(f'{device} has an ip address of {ip} and manufacturer {manu}')