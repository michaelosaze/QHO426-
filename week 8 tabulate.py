from tabulate import tabulate

table_data= [ ["Audi", 51],["BMW", 47],["MINI",12] ]
col_headings = ["Make", "Sales"]
print("Sales volume Summary")
print(tabulate(table_data,headers=col_headings))
