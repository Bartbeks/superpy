from datetime import date, datetime
from classes.product import Product
from pathlib import Path



bought_file = Path.cwd()/"data/bought.csv"
today = datetime.now()


def buy( product_name, purchase_price,amount,expires):

     """ Inkoop van het product"""
     # sourcery skip: hoist-statement-from-if, none-compare, remove-redundant-if, use-named-expression
   
     product_exist_in_stock = Product.is_check_product_in_stock("self",product_name,expires)  # Check if product exists
     if product_exist_in_stock:
        product_expires_in_stock = Product.product_expires_in_stock(product_name)  # Check if product expires 
        if product_expires_in_stock:
            check_product_state = Product.check_product_state(product_name)  # Check state of product
            if check_product_state :
                Product.update_state_in_stock("self",product_name) # update state in stock
                print(f"WARNING {product_name } Not for sale, product is expired must be removed from store !!!")
            elif not check_product_state:
                 print(f"WARNING {product_name } Not for sale, product is expired must be removed from store !!!")
                
        elif product_expires_in_stock == None:
             """De eerste keer returned expires in stock none"""
             """voeg het product toe"""
             Product.add_product("self",product_name, purchase_price,amount,expires)
        elif not product_expires_in_stock:  
            """Als het product al bestaat update stock"""           
            Product.update_stock("self",product_name,int(amount),expires)  # update aantal in de inventaris  
                 
     else:
        """voeg het product toe"""
        Product.add_product("self",product_name, purchase_price,amount,expires)
    