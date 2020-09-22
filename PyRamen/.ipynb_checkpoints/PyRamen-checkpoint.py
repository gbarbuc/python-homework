# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path("C:/Users/George/python-projects/PyRamen/Resources/menu_data.csv")
sales_filepath = Path("C:/Users/George/python-projects/PyRamen/Resources/sales_data.csv")
report_filepath = Path("C:/Users/George/python-projects/PyRamen/Resources/report.txt")


# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, newline='') as fm:

    menu = list(csv.reader(fm))

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, newline='') as fs:

    sales = list(csv.reader(fs))
    

    
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

"""
GBa - Scan throu the menu and sales. If item was sold in the past add it to the report. 
     If the item is already in the report update metrics
"""

for menu_item in menu:
    first=True
    for sales_item in sales:
        if sales_item[4]==menu_item[0]:
            if first:
                report.update({menu_item[0]:{"01-count":int(sales_item[3]),
                                            "02-revenue":int(sales_item[3])*(int(menu_item[3])),
                                             "03-cogs":int(sales_item[3])*int(menu_item[4]),
                                             "04-profit":int(sales_item[3])*(int(menu_item[3])-int(menu_item[4]))
                                            }})
                first=False
            else:
                report[menu_item[0]]["01-count"] += int(sales_item[3])
                report[menu_item[0]]["02-revenue"] += int(sales_item[3]) * (int(menu_item[3]))
                report[menu_item[0]]["03-cogs"] += int(sales_item[3]) * int(menu_item[4])
                report[menu_item[0]]["04-profit"] += int(sales_item[3]) * (int(menu_item[3]) - int(menu_item[4]))


for key,val in report.items():
    print(key,val,'\n')
    
print (len(sales))

f = open(report_filepath,"w")
f.write(str(report))
f.close()

