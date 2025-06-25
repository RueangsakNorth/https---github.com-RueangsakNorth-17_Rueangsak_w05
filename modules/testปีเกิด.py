from datetime import datetime,date, timedelta
today = date.today()
now = datetime.now()
brith_day = date(2000,9,26)
def cal_age(brith_day):
    age = today.year - brith_day.year
    return
age=cal_age(brith_day)
print(age)
