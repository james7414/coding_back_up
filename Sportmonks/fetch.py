'''Fetch script used to grab Sportmonks data'''

from sportmonks_utility import (
    read_json
)


def fetch_fixtures_data(league_ids_list, years_list, fixture_data='events'):
    '''Function used to grab fixture json data for specified leagues. Fixture data can be events or odds '''
    if fixture_data not in ['events', 'odds']:
        raise FileNotFoundError ("Invalid file type.")
    
    season_data_dict = {}
    for league_id in league_ids_list:
        for year in years_list:
            year_format = year.replace('/','_')
            season_name = str(league_id) + '_' + year_format
            season = str(league_id) + '_' + year_format
            event_data = read_json(f'sportmonks_data/fixtures_w_{fixture_data}_{league_id}_{year_format}.json')
            season_data_dict[season_name] = event_data
    return season_data_dict