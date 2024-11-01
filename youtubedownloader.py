from pytube import YouTube 

videolink=str(input("Youtube Video Link:"))
yt = YouTube(videolink)
print("Title:",yt.title)
print("views:",yt.views)
downloader=yt.streams.get_highest_resolution()
downloader.download(r"your-path-to-save-the-video")
