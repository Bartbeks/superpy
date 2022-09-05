import csv
from pathlib import Path


def create_all_files( ):

    
        report_inventory_path = Path.cwd()/"reports/report_inventory.csv"
        report_inventory_date = Path.cwd()/"reports/report_inventory_date.csv"
        report_expired_products = Path.cwd()/"reports/report_expired_product.csv"
        bought_path = Path.cwd()/"data/bought.csv"
        sold_path =  Path.cwd()/"data/sold.csv"
        COLS = ["id","product","sell_date","buy_price","amount","expiration_date","state"]
        COLS_SOLD = ["id","bought_id","sell_date","sell_price","amount"]
        path_list = [report_inventory_path,report_inventory_date,report_expired_products,bought_path,sold_path]
        for path in path_list:
            if path.is_file(): 
                print(f" {path} is OK")

        for path in path_list:
                with open(path , "w") as csvfile:
                        if path ==sold_path:
                                writer = csv.DictWriter(csvfile, fieldnames=COLS_SOLD,lineterminator="\n")
                                            # writer.writerow({})
                        else:
                                writer = csv.DictWriter(csvfile, fieldnames=COLS,lineterminator="\n")
                        writer.writeheader()
        for path in path_list:
            with open(path , "r") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=COLS_SOLD,lineterminator="\n")
        return
