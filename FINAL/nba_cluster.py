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

# URL FOR DRIM.
baseURL_playerstat_drim ='http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Defense&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

### URL FOR PASS.
baseURL_playerstat_pass ='https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Passing&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL FOR TOUCHES
baseURL_playerstat_touches ='http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Possessions&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL FOR REBOUND
baseURL_playerstat_reb ='http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Rebounding&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

# URL FOR DRIVES
baseURL_playerstat_drives = 'http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Drives&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

#URL FOR CNS
baseURL_playerstat_cns ='http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=CatchShoot&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

#URL FOR BIO
baseURL_playerstat_bio ='https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='

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


# DRIM PARAM.
parameters_playerstat_drim = {
            
            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
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
            'PlayerOrTeam': 'Player',
            'PlayerPosition': '',
            'PtMeasureType': 'Possessions',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
        }
#PASS PARAM
parameters_playerstat_pass = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
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
            'PlayerOrTeam': 'Player',
            'PlayerPosition': '',
            'PtMeasureType': 'Passing',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
# PARAM TOUCHES
parameters_playerstat_touches = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
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
            'PlayerOrTeam': 'Player',
            'PlayerPosition': '',
            'PtMeasureType': 'Possessions',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
# PARAM REB
parameters_playerstat_reb = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
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
            'PlayerOrTeam': 'Player',
            'PlayerPosition': '',
            'PtMeasureType': 'Rebounding',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
#PARAM DRIVES
parameters_playerstat_drives = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
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
            'PlayerOrTeam': 'Player',
            'PlayerPosition': '',
            'PtMeasureType': 'Drives',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
