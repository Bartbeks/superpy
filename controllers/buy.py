from datetime import date, datetime
from classes.product import Product
from pathlib import Path
from decimal import Decimal


bought_file = Path.cwd()/"data/bought.csv"
today = datetime.now()
# COLS = ["ID","PRODUCT","SELLDATE,BUYPRICE","AMOUNT","EXPERATIONDATE","STATE"]

def buy( product_name, purchase_price,amount,expires,state):
     # sourcery skip: hoist-statement-from-if, none-compare, remove-redundant-if, use-named-expression
    # Check if product exists
     product_exist_in_stock = Product.is_check_product_in_stock("self",product_name)
     if product_exist_in_stock:
        product_expires_in_stock = Product.product_expires_in_stock(product_name)  # Check of product expires is
        if product_expires_in_stock:
            check_product_state = Product.check_product_state(product_name)
            if check_product_state :
                Product.update_state_in_stock("self",product_name)
                print(f"WARNING {product_name } Not for sale, product is expired must be removed from store !!!")
            elif not check_product_state:
                 print(f"WARNING {product_name } Not for sale, product is expired must be removed from store !!!")
        elif product_expires_in_stock == None:
            # eerste run
             Product.add_product("self",product_name, purchase_price,amount,expires,state)
        elif not product_expires_in_stock:             
            Product.update_stock("self",product_name,int(amount))
            # update aantal in de inventaris        
     else:
        Product.add_product("self",product_name, purchase_price,amount,expires,state)
    