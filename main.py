import json
import os
import time
import pandas
from itertools import chain

start_time = time.time()


# Store all file locations and collate it to iterate the locations one by one
file_loc_1 = r"my_spotify_data\Spotify Extended Streaming History\Streaming_History_Audio_2019-2020_0.json"
file_loc_2 = r"my_spotify_data\Spotify Extended Streaming History\Streaming_History_Audio_2020-2021_1.json"
file_loc_3 = r"my_spotify_data\Spotify Extended Streaming History\Streaming_History_Audio_2021-2022_2.json"
file_loc_4 = r"my_spotify_data\Spotify Extended Streaming History\Streaming_History_Audio_2022-2023_3.json"
file_loc_5 = r"my_spotify_data\Spotify Extended Streaming History\Streaming_History_Audio_2023_4.json"
file_loc_6 = r"my_spotify_data\Spotify Extended Streaming History\Streaming_History_Audio_2023-2024_5.json"
file_loc_7 = r"my_spotify_data\Spotify Extended Streaming History\Streaming_History_Audio_2024_6.json"

all_file_locs = list((file_loc_1, file_loc_2, file_loc_3, file_loc_4, file_loc_5, file_loc_6, file_loc_7))

# Go through all the files and store all the data in var 'all_lines'
all_lines = list()

for each_file in all_file_locs:
    # Check if the file exists
    if not os.path.exists(each_file):
        print(f"File not found: {each_file}")
        exit()
    with open(each_file, 'r', encoding='utf-8') as open_file:
        all_lines.append(json.load(open_file))
        # print(f'{each_file} done')

# Use from_iterable to de-list the nested list, effectively making the multiple lists (i.e., each file) into one
all_lines = list(chain.from_iterable(all_lines))

# Use Pandas, Profit???
all_lines_df = pandas.DataFrame(list(all_lines))
all_lines_df.columns = ['DateTime', 'Platform', 'Time Played(ms)',
                        'Country', 'IP_Addr', 'Track Name',
                        'Artist', 'Album', 'URL',
                        'episode_name', 'show_name', 'episode_uri',
                        'reason_start',
                        'reason_end', 'shuffle', 'skipped',
                        'offline', 'Offline_timestamp', 'Incognito Mode']
all_lines_df.index = range(1, len(all_lines_df) + 1)

# Convert 'ts' to DateTime format to filter and search later on
all_lines_df['DateTime'] = pandas.to_datetime(all_lines_df['DateTime'], utc=True)
# Convert to Indian Standard Time (IST)
all_lines_df['DateTime'] = all_lines_df['DateTime'].dt.tz_convert('Asia/Kolkata')
# Check the data type of 'DateTime' and Verify the conversion, Preview the first & last few converted datetime entries
''' print(all_lines_df.info())  
print(f"{all_lines_df['DateTime'].head()}\n{all_lines_df.tail()}")  '''

# print(len(all_lines_df))
# print(all_lines_df.columns)
# print(all_lines_df)

# all_lines_df.to_csv('temp_file4.csv')


def sum_heard_music(all_lines_df):
    unfiltered_sum_listened = sum(all_lines_df['Time Played(ms)'])
    print(
        f'Entire SUM of music/podcasts played: \n\t {unfiltered_sum_listened} ms, i.e.,\n\t {unfiltered_sum_listened / 1000} secs,'
        f' or\n\t {unfiltered_sum_listened / 60000} minutes, or\n\t {unfiltered_sum_listened / 3600000} hours '
        f'or\n\t {unfiltered_sum_listened / 86400000} days')


sum_heard_music(all_lines_df)

print(f'Done in {time.time() - start_time}')
exit()  # TEMP

print(json.dumps(list(all_lines), indent=2))
print(f'Done in {time.time() - start_time} seconds')
