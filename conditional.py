# Rohan's Awesome Weather Checker! 😎

# Asking the user for the temperature
temp = int(input("hi, Rohan enter the temperature today in Celsius: "))

# Checking if it's warm enough for light clothes
if temp > 25:
    print("yes It is super warm outside! ")
    print("You can totally wear your light and soft clothes today!")

elif temp >= 15:
    print("The weather is okay, but it might get chilly")
    print("Maybe wear a light t-shirt but keep a hoodie nearby")

else:
    print("It is way too cold")
    print("Do not take off your jacket")