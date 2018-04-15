import requests
import pandas as pd
import os
import time

user_agent_headers = {'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

# URL FOR DEFENDING SHOTS GT 15FT.
baseURL_playerstat_GT15 ='https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Greater+Than+15Ft&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL FOR DEFENDING SHOTS LT 10FT.
baseURL_playerstat_LT10 ='https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Less+Than+10Ft&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL FOR DEFENDING SHOTS LT 6FT.
baseURL_playerstat_LT6 ='https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Less+Than+6Ft&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL FOR DEFENDING 3PT.
baseURL_playerstat_3PT ='https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=3+Pointers&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL FOR DEFENDING 2PT.
baseURL_playerstat_2PT ='https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=2+Pointers&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# DEFENDING SHOTS GREATER THAN 15FT PARAM.
parameters_playerstat_GT15 = {
            
            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
	    'DefenseCategory': 'Greater Than 15Ft',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
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
	    'Period': 0,
            'PlayerExperience': '',
            'PlayerID': '',
            'PlayerPosition': '', 
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
        }
# DEFENDING SHOTS LT 10FT PARAM.
parameters_playerstat_LT10 = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'DefenseCategory': 'Less Than 10Ft',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
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
            'Period': 0,
            'PlayerExperience': '',
            'PlayerID': '',
            'PlayerPosition': '',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
# DEFENDING SHOTS LT 6FT PARAM.
parameters_playerstat_LT6 = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'DefenseCategory': 'Less Than 6Ft',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
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
            'Period': 0,
            'PlayerExperience': '',
            'PlayerID': '',
            'PlayerPosition': '',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
# DEFENDING 3PT SHOTS PARAM.
parameters_playerstat_3PT = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'DefenseCategory': '3 Pointers',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
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
            'Period': 0,
            'PlayerExperience': '',
            'PlayerID': '',
            'PlayerPosition': '',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
# DEFENDING 2PT PARAMS.
parameters_playerstat_2PT = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'DefenseCategory': '2 Pointers',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
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
            'Period': 0,
            'PlayerExperience': '',
            'PlayerID': '',
            'PlayerPosition': '',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}

# SCRAPE FUNCTION.
def scrapeURL(baseURL, parameters):
    response = requests.get(baseURL, params=parameters, headers=user_agent_headers)
    response.raise_for_status()
    headers = response.json()['resultSets'][0]['headers']
    stats = response.json()['resultSets'][0]['rowSet']
    stats_df = pd.DataFrame(stats, columns=headers)
    stats_df['Season'] = parameters['Season']
    #stats_df.drop(['CFID', 'CFPARAMS'], axis=1, inplace=True)
    return stats_df

#LETS START SCRAPING
df_def15gt = scrapeURL(baseURL_playerstat_GT15, parameters_playerstat_GT15)
df_def15gt = df_def15gt[df_def15gt['GP']>39]
df_def15gt = df_def15gt.rename(columns={'CLOSE_DEF_PERSON_ID': 'PLAYER_ID'})
df_def15gt = df_def15gt.set_index(['PLAYER_ID','PLAYER_NAME'])
time.sleep(5)
df_def10lt = scrapeURL(baseURL_playerstat_LT10, parameters_playerstat_LT10)
df_def10lt = df_def10lt[df_def10lt['GP']>39]
df_def10lt = df_def10lt.rename(columns={'CLOSE_DEF_PERSON_ID': 'PLAYER_ID'})
df_def10lt = df_def10lt.set_index(['PLAYER_ID','PLAYER_NAME'])
time.sleep(5)
df_def6lt = scrapeURL(baseURL_playerstat_LT6, parameters_playerstat_LT6)
df_def6lt = df_def6lt[df_def6lt['GP']>39]
df_def6lt = df_def6lt.rename(columns={'CLOSE_DEF_PERSON_ID': 'PLAYER_ID'})
df_def6lt = df_def6lt.set_index(['PLAYER_ID','PLAYER_NAME'])
time.sleep(5)
df_def3pt = scrapeURL(baseURL_playerstat_3PT, parameters_playerstat_3PT)
df_def3pt = df_def3pt[df_def3pt['GP']>39]
df_def3pt = df_def3pt.rename(columns={'CLOSE_DEF_PERSON_ID': 'PLAYER_ID'})
df_def3pt = df_def3pt.set_index(['PLAYER_ID','PLAYER_NAME'])
time.sleep(5)
df_def2pt = scrapeURL(baseURL_playerstat_2PT, parameters_playerstat_2PT)
df_def2pt = df_def2pt[df_def2pt['GP']>39]
df_def2pt = df_def2pt.rename(columns={'CLOSE_DEF_PERSON_ID': 'PLAYER_ID'})
df_def2pt = df_def2pt.set_index(['PLAYER_ID','PLAYER_NAME'])

