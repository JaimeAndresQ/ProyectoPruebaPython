age = int(input("How old are you?: "))
while age < 0: 
    print("It is not a valid age, please enter a valid age!!")
    age = int(input("How old are you?: "))
else:
    if age >= 18: 
        print("You are adult in Colombia")
    else:
        print("You aren't adult in Colombia")