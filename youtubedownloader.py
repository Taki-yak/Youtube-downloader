from pytube import YouTube 

videolink=str(input("Youtube Video Link:"))
yt = YouTube(videolink)
print("Title:",yt.title)
print("views:",yt.views)
yd=yt.streams.get_highest_resolution()
yd.download(r"your-path-to-save-the-video")
