import csv
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
import shutil
import tempfile
from classes.product import BOUGHT_PATH, Product


SOLD_FILE = Path.cwd()/"data/sold.csv"
global revenue
COLS = ["id","bought_id","sell_date","sell_price","amount"]

class Purchase():
    def __init__(self, file_path, bought_id,sell_date,sell_price,amount):
        file_lenght = self.get_file_lenght(file_path)
        self.id = file_lenght-1
        self.bought_id = bought_id
        self.sell_date = sell_date
        self.sell_price = sell_price
        self.amount = amount


    def get_file_lenght(self, file_path):
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            reader_list = list(reader)
        return len(reader_list)


    def check_amount(self, product, purchased_amount):
        with open(BOUGHT_PATH ,"r") as file:
            data = list(file)
        for line in data[1:]:
            line_amount = line.split(',')[4].strip()
            if product == line.split(',')[1].strip() and( int(line_amount) >= int(purchased_amount)):
                    return True
        else:
            return False


    def check_amount_left(product):
        with open(BOUGHT_PATH ,"r") as file:
            data = list(file)
        for line in data[1:]:
            if line.split(',')[1].strip()==product:
                return line.split(',')[4].strip() 


    def stock_after_sell(self, product, purchased_amount):
        with open(BOUGHT_PATH ,"r") as file:
            temp_bought_file = tempfile.NamedTemporaryFile(mode= "w", 
                                                delete= False)
            data = list(file)
            new_amount=0
            tempwriter = csv.DictWriter( temp_bought_file, fieldnames = ["id","product","sell_date","buy_price","amount","expiration_date","state"], lineterminator="\n")
            tempwriter.writeheader()
        for line in data[1:]:   
                # als product in store update bougtfile en amount en registreer verkoop of update stock
            order_amount =int(purchased_amount)
            Line_product = line.split(",")[1]
            Line_amount = int(line.split(",")[4])
            if Line_product == product and Line_amount >0 and Line_amount >= order_amount:
                new_amount = Line_amount - order_amount
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
        # Product.display("self",BOUGHT_PATH)


    def write_2_buy(self, SOLD_FILE,bought_id, purchase_date, purchase_price, amount):
        today = datetime.now()
        today.strftime('%Y-%m-%d')
        new_purchase = Purchase(SOLD_FILE, bought_id, purchase_date, purchase_price, amount)
        with open(SOLD_FILE, "a+", newline="") as file:
             writer = csv.DictWriter(file, fieldnames=COLS)
             new_purchase = Purchase(SOLD_FILE, bought_id, purchase_date, purchase_price, amount)
             writer.writerow({
                    "id": new_purchase.id, 
                    "bought_id": new_purchase.bought_id, 
                    "sell_date": new_purchase.sell_date, 
                    "sell_price": new_purchase.sell_price, 
                    "amount": new_purchase.amount})
        Product.display("self",SOLD_FILE)
