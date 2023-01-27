import calendar
from dateutil.relativedelta import relativedelta
from datetime import timedelta
import datetime


def max_day():
    # Part check this month and this year
    today = datetime.date.today()
    this_month = int(today.strftime("%m"))
    this_year = int(today.strftime("%Y"))

    last_month = int((today - relativedelta(months=1)).strftime("%m"))
    last_year = int((today - relativedelta(months=1)).strftime("%Y"))

    # monthrange include('year', 'month')[1] < return last day of month
    days_in_this_month = calendar.monthrange(this_year, this_month)[1]
    days_in_last_month = calendar.monthrange(last_year, last_month)[1]

    # find max day between two month
    max_day = max(days_in_this_month, days_in_last_month)

    print("max day of this 2 month is: ", max_day)
    print("----------------------------------------")

max_day()
