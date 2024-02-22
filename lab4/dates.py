from datetime import datetime,timedelta
nowd=datetime.now()
newd=nowd-timedelta(days=5)
print(newd)  
#ex1
today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Yesterday: ",yesterday.strftime("%d"))
print("Today: ", today.strftime("%d"))
print("Tomorrow: ",tomorrow.strftime("%d"))   
#ex2
nowd=datetime.now()
time_drop=nowd.replace(microsecond=0)
print(time_drop)   
#ex 3
first_d = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S") 
second_d = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
print((second_d-first_d).total_seconds())  
#ex 4