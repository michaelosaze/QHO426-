from process import read_csv_file
from tui import *

carlist = read_csv_file()

allmakes=()
for car in carlist:
    if car[1].upper() not in allmakes:
        allmakes.append(car[1].upper())
print(allmakes)

make = get_selected_make(allmakes)

for car in carlist:
    if make.upper() == car[1].upper():
        print(car)