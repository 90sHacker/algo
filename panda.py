import pandas as pd
from datetime import datetime


dates = pd.date_range('2022-10-31', '2022-11-23')

dt = [datetime.strftime(date,'%Y-%m-%d') for date in dates]

#date = [date for date in dates.to_pydatetime().tolist()]
print(dt)

now = datetime.now().strftime('%Y-%m-%d')
print(now in dt)

#date filter fn
# args - msg date, dateTrom, dateTo
# if dateFrom and dateTo - generate date_range
# check if msg date in date_range - return true or false
# else check if date is equal to current date - return true or false

#if output from date filter is false return att_err
