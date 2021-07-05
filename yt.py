from pytube import YouTube
import ffmpy
import os


def main():
    while True:

        yt = input("Videos URL: ")

        # check if input is correct YouTube URL
        try:
            yt = YouTube(yt)
        except:
            print("Wrong input!")
            continue

        # generate new title to avoid bugs with special characters

        ytitle = yt.title
        title = ""

        for i in range(len(ytitle)):
            if ytitle[i] != "|" and ytitle[i] != '"':
                title += ytitle[i]

        # chose the stream - best quality form audio only
        print("Working...")
        stream = yt.streams.filter(only_audio=True).first()

        # check if file exist
        if os.path.exists(title + ".mp3"):
            print("File already exist")
        else:
            download(stream)
            convert(title)


# download mp4
def download(stream):
    print("Downloading...")
    stream.download()


# convert mp4 into mp3 and delete mp4 file
def convert(title):

    # set ffmpeg
    ff = ffmpy.FFmpeg(
        inputs={title + ".mp4": None},
        outputs={title + ".mp3": None}
    )

    try:
        ff.run()
        os.system("cls")
        print("\n\nCOMPLETE!")
    except:
        os.system("cls")
        print("\nError during conversion into .mp3")
    finally:
        os.remove(title + ".mp4")


main()
