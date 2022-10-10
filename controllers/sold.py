import csv
from pathlib import Path
from classes.purchase import Purchase
from classes.product import Product

SOLD_FILE = Path.cwd()/"data/sold.csv"
COLS = ["id","bought_id","sell_date","sell_price","amount"]
expires = False

"""sellProduct  "self empty arg", product, price, amount"""
def sell(self, bought_id, purchase_price, amount):
    """Check if product is in stock"""
    is_in_stock = Purchase.is_check_product_in_stock("self", bought_id)
    if not is_in_stock:
        """ Als het product niet bestaat """
        print(f"{bought_id} not in stock choose another product")
        return   
    if is_in_stock:
        """ check of het product vaker voorkomt 
        en maak keuze welk product je wil kopen
        """
    product_list = Purchase.is_check_product_in_stock_more_then_once("self", bought_id)
    if len(product_list)>1:  
        for product in product_list:         
            x = input(f" product komt vaker voor: wil je {product['product']} met experationdate: {product['expires']} kopen (yes or no) ").lower().strip()
            if x == "yes":
                 expires = Product.product_expires_in_stock(product['id'])
                 break                 
            elif x == "no":
                

                print("next product")              
            else:
               print("Error: Answer must be Yes or No")
        

    if len(product_list)<=1:
        for product in product_list:
         expires = Product.product_expires_in_stock(product['id'])
         
    """catch error na x aantal No """   
    try:
        if expires:
            Product.update_state_in_stock("self",product['id'])
            return  print("Warning product has expired!!!, not for sale ")
        if not expires: 
         """ Check of er genoeg voorraad is"""
        amount_ok = Purchase.check_amount("self",product['id'],amount)
        if amount_ok:
                """ update de voorraad na verkoop"""
                Purchase.stock_after_sell(self,product['id'],amount)
                Purchase.write_2_buy(self,SOLD_FILE,bought_id, purchase_price, amount)
                return;
        if not amount_ok:
           
            """ Als er te weinig voorraad is laat zien hoeveel er nog te koop zijn """
            number_left = Purchase.check_amount_left(product['id'])
            print(f" there is only {number_left} left for {bought_id }  You can order a maximum of {number_left} {bought_id}(en)")
            return
    except UnboundLocalError :
        return print("choose another product")
 
    
        
    
    """ Schrijf verkochte product naar de datbase """
    with open(SOLD_FILE, "a", newline="") as file:
        new_purchase = Purchase(SOLD_FILE, bought_id, purchase_price, amount)
        sold_dict ={
                "id": new_purchase.id-1, 
                "bought_id": new_purchase.bought_id, 
                "sell_date": new_purchase.sell_date, 
                "sell_price": new_purchase.sell_price, 
                "amount": new_purchase.amount}
        writer = csv.DictWriter(file, fieldnames=COLS)
        writer.writerow(sold_dict)
    Product.display("self",SOLD_FILE)
