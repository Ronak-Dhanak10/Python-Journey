# DATE AND TIME IN PYTHONE 
# EXCERSIE ON IF ELSE
import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if int(time.strftime('%H')) < 12:
    print("Good Morning")
elif int(time.strftime('%H')) < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))    
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)