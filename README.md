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
            "output": "anime.rss"
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
