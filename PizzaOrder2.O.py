print("Welcome to MG Pizza!")
no_of_pizza=input("Enter the Number of Pizza:\n")
num_of_pizza=int(no_of_pizza)
bill=0
if num_of_pizza == 1:
    size=input("What Size? S,M or L\n")
    if size == "S":
        bill=7
        print("Small Pizza is $7.")
    if size == "M":
        bill=14
        print("Medium Pizza is $14.")
    if size == "L":
        bill=20
        print("Large Pizza is $20.")
if num_of_pizza > 1:
    s_pizza=int(input("Enter the Number of Small Pizza: \n"))
    m_pizza=int(input("Enter the Number of Medium Pizza: \n"))
    l_pizza=int(input("Enter the Number of Large Pizza: \n"))
    bill=s_pizza*7 + m_pizza*14 + l_pizza*20
    print(f"Your Order is ${bill}.")
extra_dipping=input("Do you want extra dippings? \nEach Pizza $1.\nYes or No \n")
extra_cheese=input("Do you want us to add extra cheese in your pizza? \nEach Pizza $1.\nYes or No \n")
if extra_dipping == "Yes":
    bill=num_of_pizza+bill
if extra_cheese == "Yes":
    bill=num_of_pizza+bill
print(f"Your Total Bill is ${bill}.\n Thank you and Enjoy your Meal.")

    

