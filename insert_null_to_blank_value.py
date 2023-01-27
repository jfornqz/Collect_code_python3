import calendar
from dateutil.relativedelta import relativedelta
from datetime import timedelta
import datetime


def test():

    # Part check this month and this year
    today = datetime.date.today()
    this_month = int(today.strftime("%m"))
    this_year = int(today.strftime("%Y"))

    last_month = int((today - relativedelta(months=1)).strftime("%m"))
    last_year = int((today - relativedelta(months=1)).strftime("%Y"))

    days_in_this_month = calendar.monthrange(this_year, this_month)[1]
    days_in_last_month = calendar.monthrange(last_year, last_month)[1]
    max_day = max(days_in_this_month, days_in_last_month)

    # print(this_year, this_month)
    # print(last_year, last_month)
    print("----------------------------------------")

    # Get the current date
    current_date = datetime.date.today()

    # Subtract one month from the current date
    last_month = current_date - timedelta(days=30)


    # Find the number of days in a specific month
    year = 2023
    month = 1
    days_in_this_month = calendar.monthrange(year, month)[1]
    # It returns a tuple containing the first day of theweek and thenumber of days in thatmonth


    records = [(12.0, 105.20044, None), (13.0, 0.0, None), (14.0, 0.0, None), (15.0, 0.0, None), (16.0, 6630.299, None),
               (17.0, 0.0, None), (18.0, 0.0, None), (19.0, 0.0, None), (20.0, 0.0, None), (21.0, 0.0, None),
               (22.0, 0.0, None), (23.0, 0.0, None), (24.0, 0.0, None), (25.0, 30884.701, None), (26.0, 226.0, None)]

    objects_day = [oj[0] for oj in records]
    print("day in records:", objects_day)
    print(records)
    print(len(records))

    for day in range(1, max_day+1):
        if day not in objects_day:
            records.append([day, None, None])

    print('len record after append', len(records))
    print('record after append', records)

    selectObject = []
    columnNames = ['day', 'this_month', 'last_month']

    for record in records:
        selectObject.append(dict(zip(columnNames, record)))

    print(selectObject)
    sorted_selectObject = sorted(selectObject, key=lambda x: x['day'])
    print(sorted_selectObject)

    this_month = []
    last_month = []
    day = []

    for object in sorted_selectObject:
        this_month.append(object['this_month'])
        last_month.append(object['last_month'])
        day.append(int(object['day']))

    res = {
        'this_month': this_month,
        'last_month': last_month,
        'day': day,
    }
    print(res)


test()
