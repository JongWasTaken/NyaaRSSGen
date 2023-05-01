# NyaaRSSGen

This is a simple python script intended to be run in a docker container.
It will take an `input.txt` text file, consisting of tv show names, and assemble it into a Nyaa.si URL.
This URL is then opened and read. The result is saved to `output_name.rss` file in `./web/`. This folder is being served on the users chosen port (default 6969).

## Config file
A simple JSON file named `config.json` in `./exposed/`.
Sample:  
```
{
    "targets": [
        {
            "input": "testdata.txt",
            "output": "anime.rss",
            "username": "subsplease",
            "category": "1_2",
            "quality": "1080p"
        }
    ]
}
```

## Environment Variables
The port and time interval can be adjusted using environment variables:
|Name|Default Value|Description|
|--|--|--|
|PORT|6969|Port for the web server|
|TIME|1800|Interval in seconds|

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
RUN git clone https://JongWasTaken:GITHUB_PAT_GOES_HERE@github.com/JongWasTaken/NyaaRSSGen /app
WORKDIR /app
RUN mkdir -p /app/exposed
RUN mkdir -p /app/web
VOLUME /app/exposed
ENV PORT=6969
ENV TIME=3600
CMD ["./launch.sh"]
```  
Since this repository is private, a GitHub PAT with sufficient rights is required to clone it.
