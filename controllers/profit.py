from datetime import  datetime
from classes.reports import Reports


def calc_profit(arg):
 
    #  calculate profit for store
    if arg == "all":
        selling_price = Reports.revenue_all("self")
        purchased_price = Reports.purchased_products("self")
        profit = selling_price - purchased_price
        print( f"total sold = €.{selling_price}")     
        print( f"total profit = €.{profit}")
    
    #  calculate profit for internal_date in   store    
    else:
        selling_price = Reports.revenue_number_of_days("self",arg,"none")
        purchased_price = Reports.purchased_products_by_date('self',arg)
        if  selling_price is None:
            selling_price = 0
        elif not selling_price is None:
            profit = selling_price - purchased_price
           
            print( f"total sold = €.{selling_price}")     
            print( f"total bought = €.{purchased_price}") 
            print(f"todays profit = €.{profit}")
    
   


        
      
   