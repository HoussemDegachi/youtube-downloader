## youtube-downloader
download all your favourite YouTube videos at once without using Url's
## usage:
python downloader.py -h for help
python downloader.py -u -d
you have to use either u or d (only one)
- u (means url) you can input next to it the url or name of the video that you want to download
- d (means directory) you can input the directory where the file which contains the names or/and url's of the video/s exist
## technologies:
- python
- pytube library
- youtube-search-python library
- sys library
- re library
- csv library
- argparse library
## Implemetation
### main function
it is responsible for controling the project's behaviours
it gets the argv (user input via the cli)
if directory mode is used it tries to get all data provided and appends it to a list and if an error raises it quits the system
if is a url mode it adds the url to list
then it downloads the list using download_videos function
### get_argv function
it sets up argpaser system
and it validates that that (-u and -d) are not both used or not used at the same time
### download_videos function
accepts list as input which contains names or/and url's
then for all videos:
it checks wether this is a url or name
if url it calls download_video_by_url
else id calls download_video_by_name
### download_video_by_url
it accepts url as a string as input
it calls pytube to download video with the provided url
if url doesn't exist it will not download
### download_video_by_name
it accepts name of video as input
it calls the youtube-search-python library
and it gets video url
finally it calls download_video_by_url passing the new url to be downlaoded
