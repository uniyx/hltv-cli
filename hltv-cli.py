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

table30()