from pytube import YouTube

def downloader(link):
    youtube_obj = YouTube(link)
    youtube_vidfile = youtube_obj.streams.get_highest_resolution()
    try:
        youtube_vidfile.download()
    except:
        print("An unknown error occurred")
    print("Video downloaded successfully")


# example
downloader("https://www.youtube.com/watch?v=eao7ABGFUXs&list=PL4cUxeGkcC9gZD-Tvwfod2gaISzfRiP9d&index=17")

# convert a youtube video to an audio

def audio(link):
    youtube_obj = YouTube(link)
    youtube_aud = youtube_obj.streams.get_audio_only()
    try:
        youtube_aud.download()
    except:
        print("An unknown error occurred")
    print("Audio downloaded successfully")

# example
audio("https://www.youtube.com/watch?v=eao7ABGFUXs&list=PL4cUxeGkcC9gZD-Tvwfod2gaISzfRiP9d&index=17")


# they have an api, you can turn it into a full-blown webapp