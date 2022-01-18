
#Create an empty dictionary to store Bidders name and amount
Bidders = {}

#Define the highest Bidder
def highest_Bidder():
    #Ge the highest amount
    max_value = max(Bidders.values())
    #Get the name of the highest amount
    max_name = max(Bidders , key=Bidders.get)
    print(f"The Winner is {max_name} with an amount of {max_value}")


#While loop to accept Biders and amount
Bidding_finished = False
while Bidding_finished == False:
    name = input("\nWhat's your name: ")

    #Try and except the user amount to enter in numbers
    try:
        amount = float(input("\nWhat's the amount you want to bid $: "))
    except:
        amount = float(input("\nPlease enter amount in numbers $:"))
    
    #Store the User's name and amount in Bidders dictionary
    Bidders[name] = amount
    #Ask If there's other Bidders
    ask = input("\nAre there other Bidders? Yes or No ").lower()

    #If statement to terminate the while loop
    if ask == "no":
        Bidding_finished = True
        #Call the function highest_Bidder
        highest_Bidder()
        break
