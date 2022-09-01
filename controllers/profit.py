from datetime import  datetime
from classes.purchase import Purchase
from classes.product import Product

def calc_profit(arg):
    today = datetime.now()
    #  calculate profit for store
    if arg== "all":
        selling_price =Purchase.revenue("self")
        purchased_price = Product.purchased_products("self")
        profit = selling_price - purchased_price    
        print( f"total profit = €.{profit}")
    #  calculate profit for today in   store 
    
    elif arg == today.strftime('%Y-%m-%d'):
        selling_price =Purchase.revenue_number_of_days("self",today.strftime('%Y-%m-%d'))
        purchased_price =Product.purchased_products_by_date('self',today)
        
        if selling_price == None: 
            
            return print("Nothing sold")
        profit = selling_price-purchased_price  
        print(f"todays profit = €.{profit}")

        
      
   