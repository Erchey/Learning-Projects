import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

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


track_results = sp.search(q="artist:Olivia Rodrigo track:Enough for you", type="track", limit=1)
print(track_results)
if track_results["tracks"]["items"]:
    track_uri = track_results["tracks"]["items"][0]["uri"]
    print(f"Track URI: {track_uri}")
else:
    print("No track found")
