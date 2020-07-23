import math

# firstly asked user to choose between the different options namely investment or bond

print("Choose either 'investment' or 'bond' from the menu blow to proceed:")

choice = input("enter choice here ").lower()
print(choice)

# made sure no matter what way the said options get typed out the program will response
# acorddinly with the parameters i have set.

if choice == "investment":
    deposit = float(input("put in deposit "))
    interest_rate = float(input("interest rate % "))/100
    time = int(input("year of investment "))
    investment_choice = input("simple or compound ").lower()
    if investment_choice == "simple":
        A = deposit*(1 + interest_rate * time)
    elif investment_choice == "compound":
        A = deposit * math.pow((1 + interest_rate), time)
    print(round(A ,2))

# next the option for the invesment selection with its own conditons were made
# user is required to enter a few pieces of information for the program to
# give and accurate answer.

elif choice == "bond":
    house_value = float(input(" put in value of house"))
    interest_rate = float(input("interest rate in months % "))/100
    time = int(input("months they plan on repaying"))

# following that the option for the bond selection had its own conditions made
# which again aske the user to enter a certain amount of information to do a
# accurate calculation for the user.
    

    x = house_value * ((interest_rate / 100 / 12 * (1 + interest_rate / 100 / 12) ** time) / (((1 + interest_rate / 100 / 12) ** time) - 1))
#   x = (interest_rate*house_value)/(1 - math.pow((1+ interest_rate),-time))   
    print(round(x ,2))

else:
    print("invalid input")

# finally the else function is there incase the inputs provided is invalid
# and will inform the user of this so they can stop and check to add the information
# as required.
