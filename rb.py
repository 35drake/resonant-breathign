import time
from datetime import datetime
from datetime import date
import random

Trial_time = 2 #normally is 2, for 2 minutes

def countdown(a):
	a=int(100*a)
	while a > 0:
		time.sleep(1/100)
		a = a - 1
		if a%10 == 0:
			if a%100 == 0:
				print(a/100)
			else:
				if a%20 == 0:
					print(".")
		

# MAIN PROGRAM:

#Frac = float(input("Inhalation fraction: "))
#Bpm = float(input("Breaths per minute: "))
#Trial_time = float(input("Minutes of trial (put 2): "))  #minutes to run trial

#Since the low frac's were so bad, I'm eliminating 0.3 and 0.35
Frac = random.choice([0.4,0.45,0.5])
Bpm = random.choice([5,5.5,6,6.5,7])


inhale = 60/Bpm*Frac
exhale = 60/Bpm*(1-Frac)

input("Pausing (press ENTER)")


print("\nTwo practice runs start in:")
for a in range(3):
	print(3-a)
	time.sleep(1)
for a in range(2):
	print("\nINHALE")
	countdown(inhale)
	print("\nEXHALE")
	countdown(exhale)
print("Practice over.\n")




for a in range(int(Trial_time*Bpm+1)):
	print("\nINHALE")
	countdown(inhale)
	print("\nEXHALE")
	countdown(exhale)
time_total = 60/Bpm*(int(Trial_time*Bpm+1))

num = int(input("How many heartbeats? "))

comments = input("Comments? ")

print(str(int(Trial_time*Bpm+1))+" breaths in "+str(time_total)+" seconds.")

result=num/time_total*60
print("Heartbeats per minute: "+str(result))



now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date=str(date.today())


writing = str(Frac)+","+str(Bpm)+","+str(result)+","+str(time_total)+","+current_time+" on "+current_date+","+comments+"\n"

print(writing)
the_database = open("rb-results.txt","a")
the_database.write(writing)
the_database.close()