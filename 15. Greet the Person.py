import time
name = input("Enter your name ")
# print(time.strftime("%H:%M:%S"))

t=int(time.ctime().split(" ")[3].split(":")[0])
# print(time.ctime().split(" ")[2])


if(t>=0 and t<=11):
    print(f"Good Morning {name}...")
elif(t>=12 and t<=15):
    print(f"Good Noon {name}...")
elif(t>=16 and t<=20):
    print(f"Good Evening {name}...")
else:
    print(f"Good Night {name}...")
