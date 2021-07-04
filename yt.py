from pytube import YouTube
import ffmpy
import os

yt = input("Videos URL: ")

yt = YouTube(yt)

stream = yt.streams.first()

stream.download()

ff = ffmpy.FFmpeg(
    inputs = {yt.title + ".mp4" : None}, 
    outputs = {yt.title + ".mp3" : None}
    )

ff.run()

os.remove(yt.title + ".mp4")


