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

