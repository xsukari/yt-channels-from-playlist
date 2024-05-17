import argparse
import time
import sys
import math
from pytube import Playlist

parser = argparse.ArgumentParser(description="Process Youtube playlist URL")
parser.add_argument("playlist", type=str, help='playlist url to process')
args = parser.parse_args()

playlist = Playlist(args.playlist)
channels = []

spinner = ["|", "/", "—", "\\"]
counter = 0
startTime = time.time()

for video in playlist.videos:
    if video.author not in channels:
        channels.append(video.author)
    indicator = f"Processing {spinner[counter % len(spinner)]}"
    sys.stdout.write("\r" + indicator)
    counter += 1

endTime = time.time()

print(f"\nFetched {len(channels)} channel in {math.floor(endTime - startTime)} seconds")

fileName = "channels.txt"

with open(fileName, "w") as file:
    for channel in channels:
        file.write(f"{channel}\n")

print(f"Channels written to {fileName} in script folder")
