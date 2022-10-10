from datetime import date, datetime, timedelta
from decimal import Decimal
import decimal



"""check if user input  date is valid date"""
def validate_date(arg_date):
    isValidDate = True
    try:
            year, month, day = arg_date.split('-')
            tmp_date = datetime(int(year), int(month), int(day))
         
            present = datetime.now()
            present.strftime('%Y-%m-%d')
            if tmp_date <= present:
             
                return False
            
    except ValueError :
            isValidDate = False
    if(isValidDate):
            tmp_date = datetime(int(year), int(month), int(day))
            date = tmp_date.strftime('%Y-%m-%d')
            return date        
    else:
        return False


"""check if user input price is decimal"""
def validate_decimal(price):
    try: 
        purchase_price = Decimal(price)
        
        if purchase_price >=0:
            return True
        if purchase_price < 0:
             return False
    except ( decimal.InvalidOperation):
        return False


"""check if user input amount is int"""
def validate_int(amount):
    try:
        is_int = isinstance(int(amount), int)
       

        if is_int and int(amount)>0:
            return True
        else:
            return False
    except ValueError:
        return False
    except TypeError:
        return False


    

        
        

  

