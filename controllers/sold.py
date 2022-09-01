import csv
from pathlib import Path
from classes.purchase import Purchase
from classes.product import Product

SOLD_FILE = Path.cwd()/"data/sold.csv"
COLS = ["id","bought_id","sell_date","sell_price","amount"]


def sell(self, bought_id, purchase_date, purchase_price, amount):
    is_in_stock = Product.is_check_product_in_stock("self", bought_id)
    if is_in_stock:
        expires =Product.product_expires_in_stock(bought_id)
        if expires:
            Product.update_state_in_stock("self",bought_id)
            return  print("Warning product has expired!!!, not for sale ")
        if not expires: 
            # check of er genoeg op voorraad is
            amount_ok = Purchase.check_amount("self",bought_id,amount)
            if amount_ok:
                    Purchase.stock_after_sell(self,bought_id,amount)
                    Purchase.write_2_buy(self,SOLD_FILE,bought_id, purchase_date, purchase_price, amount)
                    return;
            if not amount_ok:
                number_left = Purchase.check_amount_left(bought_id)
                print(f" there is only {number_left} left for {bought_id }  You can order a maximum of {number_left} {bought_id}(en)")
                return
    if not is_in_stock:
        print(f"{bought_id} not in stock")
        return
    with open(SOLD_FILE, "a", newline="") as file:
        new_purchase = Purchase(SOLD_FILE, bought_id, purchase_date, purchase_price, amount)
        sold_dict ={
                "id": new_purchase.id-1, 
                "bought_id": new_purchase.bought_id, 
                "sell_date": new_purchase.sell_date, 
                "sell_price": new_purchase.sell_price, 
                "amount": new_purchase.amount}
        writer = csv.DictWriter(file, fieldnames=COLS)
        writer.writerow(sold_dict)
    Product.display("self",SOLD_FILE)
