# Anime_Downloader
Downloads anime from gogoanime

# Usage
`python anime_downloader.py [-h] [-q quality] [-d] -s source_url [-n no of episodes]`
## Arguments:
  -h, --help            show this help message and exit
  
  -q quality, --quality quality
                        Quality of Video.<br>
                        0- 1080p<br>
                        1- 720p<br>
                        2- 480p<br>
                        3- 360p.<br>
                        Default: 1080p.<br>
                        If current quality not found, will download next best quality available
                        
  -d, --download        Specify if you want to download, by default just simulates
  
  -s source_url, --source source_url
                        URL of the starting episode you want to start downloading (Required argument)
                        
  -n no of episodes, --noep no of episodes
                        Specify number of episodes, default is 1 episode

# Usage examples
`python3 anime_downloader.py -s https://gogoanime.so/hunter-x-hunter-2011-episode-101 -n 5 -d ` <br>downloads 5 episode ( from 101 to 105 ) of hunter x hunter in 1080p<br><br>
`python3 anime_downloader.py -s https://gogoanime.so/hunter-x-hunter-2011-episode-101 -q 2 -d ` <br>downloads 1 episode ( 101 ) of hunter x hunter in 480p
