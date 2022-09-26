# Imports
import argparse

from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation
import decimal
from itertools import product 
from pathlib import Path
from classes.product import Product
from classes.purchase import Purchase
import controllers.buy as buy_inventory
import controllers.sold as sell
import controllers.profit as cp
import controllers.filecreater as fc
import controllers.load_dummy_data as ld
import controllers.plot as plot
import controllers.validate as valid
import controllers.date_setter as date_setter

from classes.reports import Reports





 
# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.




def main():  # sourcery skip: extract-method, for-append-to-extend
    parser = argparse.ArgumentParser(prog="main.py", description="Keep track of supermarket inventory." )
    parser.add_argument("--operation", help="operation to operate"
                   ,choices=["start,buy", "sold","report_inventory"] )
    subparsers = parser.add_subparsers(dest='command')
    start = subparsers.add_parser("start", help="required to run te program")
    setdate = subparsers.add_parser("setdate",help="set internal date")
    setdate.add_argument("--num_of_days",help="set internal date by number of days ",type= int)
    buy = subparsers.add_parser('buy', help='store bought products in inventory')
    buy.add_argument('--product_name', help="name of product",type = str)
    buy.add_argument("--purchase_price", help="price of product", type = str)
    buy.add_argument("--amount", help="amount of products")
    buy.add_argument("--now", help="date of today , format 2022-08-21")
    buy.add_argument("--expires", help="expiration date of product , format 2022-08-21")
   
    sold = subparsers.add_parser('sold',help='store sold products in inventory')
    sold.add_argument("--sp", help="sell price of product", type = str)
    sold.add_argument("--b", help="name of sold product",type = str)
    
    sold.add_argument("--amount", help="amount of products",type = str) 
    inventory = subparsers.add_parser('inventory', help='get inventory')
    inventory.add_argument("--advance_time", help="get de inventory by number of days in history ",type= int) 
    revenue = subparsers.add_parser('revenue', help='get revenue of store')
    revenue.add_argument("--advance_time", help="get de revenue by  number of days in history ",type= int)
    revenue.add_argument("--by_date", help="get de revenue by date date , format 2022-08-21",type= str) 
    profit = subparsers.add_parser('profit', help='calculate profit of the store')
    profit_today = subparsers.add_parser('profit_today', help='calculate profit today in store')
    profit_by_range = subparsers.add_parser('profit_by_range', help='calculate profit of the today in of store by a range of dates')
    profit_by_range.add_argument("--start", help="start date for profit by range, format 2022-08-21",type= str)
    profit_by_range.add_argument("--end", help="end date for profit by range , format 2022-08-21",type= str)
    expired = subparsers.add_parser('expired', help='create report of all expired products ')
    expired.add_argument("products", help="create report expired products" ,type= str)
    graphic = subparsers.add_parser('graphic', help='info grafic of stock')
    graphic.add_argument('stock_graphic', help='info grafic of stock')
   
    
    args = parser.parse_args()
     
     
    if args.command == "start":     
        fc.create_all_files()
    
    if args.command == "setdate":
        num_of_days = args.num_of_days 
        date_setter.set_num_of_days(num_of_days)
        date_setter.read_nums_of_days()

  
    if args.command == "buy":
        """buy products for inventory"""
        
        inputDate = args.expires
        input_price = args.purchase_price
        amount = args.amount
        """check if is valid date"""
        args.expires = valid.validate_date(inputDate)
        """check if is valid decimal"""
        args.purchase_price = valid.validate_decimal(input_price)
        """check if is valid integer"""
        args.amount = valid.validate_int(amount)
        
        
        if args.expires == False:
            return print("Input expires is not valid.. try again")
        if args.purchase_price == False:
            return print("Input price is not valid.. try again")
        if args.amount == False:
            return print("amount is not valid.. try again")
         
        else:
            buy_inventory.buy(args.product_name.lower(), round(Decimal(input_price),2), int(amount), args.expires)
      
    
    if args.command == "sold":
        """sell products """
       
        input_price = args.sp
        amount = args.amount
       
        """check if is valid decimal"""
        args.purchase_price = valid.validate_decimal(input_price)
        """check if is valid integer"""
        args.amount = valid.validate_int(amount)

        
        if args.purchase_price == False:
            return print("Input price is not valid.. try again")
        if args.amount == False:
            return print("amount is not valid.. try again")
        sell.sell("self",args.b.lower(),  round(Decimal(input_price),2),int(amount))
       
    if args.command == "inventory":
        if args.advance_time:
           today = datetime.now()
           searchdate = today + timedelta(days=args.advance_time)
           """inventory number of days in history   """
           Reports.report_date_inventory("self",searchdate.strftime('%Y-%m-%d'))
        else:
            """report inventory """
            Reports.report_inventory("self")
    
    if args.command == "revenue":
        if args.advance_time:
           today = datetime.now()
           searchdate = today + timedelta(days=args.advance_time)
           """revenue number of days in history   """
           Reports.revenue_number_of_days("self",searchdate.strftime('%Y-%m-%d'))
        
        if args.by_date:
           today = datetime.now()
           searchdate = args.by_date
           """revenue today"""
           Reports.revenue_number_of_days("self",searchdate)
        else:
            """overall revenue """
            Reports.revenue_all("self")
   
    if args.command == "profit":
        cp.calc_profit("all")
        
    if args.command == "profit_today":
        today = datetime.now()
        search_date = today.strftime('%Y-%m-%d')
        cp.calc_profit(search_date)
    
    if args.command == "profit_by_range":
        """ create report profit by time range  start and end date"""
        Reports.calc_profit_by_range("self",args.start, args.end)

    if args.command == "expired":
        """ create report expired products"""
        Reports.report_expired("self")
        # Reports.calc_profit_by_range("self",args.start, args.end)
   
    if args.command == "graphic":
        """ create info grafic bought en sold products"""
        plot.stock_plot()
       
     
   
if __name__ == "__main__":
    main()
