import requests
import pandas as pd
import os

user_agent_headers = {'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

# this is the base url for player statistics.
baseURL_playerstat ='https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
# we also need some parameters.
parameters_playerstat = {
            
            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
            'GameSegment': '',
	    'Height': '',
            'LastNGames': 0,
            'LeagueID': '00',
            'Location': '',
            'Month': 0,
            'OpponentTeamID': 0,
            'Outcome': '',
            'PORound': 0,
            'PerMode': 'PerGame',
            'PlayerExperience': '',
            'PlayerPosition': '',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'ShotClockRange': '',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',

            #'College': '',
            #'Conference': '',
            #'Country': '',
            #'DateFrom': '',
            #'DateTo': '',
            #'Division': '',
            #'DraftPick': '',
            #'DraftYear': '',
            #'GameScope': '',
            #'GameSegment': '',
            #'Height': '',
            #'LastNGames': 0,
            #'LeagueID': '00',
            #'Location': '',
            #'MeasureType': 'Base',
            #'Month': 0,
            #'OpponentTeamID': 0,
            #'Outcome': '',
            #'PORound': 0,
            #'PaceAdjust': 'N',
            #'PerMode': 'PerGame',
            #'Period': 0,
            #'PlayerExperience': '',
            #'PlayerPosition': '',
            #'PlusMinus': 'N',
            #'Rank': 'N',
            #'Season': '2016-17',
            #'SeasonSegment': '',
            #'SeasonType': 'Regular Season',
            #'ShotClockRange': '',
            #'StarterBench': '',
            #'TeamID': 0,
            #'VsConference': '',
            #'VsDivision': '',
            #'Weight': '',
        }

# returns dataframe given base url, parameters.
def scrapeURL(baseURL, parameters):
    response = requests.get(baseURL, params=parameters, headers=user_agent_headers)
    response.raise_for_status()
    headers = response.json()['resultSets'][0]['headers']
    stats = response.json()['resultSets'][0]['rowSet']
    stats_df = pd.DataFrame(stats, columns=headers)
    stats_df['Season'] = parameters['Season']
    #stats_df.drop(['CFID', 'CFPARAMS'], axis=1, inplace=True)
    return stats_df

df_bio = scrapeURL(baseURL_playerstat, parameters_playerstat)
df_bio.head() # D A T A
df_bio = df_bio[df_bio['GP']>40]
df_bio = df_bio.drop(['TEAM_ID','TEAM_ABBREVIATION','AGE','PLAYER_HEIGHT','PLAYER_HEIGHT','PLAYER_WEIGHT','COLLEGE','COUNTRY','DRAFT_YEAR','DRAFT_ROUND','DRAFT_NUMBER','GP','PTS','REB','AST','NET_RATING','OREB_PCT','DREB_PCT','USG_PCT','TS_PCT','AST_PCT','Season'],1)
 
