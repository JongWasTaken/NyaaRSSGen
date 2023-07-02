# NyaaRSSGen

This is a simple python script intended to be run in a docker container.
It will take an `input.txt` text file, consisting of tv show names, and assemble it into a Nyaa.si URL.
This URL is then opened and read. The result is saved to `output_name.rss` file in `./web/`.  
This folder is being served on the chosen port (default 6969).  
Finally, point your favorite torrent client to the rss file.

## Config file
A simple JSON file named `config.json` in `./exposed/`.
Example:  
```
{
    "targets": [
        {
            "input": "winter2023.txt",
            "output": "anime-subsplease.rss",
            "username": "subsplease",
            "category": "1_2",
            "quality": "1080p"
        }
    ]
}
```
All keys need to be present.  
Leave `username` empty for `Anonymous` uploads.  
If `category` is empty, `Anime - English translated` is assumed (`1_2`).  
If `quality` is empty, `1080p` is assumed.`

## Input file
Example (Winter 2023):  
```
# Monday
Vinland Saga S2
Dead Mount Death Play
Kimi wa Houkago Insomnia
Kanojo ga Koushaku-tei ni Itta Riyuu

# Tuesday

# Wednesday
Oshi no Ko
Kaminaki Sekai no Kamisama Katsudou

# Thursday
Dr. Stone S3
Yuusha ga Shinda

# Friday
Mashle
Kawaisugi Crisis
Mahou Shoujo Magical Destroyers
Rokudou no Onna-tachi
Tonikaku Kawaii S2

# Saturday
Jigokuraku
Boku no Kokoro no Yabai Yatsu
Otonari ni Ginga
Yamada-kun to Lv999 no Koi wo Suru

# Sunday
```
Comments are only allowed at the beginning of a line.

## Environment Variables
The port and time interval can be adjusted using environment variables:
|Name|Default Value|Description|
|--|--|--|
|PORT|6969|Port for the web server|
|TIME|1800|Interval in seconds|

> :warning: **Possible rate limiting**: You might have to increase the interval time if you have too many targets!  

## Manual Trigger
If you do not want to wait for the next interval, simply create a file named `trigger` in `/app/exposed`.
This is useful when testing new input files.  
`touch /mnt/smb/Docker/rss/trigger`  
The script checks for this file every 60 seconds, and if it exists, it gets deleted and all rss feeds get rechecked.

## Example Dockerfile
```
FROM python:3.10-bullseye
RUN apt-get -y update
RUN apt-get -y install git
RUN git clone https://github.com/JongWasTaken/NyaaRSSGen /app
WORKDIR /app
RUN mkdir -p /app/exposed
RUN mkdir -p /app/web
VOLUME /app/exposed
ENV PORT=6969
ENV TIME=3600
CMD ["./launch.sh"]
```