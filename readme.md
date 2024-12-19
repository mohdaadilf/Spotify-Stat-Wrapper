# Spotify Streaming History Analysis

This script processes and analyzes Spotify's extended streaming history data. It calculates metrics such as total playback time, most skipped songs, least skipped songs, and most played songs.

## Features

1. **First Song Information**: Displays the first song ever listened to and the first song listened to in 2024.
2. **Total Playback Time**: Provides a detailed breakdown of the total time spent listening to tracks or podcasts.
3. **Skip Analysis**: Identifies the most and least skipped songs, along with their skip rates.
4. **Most Played Songs**: Lists the most frequently played tracks.
5. **Time Zone Conversion**: Converts timestamps to Indian Standard Time (IST) for better readability.

## Setup

1. **Requirements**:
   - Python 3.7+
   - Required Python Libraries:
     - `pandas`
     - `json`
     - `os`
     - `time`
     - `itertools`
     - `datetime`

   Install missing libraries with:
   ```bash
   pip install pandas
   ```

2. **Input Data**:
   - Ensure your Spotify streaming history files are in JSON format and placed in the `my_spotify_data/Spotify Extended Streaming History/` directory.
   - Files should follow the naming convention `Streaming_History_Audio_<year-range>_<index>.json`.

## Usage

1. Place your Spotify JSON files in the specified folder.
2. Run the script:
   ```bash
   python <script_name>.py
   ```

3. The script will output:
   - The first song ever listened to.
   - Total playback time in various units (ms, seconds, minutes, hours, days).
   - The first song listened to in 2024.
   - Summaries of most skipped, least skipped, and most played songs.

4. Optional: Save the generated summaries to CSV files by uncommenting the relevant lines in the script.

## Disclaimer

This script is provided "as is" without any guarantees or warranties. The author is not liable for any errors, data loss, or other issues that may arise from its use. Use it at your own risk.
