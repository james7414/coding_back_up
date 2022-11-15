'''Clean script used to clean Sportmonks data'''

def clean_fixture_data(fixture_json):
    '''Function used to clean fixture data into format required'''
    clean_fixture_dict={}
    clean_fixture_dict['fixture_id'] = fixture_json['id']
    clean_fixture_dict['league_id'] = fixture_json['league_id']
    clean_fixture_dict['season_id'] = fixture_json['season_id']
    clean_fixture_dict['home_id'] = fixture_json['localteam_id']
    clean_fixture_dict['away_id'] = fixture_json['visitorteam_id']
    clean_fixture_dict['home_score'] = fixture_json['scores']['localteam_score']
    clean_fixture_dict['away_score'] = fixture_json['scores']['visitorteam_score']
    clean_fixture_dict['ht_score'] = fixture_json['scores']['ht_score']
    clean_fixture_dict['date_time'] = fixture_json['time']['starting_at']['date_time']
    clean_fixture_dict['home_name'] = fixture_json['localTeam']['name']
    clean_fixture_dict['away_name'] = fixture_json['visitorTeam']['name']
    return clean_fixture_dict