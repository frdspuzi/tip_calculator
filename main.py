#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("WELCOME TO THE TIP CALCULATOR");
bill= float(input("What was the total bill? $"));

tip= int(input("What percentage tip would you like to give? 10, 12 or 15?"));

numOfPeople= int(input("How many people to split the bill? "));

split = float(bill/numOfPeople);

if (tip == 10):
	splitAfterTip=  split*1.10;
	print(split," x ",1.10,"= ",splitAfterTip);

elif (tip == 12):
	splitAfterTip=  split*1.12;
	print(split," x ",1.12,"= ",splitAfterTip);

elif (tip == 15):
	splitAfterTip=  split*1.15;
	print(split," x ",1.15,"= ",splitAfterTip);

total= "{:.2f}".format(splitAfterTip)
print(f"Each person should pay: ${total}");
