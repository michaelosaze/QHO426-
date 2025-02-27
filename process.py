import csv

def read_csv_file():
    csvfile=open("data/car_prices.csv")
    csvreader=csv.reader(csvfile)
    headings=next(csvreader)
    carlist=list(csvreader)
    csvfile.close()
    return carlist