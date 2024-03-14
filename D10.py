import time
# timestamp = time.strftime('%H:%M:%S')    
# print(timestamp)
timestamp=time.strftime('%H')
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)

hour=int(timestamp)
if (hour<12):
    print("Good Morning, Mr.Tejash Patel")
elif(hour>=12 and hour<=19):
    print("Good Afternoon, Mr.Tejash Patel")
else:
    print("Good Night, Mr.Tejash Patel")