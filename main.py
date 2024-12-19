import json
import os
import time
import pandas
from itertools import chain
from datetime import datetime

start_time = time.time()


def first_song(df):
    song = df.head(1)
    print(
        f"{song["Track Name"].iloc[0]} by {song["Artist"].iloc[0]} on {song["DateTime"].iloc[0].strftime("%d %b %Y at %I:%M %p %Z")}")


def sum_heard_music(all_lines_df):
    unfiltered_sum_listened = sum(all_lines_df['Time Played(ms)'])
    print(
        f'Entire SUM of music/podcasts played: \n\t {unfiltered_sum_listened} ms, i.e.,\n\t {unfiltered_sum_listened / 1000} secs,'
        f' or\n\t {unfiltered_sum_listened / 60000} minutes, or\n\t {unfiltered_sum_listened / 3600000} hours '
        f'or\n\t {unfiltered_sum_listened / 86400000} days')


def most_skipped(all_lines_df):
    pass



path_to_json = r"my_spotify_data\Spotify Extended Streaming History"
all_file_locs = [path_to_json + '\\' + pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

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

# all_lines_df.to_csv('temp_file4.csv')

filtered_df_2024 = all_lines_df[all_lines_df['DateTime'] > '2024']

sum_heard_music(all_lines_df)
print(f"First song ever listened to was: ", end="")
first_song(all_lines_df)
print(f"First song listened to in 2024 was: ", end="")
first_song(filtered_df_2024)

print(f'Done in {time.time() - start_time}')
exit()  # TEMP

print(json.dumps(list(all_lines), indent=2))
print(f'Done in {time.time() - start_time} seconds')
