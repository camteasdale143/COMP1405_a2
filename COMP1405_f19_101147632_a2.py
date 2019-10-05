# name:  Cameron Tesadale 
# student num: 101147632
title = """  ___  ____  _____ ____    _    _   _  ___    _____ ____      _    ___ _     
 / _ \|  _ \| ____/ ___|  / \  | \ | |/ _ \  |_   _|  _ \    / \  |_ _| |    
| | | | |_) |  _|| |  _  / _ \ |  \| | | | |   | | | |_) |  / _ \  | || |    
| |_| |  _ <| |__| |_| |/ ___ \| |\  | |_| |   | | |  _ <  / ___ \ | || |___ 
 \___/|_| \_\_____\____/_/   \_\_| \_|\___/    |_| |_| \_\/_/   \_\___|_____|"""


def main():                                                                            

    print("================================================================================\n{:s}\n================================================================================".format(title))
    
    print("The Oregano Trail is the most dangerous trail in the West, people from all around the country came to travel the trail in search of oregano. Due to such an influx of people into the state, travelling on the oregano trail has been outlawed along with the possession of any oregano. As such it is of extreme importance that you say exactly what needs to be said, clearly enough that it cannot be confused. Speaking in a roundabout or confusing way is a telltale sign of oregano possesion and will get you caught!\n\nMany people have attempted the dangerous trek to find the elusive wild oregano! Who will you be?")

    print("\t 1. a student just looking to have some fun with your friends")
    print("\t 2. a stock broker searching for an escape from his stressful day job")
    print("\t 3. a coder trying to find something to help him relax before an all night coding session")
    print("\t 4. a pizza chef who's family business will go under if they don't find oregano")

    character = (int(input("\nWhat is your choice? ")) - 1)

    print("\nIt is dangerous to go alone\nwhat is your name and the name of the 4 others you will take with you?")

    partyNum1 = str(input("What is the name of party member #1: "))
    partyNum2 = str(input("What is the name of party member #2: "))
    partyNum3 = str(input("What is the name of party member #3: "))
    partyNum4 = str(input("What is the name of party member #4: "))
    partyNum5 = str(input("What is the name of party member #5: "))

    print("\nbefore you leave you should buy some things to bring with you")
    
    item1 = int(input("\nOregano Shears cost $25.99 a pair. Multiple pairs will be required for larger oregano harvests. How many pairs would you like? "))
    print("your current bill is: {:.2f}".format(25.99 * float(item1)))
    item2 = int(input("\nWater Bottles cost $7.95 a 6 pack. Good for keeping hydrated while on the search for the elusive oregano in it's dry sultry environment. How many 6 packs would you like? "))
    print("your current bill is: {:.2f}".format(25.99 * float(item1) + 7.95 * float(item2)))
    item3 = int(input("\nEnergy Bars cost $14.50 a 12 pack box. Will give you the energy to keep moving while you are traversing the rocky oregano environment. How many 12 pack boxes would you like? "))
    print("your current bill is: {:.2f}".format(25.99 * float(item1) + 7.95 * float(item2) + 14.50 * float(item3)))
    item4 = int(input("\nOregano Pigs cost $150.00 a pic. They 'find oregano for you' according to the salesmon, although the desperation in his eyes seems like he is just trying to get rid of some regular pigs. How many pigs would you like? "))
    print("your current bill is: {:.2f}".format(25.99 * float(item1) + 7.95 * float(item2) + 14.50 * float(item3) + 150.00 * float(item4)))
    item5 = int(input("\nOregano Pipes cost $400.00 a pipe. They are illegal in these parts of the world, but apparently somebody smuggled a shipment down from up north. How many oregano pipes would you like? "))
    print("your current bill is: {:.2f}".format(25.99 * float(item1) + 7.95 * float(item2) + 14.50 * float(item3) + 150.00 * float(item4) + 400.00 * float(item5)))
    
    print("\n==============================\n\tTHE OREGANO STORE\n==============================")
    print("1.   Oregano shears \t${:>.2f}".format(25.99 * float(item1)))
    print("2.   Water Bottles \t${:>.2f}".format(7.95 * float(item2)))
    print("3.   Energy Bars \t${:>.2f}".format(14.50 * float(item3)))
    print("4.   Oregano Pigs \t${:>.2f}".format(150.00 * float(item4)))
    print("5.   Oregano Pipes \t${:>.2f}".format(400.00 * float(item5)))
    print("==============================")

    print("\nYour total bill is: ${:.2f}".format(25.99 * float(item1) + 7.95 * float(item2) + 14.50 * float(item3) + 150.00 * float(item4) + 400.00 * float(item5)))
try: 
    main()
except:
    print("\nYou got caught by the police while preparing for your trek and are now convicted of attempted oregano searching!\n\nYOU FAILED\n\n")