#EDIT LT10
df_def10lt = df_def10lt.drop(['PLAYER_LAST_TEAM_ID','PLAYER_LAST_TEAM_ABBREVIATION','GP','AGE','G','FREQ','NS_LT_10_PCT','PLAYER_POSITION','PLUSMINUS','Season'],1)
#EDIT GT15 
df_def15gt = df_def15gt.drop(['PLAYER_LAST_TEAM_ID','PLAYER_LAST_TEAM_ABBREVIATION','GP','AGE','G','FREQ','NS_GT_15_PCT','PLAYER_POSITION','PLUSMINUS','Season'],1)
#EDIT LT6
df_def6lt = df_def6lt.drop(['PLAYER_LAST_TEAM_ID','PLAYER_LAST_TEAM_ABBREVIATION','GP','AGE','G','FREQ','NS_LT_06_PCT','PLAYER_POSITION','PLUSMINUS','Season'],1)
#EDIT 3PT
df_def3pt = df_def3pt.drop(['PLAYER_LAST_TEAM_ID','PLAYER_LAST_TEAM_ABBREVIATION','GP','AGE','G','FREQ','NS_FG3_PCT','PLAYER_POSITION','PLUSMINUS','Season'],1)
#EDIT 2PT
df_def2pt = df_def2pt.drop(['PLAYER_LAST_TEAM_ID','PLAYER_LAST_TEAM_ABBREVIATION','GP','AGE','G','FREQ','NS_FG2_PCT','PLAYER_POSITION','PLUSMINUS','Season'],1)


#JOIN DATAFRAMES
df_def=df_def3pt.join(df_def15gt).join(df_def10lt).join(df_def6lt).join(df_def2pt)

#Now let's get columns we want:
#15-3Pt
df_def['FGM_15_to_3PT']=df_def['FGM_GT_15']-df_def['FG3M']
df_def['FGA_15_to_3PT']=df_def['FGA_GT_15']-df_def['FG3A']
#df_def['FG_15_to_3PT_PCT']=df_def['FGM_15_to_3PT']/df_def['FGA_15_to_3PT']

#6-10
df_def['FGM_6_to_10']=df_def['FGM_LT_10']-df_def['FGM_LT_06']
df_def['FGA_6_to_10']=df_def['FGA_LT_10']-df_def['FGA_LT_06']
#df_def['FG_6_to_10_PCT']=df_def['FGM_6_to_10']/df_def['FGA_6_to_10']

#10-15
df_def['FGM_10_to_15']=(df_def['FG2M']-df_def['FGM_LT_10'])-df_def['FGM_15_to_3PT']
df_def['FGA_10_to_15']=(df_def['FG2A']-df_def['FGA_LT_10'])-df_def['FGA_15_to_3PT']
#df_def['FG_10_to_15_PCT']=df_def['FGM_10_to_15']/df_def['FGA_10_to_15']


#And now we get EPV!!
df_def['FG_LT_06_DefEPV']=(df_def['FGM_LT_06']*2)-(df_def['FGA_LT_06']*2)
df_def['FG_6_to_10_DefEPV']=(df_def['FGM_6_to_10']*2)-(df_def['FGA_6_to_10']*2)
df_def['FG_10_to_15_DefEPV']=(df_def['FGM_10_to_15']*2)-(df_def['FGA_10_to_15']*2)
df_def['FG_15_to_3PT_DefEPV']=(df_def['FGM_15_to_3PT']*2)-(df_def['FGA_15_to_3PT']*2)
df_def['FG3_DefEPV']=(df_def['FG3M']*3)-(df_def['FG3A']*3)

#df_def['FG_LT_06_DefEPV']=df_def['LT_06_PCT']*2
#df_def['FG_6_to_10_DefEPV']=df_def['FG_6_to_10_PCT']*2
#df_def['FG_10_to_15_DefEPV']=df_def['FG_10_to_15_PCT']*2
#df_def['FG_15_to_3PT_DefEPV']=df_def['FG_15_to_3PT_PCT']*2
#df_def['FG3_DefEPV']=df_def['FG3_PCT']*3

#We get Frequency
df_def['DFGA_LT06']=df_def['FGA_LT_06']/(df_def['FGA_LT_06']+df_def['FGA_6_to_10']+df_def['FGA_10_to_15']+df_def['FGA_15_to_3PT']+df_def['FG3A'])

df_def['DFGA_6to10']=df_def['FGA_6_to_10']/(df_def['FGA_LT_06']+df_def['FGA_6_to_10']+df_def['FGA_10_to_15']+df_def['FGA_15_to_3PT']+df_def['FG3A'])

df_def['DFGA_10to15']=df_def['FGA_10_to_15']/(df_def['FGA_LT_06']+df_def['FGA_6_to_10']+df_def['FGA_10_to_15']+df_def['FGA_15_to_3PT']+df_def['FG3A'])

df_def['DFGA_15to3PT']=df_def['FGA_15_to_3PT']/(df_def['FGA_LT_06']+df_def['FGA_6_to_10']+df_def['FGA_10_to_15']+df_def['FGA_15_to_3PT']+df_def['FG3A'])

df_def['DFGA_3PT']=df_def['FG3A']/(df_def['FGA_LT_06']+df_def['FGA_6_to_10']+df_def['FGA_10_to_15']+df_def['FGA_15_to_3PT']+df_def['FG3A'])

#Then we can Drop the Rest!
df_def = df_def[['DFGA_LT06','DFGA_6to10','DFGA_10to15','DFGA_15to3PT','DFGA_3PT','FG_LT_06_DefEPV','FG_6_to_10_DefEPV','FG_10_to_15_DefEPV','FG_15_to_3PT_DefEPV','FG3_DefEPV']]


