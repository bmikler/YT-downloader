from pytube import YouTube

yt = input("Videos URL: ")

yt = YouTube(yt)

stream = yt.streams.first()

stream.download()
