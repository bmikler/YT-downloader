from pytube import YouTube
import ffmpy
import os

while True:

    yt = input("Videos URL: ")

    try:
        yt = YouTube(yt)
    except:
        print("Wrong input!")
        continue

    print("Working...")
    stream = yt.streams.first()

    print("Download...")
    stream.download()

    ff = ffmpy.FFmpeg(
        inputs={yt.title + ".mp4": None},
        outputs={yt.title + ".mp3": None}
    )

    try:
        ff.run()
        os.system("cls")
        print("\n\nCOMPLETE!")
    except:
        os.system("cls")
        print("\nError during conversion into .mp3")
        continue
    finally:
        os.remove(yt.title + ".mp4")
