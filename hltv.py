import requests
from bs4 import BeautifulSoup as bs


def top5():
    html = requests.get("https://www.hltv.org")
    hltv = bs(html.text, "lxml")

    teams = []

    for team in hltv.findAll("div", {"class": ["col-box rank"], }):
        teamname = team.text
        teams.append(teamname[3:])
    print(teams)


def top30():
    html = requests.get("https://www.hltv.org/ranking/teams")
    hltv = bs(html.text, "lxml")

    teams = []

    for team in hltv.findAll("div", {"class": ["ranked-team standard-box"], }):

        newteam = {'name': team.find('div', {"class": "ranking-header"}).select('.name')[0].text.strip(),
                   'rank': team.find('div', {"class": "ranking-header"}).select('.position')[0].text.strip(),
                   'points': team.find('div', {"class": "ranking-header"}).select('.points')[0].text.strip("()points "),
                   'id': team.find('img').get('src').strip("https://static.hltv.org/images/team/logo/"),
                   'players': []}

        for player in team.findAll("td", {"class": ["player-holder"], }):

            newplayer = {'name': player.select('.pointer')[0]['href'][8:].split("/")[1],
                         'id': player.select('.pointer')[0]['href'][8:].split("/")[0]}

            newteam['players'].append(newplayer)

        teams.append(newteam)
    return(teams)

def listresults():
    html = requests.get("https://www.hltv.org/results")
    hltv = bs(html.text, "lxml")

    results = []

    sublist =  hltv.findAll("div", {"class": "results-holder", })[2]

    for result in sublist.findAll("div", {"class": "result-con", }):

        newresult = {'team1': result.find('div', {"class": "line-align team1"}).select('.team ')[0].text.strip(),
                     'team2': result.find('div', {"class": "line-align team2"}).select('.team ')[0].text.strip(),
                     'score1': result.find('td', {"class": "result-score"}).findAll('span')[0].text.strip(),
                     'score2': result.find('td', {"class": "result-score"}).findAll('span')[1].text.strip(),
                     'event': result.find('span', {"class": "event-name"}).text.strip(),
                     'map': result.find('div', {"class": "map-text"}).text.strip()
        }

        results.append(newresult)
    return(results)