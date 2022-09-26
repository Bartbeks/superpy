from datetime import  datetime
from classes.reports import Reports


def calc_profit(arg):
    today = datetime.now()
    #  calculate profit for store
    if arg == "all":
        selling_price = Reports.revenue_all("self")
        purchased_price = Reports.purchased_products("self")
        profit = selling_price - purchased_price
        print( f"total sold = €.{selling_price}")     
        print( f"total profit = €.{profit}")
    
    #  calculate profit for today in   store    
    elif arg == today.strftime('%Y-%m-%d'):
        selling_price = Reports.revenue_number_of_days("self",today.strftime('%Y-%m-%d'))
        purchased_price = Reports.purchased_products_by_date('self',today)
        if  selling_price is None:
            selling_price = 0
        elif not selling_price is None:
            profit = selling_price - purchased_price
            # breakpoint()
            print( f"total sold = €.{selling_price}")     
            print( f"total bought = €.{purchased_price}") 
            print(f"todays profit = €.{profit}")
    
   


        
      
   