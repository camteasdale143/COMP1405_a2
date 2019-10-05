
class store_item:
    def __init__(self, name="null", cost=1.00, desc="null", set_name="null", num = 1):
        self.name = name
        self.cost = float(cost) 
        self.desc = desc
        self.set_name = set_name
        self.num = num;

store_items = [
        store_item("Oregano Shears", 25.99, "Multiple pairs will be required for larger oregano harvests", "pair", 0),
        store_item("Water Bottles", 7.95, "Good for keeping hydrated while on the search for the elusive oregano in it's dry sultry environment", "6 pack", 0 ),
        store_item("Energy Bars", 14.50, "Will give you the energy to keep moving while you are traversing the rocky oregan environment", "12 pack box", 0 ),
        store_item("Oregano Pigs", 150.00, "They 'find oregano for you' according the salesman, although it more seems like the salesman is trying to offload his poor investment", "pig", 0 ),
        store_item("Oregano Pipes", 400.00, "Illegal in these parts of the world, but apparently somebody smuggled a shipment down from up north", "pipe", 0 ),
        ]

character_descriptions= [
        "a student just looking to have some fun with your friends",
        "a stock broker searching for an escape from his stressful day job",
        "a coder trying to find something to help him relax before an all night coding session",
        "a pizza chef who's family business will go under if they don't find oregano"
        ]
title = """  ___  ____  _____ ____    _    _   _  ___    _____ ____      _    ___ _     
 / _ \|  _ \| ____/ ___|  / \  | \ | |/ _ \  |_   _|  _ \    / \  |_ _| |    
| | | | |_) |  _|| |  _  / _ \ |  \| | | | |   | | | |_) |  / _ \  | || |    
| |_| |  _ <| |__| |_| |/ ___ \| |\  | |_| |   | | |  _ <  / ___ \ | || |___ 
 \___/|_| \_\_____\____/_/   \_\_| \_|\___/    |_| |_| \_\/_/   \_\___|_____|"""

def sum(itemList):
    total = 0;
    for item in itemList:
        total += item.cost*item.num
    return total 


def main():                                                                            

    print("================================================================================\n{:s}\n================================================================================".format(title))

    print("The Oregano Trail is the most dangerous trail in the West, people from all around the country came to travel the trail in search of oregano. Due to such an influx of people into the state, travelling on the oregano trail has been outlawed along with the possession of any oregano. As such it is of extreme importance that you say exactly what needs to be said, clearly enough that it cannot be confused. Speaking in a roundabout or confusing way is a telltale sign of oregano possesion and will get you caught!\n\nMany people have attempted the dangerous trek to find the elusive wild oregano! Who will you be?")

    for idx, character in enumerate(character_descriptions):
        print("\t {0}. {1}".format(idx + 1, character))

    character = (int(input("\nWhat is your choice? ")) - 1)

    print("\nyou are {0}".format(character_descriptions[character]))

    print("\nIt is dangerous to go alone\nwhat is your name and the name of the 4 others you will take with you?")

    party = []

    for num in range(5):
        party.append(str(input("{0}. ".format(num + 1))))

    print("\nbefore you leave you should buy some things to bring with you")

    for item in store_items:
        item.num = (int(input("\n{0} cost ${1} a {3}. {2}. How many {0} would you like? ".format(item.name, item.cost, item.desc, item.set_name))))
        print("your current bill is: {:.2f}".format(sum(store_items)))

    print("\n==============================\n\tTHE OREGANO STORE\n==============================")
    for idx, item in enumerate(store_items):
        print("{:d}.   {:s} \t${:>.2f}".format(idx + 1, item.name, item.cost))
    print("==============================")

    print("\nYour total bill is: ${:.2f}".format(sum(store_items)))

    

try: 
    main()
except:
    print("\nYou got caught by the police while preparing for your trek and are now convicted of attempted oregano searching!\n\nYOU FAILED\n\n")
