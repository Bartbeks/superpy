import csv
from pathlib import Path


def create_all_files( ):   
        """ Maak alle files aan 
        voor runnen programma"""
        report_inventory_path = Path.cwd()/"reports/report_inventory.csv"
        report_inventory_date = Path.cwd()/"reports/report_inventory_date.csv"
        report_expired_products = Path.cwd()/"reports/report_expired_product.csv"
        bought_path = Path.cwd()/"data/bought.csv"
        sold_path =  Path.cwd()/"data/sold.csv"
        internal_date_path =  Path.cwd()/"data/Internal_date.csv"
        COLS = ["id","product","sell_date","buy_price","amount","expiration_date","state"]
        COLS_SOLD = ["id","bought_id","sell_date","sell_price","amount"]
        Internal_date = ["0"]
        path_list = [report_inventory_path,report_inventory_date,report_expired_products,bought_path,sold_path,internal_date_path]
        for path in path_list:
            if path.is_file(): 
                print(f" {path} is OK")
        for path in path_list:
                with open(path , "w") as csvfile:
                        if path == sold_path:
                                writer = csv.DictWriter(csvfile, fieldnames=COLS_SOLD,lineterminator="\n")
                                writer.writeheader()
                               
                        if path == internal_date_path:
                                csvwriter = csv.writer(csvfile)
                                for _ in Internal_date:
                                        csvwriter.writerow(Internal_date)
                        if path == bought_path:
                                writer = csv.DictWriter(csvfile, fieldnames=COLS,lineterminator="\n")
                                writer.writeheader()
        # for path in path_list:
        #     with open(path , "r") as csvfile:
        #         reader = csv.DictReader(csvfile, fieldnames=COLS_SOLD,lineterminator="\n")
        return print("all files created")
