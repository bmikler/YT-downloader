from pytubefix import YouTube
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
            if ytitle[i].isalnum() or ytitle[i].isspace() or ytitle[i] == "-":
                title += ytitle[i]

        # chose the stream - best quality form audio only
        print("Working...")
        stream = yt.streams.filter(only_audio=True).first()

        # check if file exist
        if os.path.exists("download/" + title + ".mp3"):
            print("File already exist")
        else:
            download(stream, title)
            convert(title)


# download mp4
def download(stream, title):
    print("Downloading...")
    stream.download("tmp", title + ".mp4")


# convert mp4 into mp3 and delete mp4 file
def convert(title):
    # set ffmpeg
    ff = ffmpy.FFmpeg(
        inputs={"tmp/" + title + ".mp4": None},
        outputs={"download/" + title + ".mp3": None}
    )

    try:
        ff.run()
        clear_screen()
        print("COMPLETE!")
        print("You can download another file")
    except Exception as e:
        clear_screen()
        print(f"\nError during conversion into .mp3: {e}")
    finally:
        os.remove("tmp/" + title + ".mp4")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


main()
