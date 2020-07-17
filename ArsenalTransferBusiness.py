
print("Hello and welcome to the Arsenal Football Club Transfer Window Simulator.")

user_name = raw_input("What is your name?: ")

print("Hello " + user_name + " my name is Josh Kroenke and I'm the Director of Arsenal. The summer transfer window is open and we need to strengthen our squad for next season.")

print("First we have to identify which players we want to sell")

#Below this point is the selling section of this transfer simulator.

transferList = {
    "Laca" : 45000000,
    "Guendouzi": 35000000,
    "Sokratis": 10000000,
    "Mustafi": 10000000,
    "Torreira": 35000000,
    "Chambers": 15000000,
    "Ozil": 5000000,
    }

print("These are the player(s) we are willing to sell and their values")
print(transferList)

#This set of functions allow the end user to remove items from the dictionary they wish to remove
rem_list = raw_input("Please input the players you would like to keep: ")
res = dict([(key, val) for key, val in transferList.items() if key not in rem_list])

print("These are the players you have decided to sell " + str(res))
#This function allows me to sum the total of the players remaining and print it to the console
values = res.values()
total_income = sum(values)
transfer_budget = total_income + 50000000
print("Selling all these players will leave us with " + str(transfer_budget) + " with the 5000000 budget added to it to strengthen the team.")


#This part of the code concerns with signing players in the CB position
print("Now that we have decided which players to sell, lets see the type of players we can sign. Lets look at the Defense first.")

transfer_targets_centrebacks = {
    "Tah": 35000000,
    "Upamecano": 50000000,
    "Disasi": 15000000,
    "Torres": 30000000,
    "Diop": 30000000
    }
    
print("These are the centrebacks we are looking at signing.")
print(transfer_targets_centrebacks)
    
no_cbs = raw_input("Please input the centrebacks you do not want to sign: ")
yes_cbs = dict([(key, val) for key, val in transfer_targets_centrebacks.items() if key not in no_cbs])
print("These are the centrebacks you have decided to sign " + str(yes_cbs))
cbvalues = yes_cbs.values()
cb_spend = sum(cbvalues)

print("You have spent " + str(cb_spend) + " on strenghtening the centre of the defense!")

print("Now that we've strengthened our weak backline. Lets move onto the defensive midfield")


transfer_targets_defensive_midfielders = {
    'Partey': 50000000,
    'Danilo': 25000000,
    'Phillips': 30000000,
    'Sangare': 15000000,
    'Roca': 15000000
    }
print("These are our transfer targets in the defensive midfield position")
print(transfer_targets_defensive_midfielders)

no_mfs = raw_input("Please input the defensive midfielders you do not want to sign: ")
yes_mfs = dict([(key, val) for key, val in transfer_targets_defensive_midfielders.items() if key not in no_mfs])
print("These are the defensive midfielders you have decided to sign " + str(yes_mfs))
mfvalues = yes_mfs.values()
mf_spend = sum(mfvalues)

print("You have spent " + str(mf_spend) + " on strenghtening the base of the midfield!")

print("Now that we have strengthened our mifield. Let's move onto the more attacking midfielders as we need more goals from midfield if we want to succeed this season.")


transfer_targets_attacking_midfielders = {
    'Grealish': 50000000,
    'Szoboszlai': 25000000,
    'Coutinho': 70000000,
    'Pellegrini': 30000000,
    'Ikhone': 40000000,
    'Lemar': 30000000
    }

print("These are our transfer targets in the attacking midfield position")
print(transfer_targets_attacking_midfielders)

no_ams = raw_input("Please input the attacking midfielders you do not want to sign: ")
yes_ams = dict([(key, val) for key, val in transfer_targets_attacking_midfielders.items() if key not in no_ams])
print("These are attacking the midfielders you have decided to sign " + str(yes_ams))
amvalues = yes_ams.values()
am_spend = sum(amvalues)

print("You have spent " + str(am_spend) + " on strenghtening the attacking section of the midfield!")

total_spend = cb_spend + mf_spend + am_spend

net_spend = transfer_budget - total_spend

if net_spend > 0:
    print("This is a viable transfer plan that leaves us with " + str(net_spend) + " left over. Excellent job!")
elif net_spend == 0:
    print("This is a viable plan that allows us to breakeven. Good job!")
else:
    print("This is not a viable transfer plan as it leaves us in debt to the tune of " + str(net_spend) + " Please try again and make sure to stay under the transfer budget.")
    high_value_players = { 
        "Aubameyang": 75000000,
        "Xhaka": 30000000,
        "Bellerin": 30000000,
        }
    
    print("If you still wish to pursue this transfer plan you may sell some of these players to fit under budget. You have three chances to make it work!")    
    
    no_raise_funds = raw_input("Please input the high value players you do not want to sell: ")
    yes_raise_funds = dict([(key, val) for key, val in high_value_players.items() if key not in no_raise_funds])
    print("These are the high value players you have decided to sell in order to raise funds " + str(yes_raise_funds))
    hvvalues = yes_raise_funds.values()
    hv_income = sum(hvvalues)
    
    final_income = transfer_budget + hv_income
    print(final_income - total_spend)
    if final_income < total_spend:
        print("Sorry. This still won't work. Try again by pressing the run button again!")
        
    
























#Future ideas
#- Make the user have to work within transfer budget. Maybe with a total spend allowed function - Done.
#-Add a loan list


    











