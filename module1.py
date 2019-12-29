# MOdule is a set of functions to include in your applicaton. Core python modules can be installed
#using pip package manager
#ex: of core module datatime
import datetime
today_dte = datetime.date.today()
print(today_dte)

# import the method you need from the module
from datetime import date
today_dte = date.today()
print(today_dte)

from time import time

tm_stmp = time()
print(tm_stmp)


#Custom module
#import validator
from validator import validate_email
email = 'VIKy@gmail.com'
if validate_email(email):
    print('ITs Vlaid Email')
else:
    print('INvalid EMail')
