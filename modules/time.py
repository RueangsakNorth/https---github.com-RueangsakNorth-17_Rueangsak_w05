from datetime import datetime,date, timedelta
today = date.today()

# print(f"วันที่ {today}")
# print(f"วัน {today.day}")
# print(f"เดือน {today.month}")
# print(f"ปี {today.year}")

now = datetime.now()
# print(f"เวลาปัจจุบัน :{now}")
# print(f"เวลาปัจจุบัน Hr :{now.hour}")
# print(f"เวลาปัจจุบัน m :{now.minute}")
# print(f"เวลาปัจจุบัน s :{now.second}")

# จัด format วดป
# formatted_date = now.strftime("%d-%m-%y")
# print(formatted_date)

# formatted_time = now.strftime("%H-%M-%S")
# print(formatted_time)

tomorow = today+timedelta (days=1)


yasterday = today-timedelta(days=1)
print(yasterday)
nextweek = today+timedelta(days=7)
print(nextweek)
nextmount = today+timedelta(days=30)
print(nextmount)

