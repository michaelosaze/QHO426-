import csv

with open("data/data.csv", "a") as csvfile:
    csvfile.write("\n4,Skirt,Yellow")

with open("data/data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headings = next(csv_reader)
    for row in csv_reader:
        print(row) 