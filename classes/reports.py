import csv
from decimal import Decimal
from pathlib import Path
import shutil
import tempfile
from classes.product import BOUGHT_PATH, COLS
from classes.purchase import SOLD_FILE
import pandas as pd

report_inventory_date = Path.cwd()/"reports/report_inventory_date.csv"
report_expired_products = Path.cwd()/"reports/report_expired_product.csv"
report_inventory_path = Path.cwd()/"reports/report_inventory.csv"

class Reports():


    global revenue
    """report bought""" 

    def report_inventory(self):             
            with open(BOUGHT_PATH ,"r") as csvfile:
                temp_inventory_file = tempfile.NamedTemporaryFile(mode="w", delete=False, newline='')
                data = list(csvfile)
                tempwriter = csv.DictWriter(temp_inventory_file,fieldnames= COLS,lineterminator="\n")
                tempwriter.writeheader()
                for row in data[1:]:
                    tempwriter.writerow({
                        "id": row.split(',')[0].strip(),
                        "product": row.split(',')[1].strip(),
                        "sell_date": row.split(',')[2].strip(),
                        "buy_price": row.split(',')[3].strip(),
                        "amount": row.split(',')[4].strip(),
                        "expiration_date": row.split(',')[5].strip(),
                        "state": row.split(',')[6].strip()})
                temp_inventory_file.close()
                shutil.move(temp_inventory_file.name, report_inventory_path)
                print("INFO: report_inventory.csv saved in reports\n")
            with open(report_inventory_path) as file:
                    reader = csv.DictReader(file)
                    df = pd.read_csv(report_inventory_path)
                    for row in reader:                       
                        pd.options.display.max_columns = len(df.columns)                       
                    if len(df)>0:
                        df.to_csv('file_name.csv', encoding='utf-8')
                        print(df)
                    if df.empty:
                        return print('no results, please alter search and try again...')
                  
   
    def report_date_inventory(self, arg_date):
        print(arg_date)
        with open(BOUGHT_PATH, "r") as csvfile:
            data = list(csvfile)
            date_list = []
        for line in data[1:]:          
            if arg_date == line.split(',')[2].strip():
                date_list.append(line)          
        with open(report_inventory_date, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=COLS, lineterminator='\n')
            writer.writeheader()
            for row in date_list:
                    writer.writerow({
                        "id": row.split(',')[0],
                        "product": row.split(',')[1],
                        "sell_date": row.split(',')[2],
                        "buy_price": row.split(',')[3],
                            "amount": row.split(',')[4],
                            "expiration_date": row.split(',')[5],
                        "state": row.split(',')[6].strip()})
        with open(report_inventory_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                df = pd.read_csv(report_inventory_date)
                pd.options.display.max_columns = len(df.columns)
            if df.empty:
                print('no results, please alter search and try again...')
            else:
                print(df)


    def report_expired(self,what2do, date)
        with open(report_inventory_path) as file:
            reader = csv.DictReader(file)
            df = pd.read_csv(report_expired_products)
            for _ in reader:
                pd.options.display.max_columns = len(df.columns)
            if df.empty:
                print('no products')
            else:
                print(df)

    
    def purchased_products(self):
        with open(BOUGHT_PATH, "r", newline="") as file:
            data = list(file)
            i = 0
            for row in data[1:]:
                row_revenue = row.split(",")[3]
                row_revenue = row_revenue.strip('\n\r')
                getal = Decimal(row_revenue)
                revenue = i + getal
                i = revenue
            print(f'total purchased price: €.{revenue}')
        return revenue   

    
    def purchased_products_by_date(self, date, sender="none"):
        with open(BOUGHT_PATH, "r") as csvfile:
            data = list(csvfile)
            i = 0
            revenue = 0
            for row in data[1:]:
                formatted_date = date.strftime('%Y-%m-%d')
                table_date = row.split(',')[2]
                table_date = table_date.strip('\n\r')
                if formatted_date == table_date:
                    row_revenue = row.split(",")[3]
                    row_revenue = row_revenue.strip('\n\r')
                    revenue = i + Decimal(row_revenue)
                    i = revenue         
            if revenue == 0 and sender == 'by-range':
                return 0
            if revenue > 0 and sender == 'by-range':
                return revenue
            if revenue == 0 and sender != 'by-range':
                return 0
            if revenue > 0:
                return revenue                   


    def revenue_all(self):
            revenue=0
            i=0
            with open( SOLD_FILE, "r", newline="") as file:
                data = list(file)
                for row in data[1:]:
                    row_revenue =row.split(",")[3]
                    row_revenue = row_revenue.strip('\n\r')
                    getal = Decimal(row_revenue)
                    revenue = i + getal
                    i = revenue
            print(f'total sold products is: €.{revenue}')
            return revenue 


    def revenue_number_of_days( self, argdate, sender="none"):     
        with open(SOLD_FILE, "r") as csvfile:
            i = 0
            revenue = 0
            data = list(csvfile)           
            for row in data[1:]:
                row_date = row.split(',')[2]
                arg_date = str(argdate).split(' ')
                row_revenue = row.split(",")[3]
                row_revenue = row_revenue.strip('\n\r')
                getal = Decimal(row_revenue)            
                if sender == "none":
                    if  arg_date[0] == row_date:                       
                        revenue = i + getal
                        i = revenue
                  
                if sender == "by-range" and arg_date[0] == row_date:
                    row_revenue = row.split(",")[3].strip('\n\r')
                    getal = Decimal(row_revenue)
                    revenue = i + getal
                    i = revenue
            if sender=="none":
                return revenue
            else:
                return revenue
   
    def calc_profit_by_range( self, start_date, end_date, 
    sender="none"):
        i = 0
        j = 0
        revenue = 0
        purchaced = 0
        revenue = 0
        for day in pd.date_range(start=start_date, end=end_date):
            count = Reports.revenue_number_of_days("self",day,'by-range')
            if not count is None:
                revenue = i + count
                i = revenue              
        for day in pd.date_range(start=start_date, end=end_date):
            count_inkoop = Reports.purchased_products_by_date("self",day,'by-range')
            if  not count_inkoop is None:
                purchaced = j + count_inkoop
                j = purchaced
        profit_timerange = revenue - purchaced 
        print(f" Bought {start_date} till {end_date}: € {purchaced}")
        print(f" Sold {start_date} till {end_date}: € {revenue}")
        print(f" Total Profit for {start_date} till {end_date}: € {profit_timerange}")
