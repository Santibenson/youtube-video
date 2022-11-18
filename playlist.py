# downloads youtube playlists
from pytube import Playlist



def playlist_download(link):
    playlist_obj = Playlist(link)
    print(f'Downloading: {playlist_obj.title}')
    for video in playlist_obj.videos:
       video.streams.first().download()

# example
playlist_download("https://www.youtube.com/playlist?list=PL4cUxeGkcC9g9gP2onazU5-2M-AzA8eBw")
