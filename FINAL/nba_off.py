import requests
import pandas as pd
import os
import time

user_agent_headers = {'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

# URL SHOT DISTANCE.
baseURL_playerstat_shotdist ='https://stats.nba.com/stats/leaguedashplayershotlocations?College=&Conference=&Country=&DateFrom=&DateTo=&DistanceRange=5ft+Range&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL 3PT AND GP
baseURL_playerstat_trad ='https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# SHOT DISTANCE PARAMS.
parameters_playerstat_shotdist = {
            
            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
	    'DistanceRange': '5ft Range',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
            'GameSegment': '',
            'Height': '',
            'LastNGames': 0,
            'LeagueID': '00',
            'Location': '',
            'MeasureType': 'Base',
            'Month': 0,
            'OpponentTeamID': 0,
            'Outcome': '',
            'PORound': 0,
            'PaceAdjust': '',
            'PerMode': 'PerGame',
	    'Period': 0,
            'PlayerExperience': '',
            'PlayerPosition': '',
            'PlusMinus': 'N',
            'Rank': 'N', 
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'ShotCLockRange': '',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}

#TRADITIONAL PARAMS
parameters_playerstat_trad = {
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
            'MeasureType': 'Base',
            'Month': 0,
            'OpponentTeamID': 0,
            'Outcome': '',
            'PORound': 0,
            'PaceAdjust': 'N',
            'PerMode': 'PerGame',
            'Period': 0,
            'PlayerExperience': '',
            'PlayerPosition': '',
            'PlusMinus': 'N',
            'Rank': 'N',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'ShotClockRange': '',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
        }

# Scraper for NBA Shooting.
def scrapeSHOTURL(baseURL, parameters):
    response = requests.get(baseURL, params=parameters, headers=user_agent_headers)
    response.raise_for_status()
    headers = response.json()['resultSets']['headers'][1]['columnNames']
    stats = response.json()['resultSets']['rowSet']
    stats_df = pd.DataFrame(stats, columns=headers)
    stats_df['Season'] = parameters['Season']
    #stats_df.drop(['CFID', 'CFPARAMS'], axis=1, inplace=True)
    return stats_df

# Scraper for rest of NBA stats
def scrapeURL(baseURL, parameters):
    response = requests.get(baseURL, params=parameters, headers=user_agent_headers)
    response.raise_for_status()
    headers = response.json()['resultSets'][0]['headers']
    stats = response.json()['resultSets'][0]['rowSet']
    stats_df = pd.DataFrame(stats, columns=headers)
    stats_df['Season'] = parameters['Season']
    #stats_df.drop(['CFID', 'CFPARAMS'], axis=1, inplace=True)
    return stats_df

#LETS SCRAPE!

df_shot5ft = scrapeSHOTURL(baseURL_playerstat_shotdist, parameters_playerstat_shotdist)
time.sleep(5)
df_trad = scrapeURL(baseURL_playerstat_trad, parameters_playerstat_trad)

#EDIT SHOT5FT 
df_shot5ft = df_shot5ft.drop(['FG_PCT','TEAM_ID','TEAM_ABBREVIATION','AGE','Season'],1)
df_shot5ft.columns = ['PLAYER_ID', 'PLAYER_NAME', 'FGM_LT5', 'FGA_LT5','FGM_5TO10','FGA_5TO10','FGM_10TO15','FGA_10TO15','FGM_15TO20','FGA_15TO20','FGM_20TO25', 'FGA_20TO25','FGM_25+', 'FGA_25+','STOP1','STOP2','STOP3','STOP4','STOP5','STOP6']
df_shot5ft['FGM_25+']= df_shot5ft['FGM_25+']+df_shot5ft['STOP1']+df_shot5ft['STOP3']+df_shot5ft['STOP5']
df_shot5ft['FGA_25+']= df_shot5ft['FGA_25+']+df_shot5ft['STOP2']+df_shot5ft['STOP4']+df_shot5ft['STOP6']
#df_shot5ft['FGM_LT10']= df_shot5ft['FGM_LT5']+df_shot5ft['FGM_5TO10']
#df_shot5ft['FGA_LT10']= df_shot5ft['FGA_LT5']+df_shot5ft['FGA_5TO10']
df_shot5ft = df_shot5ft.drop(['STOP1','STOP2','STOP3','STOP4','STOP5','STOP6'],1)
df_shot5ft = df_shot5ft.set_index(['PLAYER_ID','PLAYER_NAME'])

#EDIT TRADITIONAL
df_trad = df_trad[['PLAYER_ID','PLAYER_NAME','GP','FG3M','FG3A']] 
df_trad = df_trad.set_index(['PLAYER_ID','PLAYER_NAME'])

#JOIN DATAFRAMES
df_off = df_shot5ft.join(df_trad)
df_off = df_off[df_off['GP']>=40]
df_off = df_off.drop(['GP'],1)

#Lets get columns we want
df_off['FGM_15to3PT'] = ((df_off['FGM_20TO25']+df_off['FGM_25+'])-df_off['FG3M'])+df_off['FGM_15TO20']
df_off['FGA_15to3PT'] = ((df_off['FGA_20TO25']+df_off['FGA_25+'])-df_off['FG3A'])+df_off['FGA_15TO20']
#df_off['FGPCT_15to3PT'] = df_off['FGM_15to3PT']/df_off['FGA_15to3PT']

#df_off['FGPCT_LT5'] = df_off['FGM_LT5']/df_off['FGA_LT5']
#df_off['FGPCT_5TO10'] = df_off['FGM_5TO10']/df_off['FGA_5TO10']
#df_off['FGPCT_10TO15'] = df_off['FGM_10TO15']/df_off['FGA_10TO15']

#WE CAN GET EPV'S
df_off['LT5_OffEPV'] = (df_off['FGM_LT5']*2)
df_off['5to10_OffEPV'] = (df_off['FGM_5TO10']*2)
df_off['10to15_OffEPV'] = (df_off['FGM_10TO15']*2)
df_off['15to3PT_OffEPV'] = (df_off['FGM_15to3PT']*2)
df_off['3PT_OffEPV'] = (df_off['FG3M']*3)

#df_off['LT5_OffEPV'] = df_off['FGPCT_LT5']*2
#df_off['5to10_OffEPV'] = df_off['FGPCT_5TO10']*2
#df_off['10to15_OffEPV'] = df_off['FGPCT_10TO15']*2
#df_off['15to3PT_OffEPV'] = df_off['FGPCT_15to3PT']*2
#df_off['3PT_OffEPV'] = df_off['FG3_PCT']*3

#df_off.fillna(value=0, inplace=True)

df_off = df_off[['FGA_LT5','FGA_5TO10','FGA_10TO15','FGA_15to3PT','FG3A','LT5_OffEPV','5to10_OffEPV','10to15_OffEPV','15to3PT_OffEPV','3PT_OffEPV']]

#DROP Players
df_off=df_off.drop(df_off.index[261])
df_off=df_off.drop(df_off.index[55])
df_off=df_off.drop(df_off.index[84])
df_off=df_off.drop(df_off.index[132])
df_off=df_off.drop(df_off.index[157])
df_off=df_off.drop(df_off.index[168])
df_off=df_off.drop(df_off.index[275])
df_off=df_off.drop(df_off.index[256])



