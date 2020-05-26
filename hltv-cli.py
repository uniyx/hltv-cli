import hltv
import curses

def table30():

    titles = ["Team", "Rank", "Points"]

    print("HLTV.ORG TOP 30 TEAMS")
    print("-------------------------------------------------")
    print("|" + titles[0].center(25) + "|" + titles[1].center(5) + "|" + titles[2].center(15) + "|")
    print("-------------------------------------------------")

    list = hltv.top30()

    for i in range(30):
        name = str(list[i].get('name'))
        rank = str(list[i].get('rank'))
        points = str(list[i].get('points'))

        print("|" + name.center(25) + "|" + rank.center(5) + "|" + points.center(15) + "|")

    print("-------------------------------------------------")

    ##INPUTS

    list = hltv.top30()
    choice = input("Choose the rank of the team you want to view: ")

    if(choice == 0):
        menu()
    else:
        choice = int(choice) - 1

        players = list[choice].get('players')

        print(str(list[choice].get('name')))

        for i in range(5):
            print(players[i].get('name'))

def menu():

    print("Welcome to HLTV-CLI.py")
    print("Select a menu option")
    print("1 - Top 30 Teams")
    print("2 - Results")

    x = input("")

    pick(x)

def pick(choice): 
    switcher = { 
        1: table30(), 
        2: "one", 
        3: "two", 
    } 

menu()