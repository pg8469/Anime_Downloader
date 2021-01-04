import requests
from bs4 import BeautifulSoup
import requests
import re
import pprint
import urllib
import sys
import time
import argparse
from argparse import RawTextHelpFormatter

qualities=['1080','720','480','360']
preferred_quality=0
no_episodes=1
want_to_download=False


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * (int(duration) + 1))) 
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

#Argument parsing here
parser=argparse.ArgumentParser(description='Downloads the anime from gogoanime')
parser.add_argument('-q','--quality',type=int,metavar='quality',
                    help=
                    "Quality of Video.  0- 1080p, 1- 720p, 2- 480p, 3- 360p.  Default: 1080p.                             If current quality not found, will download next best quality available",
                    
                    )
parser.add_argument('-d','--download',action="store_true",
                    help='Specify if you want to download, by default just simulates'
                    )
parser.add_argument('-s','--source',metavar='source_url',required=True,
                    help='URL of the starting episode you want to start downloading'
                    )
parser.add_argument('-n','--noep',metavar='no of episodes',type=int,
                    help='Specify number of episodes, default is 1 episode'
                    )
args=parser.parse_args()

if args.quality:
    preferred_quality=args.quality
    if preferred_quality<0 or preferred_quality>3:
        preferred_quality=0
if args.download:
    want_to_download=True
start_url=args.source
if args.noep:
    no_episodes=args.noep
    
    
current_episode=int(start_url.split('-')[-1])

anime_name_regex=re.compile(r'/(.*)-episode.*')
anime_name = anime_name_regex.search(start_url).group(1).split('/')[-1]

print("Anime name:",anime_name)
print(f'Specified range of episodes: {current_episode}-{current_episode+no_episodes-1}')
print(f'Selected quality: {qualities[preferred_quality]}p')
for epno in range(current_episode,current_episode+no_episodes):
    url=start_url.split('-')
    url[-1]=str(epno)
    url='-'.join(url)
    # url=f'https://gogoanime.so/tokyo-ghoul-a-episode-{epno}'
    print('########################################################################################################')
    print(f"Downloading episode {epno}....")
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    down=soup.select('.dowloads')[0]
    link=down.findChildren('a')[0]
    link=link.get('href')

    # print(link)
    res2=requests.get(link)
    
    soup2=BeautifulSoup(res2.text,'html.parser')
    down_links=soup2.select('.dowload')
    final_links={}
    reg = re.compile(r'(\d+)P')
    for down_link in down_links:
        qual = reg.search(down_link.text)
        if qual:
            final_links[qual.group(1)]=down_link.findChildren('a')[0].get('href')


    for qual in range(preferred_quality,4):
        if(qualities[qual] in final_links):
            print(f'Downloading in {qualities[qual]}p')
            filenameregex = re.compile(r'/(EP.*)\?')
            filename=filenameregex.search(final_links[qualities[qual]])
            # print(filename.group(1))
            site = urllib.request.urlopen(final_links[qualities[qual]])
            headers=str(site.headers)
            sizeregex=re.compile(r'Length: (\d+)')
            filesize=sizeregex.search(headers)
            filesize=int(filesize.group(1))/(1024*1024)
            print('File Size:',int(filesize),'MB')
            print('File name:',anime_name+'-'+filename.group(1))
            if want_to_download:
                urllib.request.urlretrieve(final_links[qualities[qual]],anime_name+'-'+filename.group(1),reporthook)
            # print(f'{qualities[qual]}:{final_links[qualities[qual]]}')
            print('')
            break
        print(f'{qualities[qual]}p not found, checking next best quality')