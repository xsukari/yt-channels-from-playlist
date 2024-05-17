## Where EXE?

It's python script, it is run by following these steps:

### Initial setup

1. Download the source or clone the repo with git
2. Unzip if downloaded, go into the "yt-channels-from-playlist" folder
3. Open a command line from that folder or navigate to the folder from a command line
4. Create a new venv, because installing packages globally sucks, by executing "python -m venv venv"
5. Execute "source venv/bin/activate" on Linux or "venv\Scripts\activate" on Windows
6. Execute "pip install pytube"
7. Run the following: ``` python main.py "put_playlist_url_here" ```
8. Your playlist will be processed, the result will be written to "results.txt" in the script folder (where main.py is located)

### Already did the initial setup?

1. Navigate to the script folder and open a command line or open a command line first and navigate to the folder from there
2. Activate the virtual environment (venv) by running "source venv/bin/activate" on Linux or "venv\Scripts\activate" on Windows
3. Execute the following: ``` python main.py "put_playlist_url_here" ```

### Didn't work?

1. You didn't follow the steps correctly, f. e. you didn't put the playlist url within quotation marks
2. Youtube messed something up
3. Youtube changed their API and the package I'm using to read youtube content (pytube) is outdated
