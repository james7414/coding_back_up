from datetime import datetime
import pandas as pd
from sportmonks.soccer import SoccerApiV2
from sportmonks_config import SPORTMONKS_TOKEN

soccer = SoccerApiV2(api_token= SPORTMONKS_TOKEN)

class Sportmonks:
    '''SPortmonks class used to fetch data from API'''
    def __init__(self, soccer = SoccerApiV2(api_token= SPORTMONKS_TOKEN)):
        self.soccer =  soccer
        
    def get_countries(self):
        '''Function used to grab countries from Sportmonks API'''
        countries_json = soccer.countries()
        countries_df = pd.json_normalize(countries_json)
        return countries_df
        
    def get_leagues(self):
        '''Function used to grab leagues from Sportmonks API'''
        leagues_json = soccer.leagues()
        leagues_df = pd.json_normalize(leagues_json)
        return leagues_df
    
    def get_seasons(self):
        '''Function used to grab seasons from Sportmonks API'''
        seasons_json = soccer.seasons(includes=['stages','rounds'])
        return seasons_json
    
    def get_season_start_end_date(self, season_id, seasons_json=None):
        '''Function used to grab season start and end date from Sportmonks API'''
        # grab data is not given as argument
        if seasons_json is None:
            seasons_json = self.get_seasons()
        
        # grab data for season id of interest
        season_json = [season for season in seasons_json if season['id']== season_id][0]
        
        # grab season start and end date
        season_start_date = season_json['rounds'][0]['start']
        season_last_available_date = season_json['rounds'][-1]['end']
        now = datetime.now().strftime("%Y-%m-%d")
        if season_last_available_date > now:
            season_end_date = np.nan
        else: 
            season_end_date = season_last_available_date
            
        return season_start_date, season_end_date
    
    def get_season_league_id(self, season_id, seasons_json=None):
        '''Function used to grab season league id from Sportmonks API'''
        if seasons_json is None:
            seasons_json = self.get_seasons()
            
        # grab data for season id of interest
        season_json = [season for season in seasons_json if season['id']== season_id][0]
        season_league_id = season_json['league_id']
            
        return season_league_id
    
    def get_season_fixtures(self, season_id, includes_list = None ,seasons_json=None):
        '''Function used to grab fixtures in Sportmonks API'''
        # Get season start date and end date
        season_start_date, season_end_date = self.get_season_start_end_date(
            season_id = season_id, 
            seasons_json = seasons_json
        )
        # get season league id
        season_league_id = self.get_season_league_id(
            season_id = season_id, 
            seasons_json=seasons_json
        )
        
        # get season fixtures json
        fixtures_json = soccer.fixtures(
            start_date = season_start_date,
            end_date = season_end_date,
            league_ids = season_league_id,
            includes = includes_list

        )
        return fixtures_json
    
    def get_markets(self):
        '''Function used to grab markets in Sportmonks API'''
        markets_json = soccer.markets()
        markets_df = pd.DataFrame(markets_json)
        return markets_df
    
    def get_bookmakers(self):
        '''Function used to grab bookmakers from Sportmonks API'''
        bookmakers_json = soccer.bookmakers()
        bookmakers_df = pd.DataFrame(bookmakers_json)
        return bookmakers_df