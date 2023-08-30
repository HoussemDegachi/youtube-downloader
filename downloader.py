from pytube import YouTube
from youtubesearchpython import VideosSearch
from sys import exit
from re import search
import csv
import argparse

# variables
success = 0
failure = 0
total = 0
    
def main():
    # var
    videos = []

    # get argv
    argv = get_argv()

	# if download by directory(list of url's)
    if argv.d != None:
	    # get download list and add it to local list
        try:
            with open(argv.d) as file:
                rows = csv.reader(file)
                for row in rows:
                    videos.append(row[0])
        except:
            print(f"file \"{argv.d}\" doesn't exist")
    else:
        # add url or name to list
        videos.append(argv.u)

	# download local list by download videos
    download_videos(videos)

    # print stats
    print(f"\n{success} videos have been downloaded succesfully\n{failure} video failed to download\n{total} in total")

def get_argv():
    # setup argv
    parser = argparse.ArgumentParser(description="to download a video either enter -u followed by the name or url of the video or -d follwed by the directory of the list where it contains the names or url's of the videos")
    parser.add_argument("-d", default=None, help="directory of file which contains url's or/and names of videos", type=str)
    parser.add_argument("-u", default=None, help="name or url of video", type=str)
    argv = parser.parse_args()

    # validate argv
    if (argv.d == None and argv.u == None) or (argv.d != None and argv.u != None):
        exit("Incorrect usage\n\"python downloader.py -h\" for help")

    # return argv
    return argv

def download_videos(videos):
	# loop into videos
    for video in videos:
        # if video is a url download by url
        if search(r"(?:https|http)://(?:www\.)?(?:youtube\.com|youtu\.be)/(?:watch\?v=|playlist\?list=)(?:\w)", video):
            download_video_by_url(video)
        else:
            # else download by name
            download_video_by_name(video)

def download_video_by_name(video_name):
	# search video
    video = VideosSearch(video_name, limit=1).result()

    # get video url
    video_link = video["result"][0]["link"]
    video_download_name = video["result"][0]["title"]
    video_channel = video["result"][0]["channel"]["name"]

    # download video by url
    print(f"found {video_download_name} by {video_channel} for {video_name} keyword")
    download_video_by_url(video_link)

def download_video_by_url(video):
    global success
    global failure
    global total

    # call pytube to download url
    try:
        yt = YouTube(video)
        print(f"downloading video number {total + 1}...")
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    except:
        print(f"video failed to download \"{video}\"")
        failure += 1
        pass
    else:
        success += 1
        print(f"video done downloading")
    total += 1

if __name__ == "__main__":
    main()