height= float(input("enter your number in cm"))
weight=float(input("enter your number in kg"))
bmi=weight / (height/100)**2
print("your bmi is " , round (bmi,2))
if bmi <= 18.4:
    print("you are under weight ")
elif bmi <= 24.9:
    print("you are healthy")
elif bmi <=29.9:
    print("you are severeky over weight")
elif bmi<=34.9:
    print ("you are obease,")
else:
    print("you are severely obease")