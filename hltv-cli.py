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

    if(int(choice) == 0):
        menu()
    else:
        choice = int(choice) - 1

        players = list[choice].get('players')

        print(str(list[choice].get('name')))

        for i in range(5):
            print(players[i].get('name'))

def results():

    titles = ["Teams", "Result", "Map", "Event"]

    print("RESULTS")
    print("-------------------------------------------------------------------------------------------------------------")
    print("|" + titles[0].center(40) + "|" + titles[1].center(9) + "|" + titles[2].center(7) + "|" + titles[3].center(48) + "|")
    print("-------------------------------------------------------------------------------------------------------------")

    list = hltv.listresults()

    for i in range(30):
        teams = str(list[i].get('team1')) + " vs " + str(list[i].get('team2'))
        result = str(list[i].get('score1')) + " - " + str(list[i].get('score2'))
        map = str(list[i].get('map'))
        event = str(list[i].get('event'))

        print("|" + teams.center(40) + "|" + result.center(9) + "|" + map.center(7) + "|" + event.center(48) + "|")

    print("-------------------------------------------------------------------------------------------------------------")


def menu():

    print("Welcome to HLTV-CLI.py")
    print("Select a menu option")
    print("0 - Return")
    print("1 - Top 30 Teams")
    print("2 - Results")

    x = input()

    pick(int(x))

def pick(choice): 
    if choice == 0:
        menu()
    elif choice == 1:
        table30()
    elif choice == 2:
        results()
    else:
        print("Try again")

menu()