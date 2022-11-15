#fetch fixtures data#

clean_fixtures_list = []
for league_id in TOP_FIVE_LEAGUE_IDS:
    for year in YEARS_OF_INTEREST:
        year_format = year.replace('/','_')
        season = str(league_id) + '_' + year_format
        season_event_data = read_json(
            f'sportmonks_data/fixtures_w_events_{league_id}_{year_format}.json'
        )
        for fixture_json in season_event_data:
            clean_fixture_dict = clean_fixture_data(fixture_json)
            clean_fixture_dict['season_name'] = year_format
            clean_fixtures_list.append(clean_fixture_dict)
            
# for lineup and bench            
import time
startTime = time.time()

lineup_bench_data_list = []

for _, season_event_data  in season_fixtures_data_dict.items():
    for fixture_json in season_event_data:
        # lineup df
        lineup_df = pd.json_normalize(fixture_json['lineup'])
        lineup_df['starting'] = True

        # bench df
        bench_df = pd.json_normalize(fixture_json['bench'])
        bench_df['starting'] = False

        # append
        lineup_bench_data_list.append(lineup_df)
        lineup_bench_data_list.append(bench_df)
    print(f'_: done')
executionTime = (time.time() - startTime)
print(executionTime)
            
# Goals, cards, subs, corners data, different method to get dataframe.#

# for _, season_event_data  in season_fixtures_data_dict.items():

import time
startTime = time.time()

season_event_data = season_fixtures_data_dict['8_2021_2022']
all_event_list = []
for fixture_json in season_event_data:
    events_df = pd.DataFrame(fixture_json['events'])
    
    corners_df = pd.DataFrame(fixture_json['corners'])
    corners_df['type'] = 'corner'
    
    all_events_df = pd.concat([events_df, corners_df])
    all_event_list.append(all_events_df)
all_event_df1 = pd.concat(all_event_list).reset_index(drop=True)

executionTime = (time.time() - startTime)
print(executionTime)