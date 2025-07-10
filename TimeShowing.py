import time
timestamp = time.strftime('%H:%M:%S')
print("Now, The time is: " , timestamp)
hour = int(time.strftime("%H"))

if(hour>12 and hour<=17):
    print("GOOD AFTERNOON Dear")
if(hour>17 and hour<=24):
    print("GOOD NIGHT Dear")
elif():
    print("GOOD MORNING Dear\nHave a good day!")

okay = input("Thank you")