# CNS PARAM
parameters_playerstat_cns = {

            'College': '',
            'Conference': '',
            'Country': '',
            'DateFrom': '',
            'DateTo': '',
            'Division': '',
            'DraftPick': '',
            'DraftYear': '',
            'GameScope': '',
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
            'PlayerOrTeam': 'Player',
            'PlayerPosition': '',
            'PtMeasureType': 'CatchShoot',
            'Season': '2016-17',
            'SeasonSegment': '',
            'SeasonType': 'Regular Season',
            'StarterBench': '',
            'TeamID': 0,
            'VsConference': '',
            'VsDivision': '',
            'Weight': '',
}
# BIO PARAM
parameters_playerstat_bio = {

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

#LETS SCRAPE
df_drim = scrapeURL(baseURL_playerstat_drim, parameters_playerstat_drim)
df_drim = df_drim[df_drim['GP']>=40]
df_drim['D_RIM_FGA'] = df_drim['DEF_RIM_FGA']/df_drim['MIN']
df_drim.head() # D A T A
df_drim = df_drim.drop(['DREB','DEF_RIM_FGA','TEAM_ID','TEAM_ABBREVIATION','GP','W','L','MIN','STL','BLK','DEF_RIM_FGM','DEF_RIM_FG_PCT','Season'], 1)

time.sleep(5)

df_pass = scrapeURL(baseURL_playerstat_pass, parameters_playerstat_pass)
df_pass = df_pass[df_pass['GP']>=40]
df_pass['PASSES_MADE'] = df_pass['PASSES_MADE']/df_pass['MIN']
df_pass['AST'] = df_pass['AST']/df_pass['MIN']
df_pass['POTENTIAL_AST'] = df_pass['POTENTIAL_AST']/df_pass['MIN']
df_pass.head() # D A T A
df_pass = df_pass.drop(['TEAM_ID','TEAM_ABBREVIATION','GP','W','L','MIN','PASSES_RECEIVED','FT_AST','SECONDARY_AST','AST_POINTS_CREATED','AST_ADJ','AST_TO_PASS_PCT','AST_TO_PASS_PCT_ADJ','Season'],1)

time.sleep(5)

df_touch = scrapeURL(baseURL_playerstat_touches, parameters_playerstat_touches)
df_touch = df_touch[df_touch['GP']>=40]
df_touch['FRONT_CT_TOUCHES'] = df_touch['FRONT_CT_TOUCHES']/df_touch['MIN']
df_touch['ELBOW_TOUCHES'] = df_touch['ELBOW_TOUCHES']/df_touch['MIN']
df_touch['POST_TOUCHES'] = df_touch['POST_TOUCHES']/df_touch['MIN']
df_touch['PAINT_TOUCHES'] = df_touch['PAINT_TOUCHES']/df_touch['MIN']
df_touch.head() # D A T A
df_touch = df_touch.drop(['TIME_OF_POSS','AVG_DRIB_PER_TOUCH','AVG_SEC_PER_TOUCH','TEAM_ID','TEAM_ABBREVIATION','GP','W','L','MIN','POINTS','TOUCHES','PTS_PER_TOUCH','PTS_PER_ELBOW_TOUCH','PTS_PER_POST_TOUCH','PTS_PER_PAINT_TOUCH','Season'],1)

time.sleep(5)

df_reb = scrapeURL(baseURL_playerstat_reb, parameters_playerstat_reb)
df_reb = df_reb[df_reb['GP']>=40]
df_reb['REB_CHANCES'] = df_reb['REB_CHANCES']/df_reb['MIN']
#df.head() # D A T A
df_reb = df_reb.drop(['MIN','TEAM_ID', 'TEAM_ABBREVIATION','GP','W','L','OREB','OREB_CONTEST','OREB_UNCONTEST','OREB_CONTEST_PCT','OREB_CHANCES','OREB_CHANCE_PCT','OREB_CHANCE_DEFER','OREB_CHANCE_PCT_ADJ','AVG_OREB_DIST','DREB','DREB_CONTEST','DREB_CONTEST','DREB_UNCONTEST','DREB_CONTEST_PCT','DREB_CHANCES','DREB_CHANCE_PCT','DREB_CHANCE_DEFER','DREB_CHANCE_PCT_ADJ','AVG_DREB_DIST','REB','REB_CONTEST','REB_UNCONTEST','REB_CONTEST_PCT','REB_CHANCE_PCT','REB_CHANCE_DEFER','REB_CHANCE_PCT_ADJ','AVG_REB_DIST','Season'], 1)

time.sleep(5)

df_drive = scrapeURL(baseURL_playerstat_drives, parameters_playerstat_drives)
df_drive = df_drive[df_drive['GP']>=40]
df_drive['DRIVE'] = df_drive['DRIVES']/df_drive['MIN']
df_drive['DRIVES_FGA'] = df_drive['DRIVE_FGA']/df_drive['MIN']
df_drive['DRIVES_PASS'] = df_drive['DRIVE_PASSES']/df_drive['MIN']
#df.head() # D A T A
df_drive = df_drive.drop(['TEAM_ID','TEAM_ABBREVIATION','GP','W','L','DRIVES','DRIVE_FGA','DRIVE_PASSES','MIN','DRIVE_FGM','DRIVE_FG_PCT','DRIVE_FTM','DRIVE_FTA','DRIVE_FT_PCT','DRIVE_PTS','DRIVE_PTS_PCT','DRIVE_PASSES_PCT','DRIVE_AST','DRIVE_AST_PCT','DRIVE_TOV','DRIVE_TOV_PCT','DRIVE_PF','DRIVE_PF_PCT','Season'],1)

time.sleep(5)

df_cns = scrapeURL(baseURL_playerstat_cns, parameters_playerstat_cns)
df_cns = df_cns[df_cns['GP']>=40]
df_cns['CNS_FGA'] = df_cns['CATCH_SHOOT_FGA']/df_cns['MIN']
df_cns['CNS_FG3A'] = df_cns['CATCH_SHOOT_FG3A']/df_cns['MIN']
#df.head() # D A T A
df_cns = df_cns.drop(['TEAM_ID','TEAM_ABBREVIATION','GP','W','L','MIN','CATCH_SHOOT_FGA','CATCH_SHOOT_FG3A','CATCH_SHOOT_FGM','CATCH_SHOOT_FG_PCT','CATCH_SHOOT_PTS','CATCH_SHOOT_FG3M','CATCH_SHOOT_FG3_PCT','CATCH_SHOOT_EFG_PCT','Season'],1)

time.sleep(5)

df_bio = scrapeURL(baseURL_playerstat_bio, parameters_playerstat_bio)
#df_bio.head() # D A T A
df_bio = df_bio[df_bio['GP']>=40]
df_bio = df_bio.drop(['TEAM_ID','TEAM_ABBREVIATION','AGE','PLAYER_HEIGHT','PLAYER_HEIGHT','PLAYER_WEIGHT','COLLEGE','COUNTRY','DRAFT_YEAR','DRAFT_ROUND','DRAFT_NUMBER','GP','PTS','REB','AST','NET_RATING','OREB_PCT','DREB_PCT','USG_PCT','TS_PCT','AST_PCT','Season'],1)

time.sleep(5)

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
df_trad = df_trad[['PLAYER_ID','PLAYER_NAME','GP','MIN','FG3M','FG3A','FG3_PCT']]
df_trad = df_trad.set_index(['PLAYER_ID','PLAYER_NAME'])

#JOIN DATAFRAMES
df_att = df_shot5ft.join(df_trad)
df_att = df_att[df_att['GP']>=40]
df_att = df_att.drop(['FGM_LT5','FGM_5TO10','FGM_10TO15','FGM_15TO20','FGM_20TO25','FGM_25+'],1)

#Lets get columns we want
#df_off['FGM_15to3PT'] = ((df_off['FGM_20TO25']+df_off['FGM_25+'])-df_off['FG3M'])+df_off['FGM_15TO20']
#df_off['FGA_15to3PT'] = ((df_off['FGA_20TO25']+df_off['FGA_25+'])-df_off['FG3A'])+df_off['FGA_15TO20']
#df_off['FGPCT_15to3PT'] = df_off['FGM_15to3PT']/df_off['FGA_15to3PT']

#df_off['FGPCT_LT5'] = df_off['FGM_LT5']/df_off['FGA_LT5']
#df_off['FGPCT_5TO10'] = df_off['FGM_5TO10']/df_off['FGA_5TO10']
#df_off['FGPCT_10TO15'] = df_off['FGM_10TO15']/df_off['FGA_10TO15']

df_att['FGA_LT5']= df_att['FGA_LT5']/df_att['MIN']
df_att['FGA_5TO10']= df_att['FGA_5TO10']/df_att['MIN']
df_att['FGA_10TO15']= df_att['FGA_10TO15']/df_att['MIN']
df_att['FGA_15TO20']= df_att['FGA_15TO20']/df_att['MIN']
df_att['FGA_20TO25']= df_att['FGA_20TO25']/df_att['MIN']
df_att['FGA_25+']= df_att['FGA_25+']/df_att['MIN']
df_att = df_att.drop(['GP','MIN'],1)

#NOW MERGE
df=df_pass.set_index(['PLAYER_ID','PLAYER_NAME']).join(df_drive.set_index(['PLAYER_ID','PLAYER_NAME']))
df=df.join(df_touch.set_index(['PLAYER_ID','PLAYER_NAME']))
df=df.join(df_drim.set_index(['PLAYER_ID','PLAYER_NAME']))
df=df.join(df_bio.set_index(['PLAYER_ID','PLAYER_NAME']))
df=df.join(df_reb.set_index(['PLAYER_ID','PLAYER_NAME']))
df=df.join(df_cns.set_index(['PLAYER_ID','PLAYER_NAME']))
df=df.join(df_att)

df_off=df_off.drop(df_off.index[262])
df_off=df_off.drop(df_off.index[55])
df_off=df_off.drop(df_off.index[85])
df_off=df_off.drop(df_off.index[134])
df_off=df_off.drop(df_off.index[160])
df_off=df_off.drop(df_off.index[172])
df_off=df_off.drop(df_off.index[280])
df_off=df_off.drop(df_off.index[261])

#SET MATRIX and CLUSTERS
mat = df.as_matrix()
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3)
km.fit(mat)
labels = km.labels_
df.assign(Position = labels)
df['Position'] = labels


df = df[['Position']]


