from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

# user_input = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
# response = requests.get(f'https://www.billboard.com/charts/hot-100/{user_input}')

#
# for song in song_names:
#     print(song)

APP_ID = os.getenv('SPOTIPY_ID')
print(APP_ID)



# Spotipy
# Initialize spotipy with OAuth authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="9832b65773484c2bb6e505712cd55b6e",
        client_secret="366b18ea6f34488d903da6fb2ba2f712",
        show_dialog=True,
        cache_path="token.txt",
        username="Erchey"
    )
)

# Get the user's Spotify ID
user_id = sp.current_user()["id"]

# Create a new playlist
# playlist_name = "My New Playlist"
# playlist = sp.playlist_add_items(user_id, playlist_name)

# playlist = sp.user_playlists(user_id)
playlist_id = '6i7wjZbDcrPCSGKoFZGnLx'

# Add tracks to the playlist
track_uris = [
    "spotify:track:2E4INiVkDRBXXkFL4kB1Vk"  # Replace with your track URIs
]
sp.playlist_add_items(playlist_id, track_uris)
