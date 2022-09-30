
from csv import DictReader, DictWriter
import csv
from decimal import Decimal
import pathlib
from pickle import LIST
import shutil
import tempfile
from pathlib import Path
import pandas as pd
from datetime import date, datetime, timedelta
import controllers.date_setter as date_setter


report_inventory_path = Path.cwd()/"reports/report_inventory.csv"
report_inventory_date = Path.cwd()/"reports/report_inventory_date.csv"
report_expired_products = Path.cwd()/"reports/report_expired_product.csv"
BOUGHT_PATH = Path.cwd()/"data/bought.csv"
COLS = ["id","product","sell_date","buy_price","amount","expiration_date","state"]
NUM_OF_DAYS = 0
class Product():
    def __init__(self, file_path, productName, 
                    buyPrice, amount,expires,state):
        self.id = Product.get_file_lenght("self",file_path)
        self.productName = productName
        self.buyDate = date_setter.get_internal_date("self",int(date_setter.read_nums_of_days()))
        self.buyPrice = buyPrice
        self.amount = amount
        self.expiration_date = expires
        self.state = state
    
      
    
    def add_product(self,product_name, purchase_price,amount,expires):
       
        new_product = Product(BOUGHT_PATH, product_name, Decimal(purchase_price) ,int(amount),expires, "true")
        with open(BOUGHT_PATH, "a") as new_file:
            prod_dict = {
                "id": new_product.id -1,
                "product": new_product.productName.lower(),
                "sell_date": new_product.buyDate.strftime('%Y-%m-%d'),
                "buy_price": new_product.buyPrice,
                "amount": new_product.amount,
                "expiration_date": new_product.expiration_date,
                "state":new_product.state}            
            csv_writer = DictWriter(new_file,fieldnames=COLS, delimiter="," ,lineterminator="\n")
            csv_writer.writerow(prod_dict)
        Product.display("self",BOUGHT_PATH)
    
                

    def  is_check_product_in_stock( self,product,expires):
        with open(BOUGHT_PATH ,"r") as file:
            data = list(file)
        for line in data[1:]:
            if product == line.split(',')[1].strip() and expires == line.split(',')[5].strip():
                return True
        else:
            return False
      

    def  product_expires_in_stock(id):
         with open(BOUGHT_PATH ,"r") as file:
            # Product.find_values_in_inventory(product,expires )
            date  =datetime.today()
            formatted_date = Product.date_to_integer(date)
            data = list(file)
            cast_date = 0
            for line in data[1:]:
                cast_date = line.split(',')[5]
                cast_date2 = datetime.strptime(cast_date.strip(),"%Y-%m-%d")
                cast_date3 = Product.date_to_integer(cast_date2)
                if id == line.split(',')[0].strip() and formatted_date >= cast_date3:
                    return True
            else:
                return False
    
    
    def  check_product_state(product):
         with open(BOUGHT_PATH ,"r") as file:
            data = list(file)
            state = "true"
            for line in data[1:]:
                if product == line.split(',')[1].strip()  and state == line.split(',')[6].strip():
                    return True
            else:
                return False
    

    def update_state_in_stock(self,id):
        with open(BOUGHT_PATH, "r") as file:
            temp_bought_file = tempfile.NamedTemporaryFile(mode="w", delete=False, newline='')
            data = list(file)
            new_state = "false"
            tempwriter = csv.DictWriter(temp_bought_file, fieldnames=COLS,lineterminator="\n")
            tempwriter.writeheader()
            for line in data[1:]:
                if line.split(',')[0].strip() == id:                  
                    tempwriter.writerow({"id": line.split(',')[0].strip(), "product": line.split(',')[1].strip(), "sell_date": line.split(',')[2].strip(), "buy_price": line.split(',')[3].strip(), "amount": line.split(',')[4].strip(), "expiration_date": line.split(',')[5].strip(), "state": new_state})
                else:
                    tempwriter.writerow({"id": line.split(',')[0].strip(), "product": line.split(',')[1].strip(), "sell_date": line.split(',')[2].strip(), "buy_price": line.split(',')[3].strip(), "amount": line.split(',')[4].strip(), "expiration_date": line.split(',')[5].strip(), "state":line.split(',')[6].strip()}) 
            temp_bought_file.close()
            shutil.move(temp_bought_file.name, BOUGHT_PATH)
            Product.display("self",BOUGHT_PATH)
    
    
    def display(self,file):
        df = pd.read_csv(file)
        pd.options.display.max_columns = len(df.columns)
        df.columns = [x.upper() for x in df.columns]
        if df.empty:
                print('no products')
        else:
                print(df)   


    def date_to_integer(dt_time):
       
        return 10000*dt_time.year + 100*dt_time.month + dt_time.day
    

    def get_file_lenght(self, file_path):
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            reader_list = list(reader)
        return len(reader_list)
       

    def update_stock(self, product, amount, expirationsdate):
        """
       update amount stock
       TODO Wordt waarschijnlijk ook voor sold gebruikt aparte functie voor maken
       """
        with open(BOUGHT_PATH ,"r") as file:
            temp_bought_file = tempfile.NamedTemporaryFile(mode= "w", 
                                                delete= False)
            data = list(file)
            new_amount=0
            row_product = ""  
            tempwriter = csv.DictWriter( temp_bought_file, fieldnames = COLS, lineterminator="\n")
            tempwriter.writeheader()          
            for line in data[1:]:
                row_product =line.split(",")[1]
                row_amount = line.split(",")[4]
                row_amount = row_amount.strip('\n\r')               
                buy_amount = int(amount)
                new_amount = int(row_amount) + buy_amount  
                row_expiration = line.split(",")[5]            
                  
                # gebruik product andd experation date om juiste product te checken
                if row_product  == product and row_expiration == expirationsdate:

                    tempwriter.writerow({
                        "id": line.split(',')[0].strip(),
                        "product": line.split(',')[1].strip(),
                        "sell_date":line.split(',')[2].strip(),
                        "buy_price": line.split(',')[3].strip(),
                        "amount": new_amount,
                        "expiration_date":line.split(',')[5].strip(),
                        "state": line.split(',')[6].strip()})
                else:
                    tempwriter.writerow({
                    "id": line.split(',')[0].strip(),
                    "product": line.split(',')[1].strip(),
                    "sell_date":line.split(',')[2].strip(),
                    "buy_price": line.split(',')[3].strip(),
                    "amount": line.split(',')[4].strip(),
                    "expiration_date":line.split(',')[5].strip(),
                    "state": line.split(',')[6].strip()})
                
        temp_bought_file.close()
        shutil.move(temp_bought_file.name, BOUGHT_PATH)
        Product.display("self",BOUGHT_PATH)


  
