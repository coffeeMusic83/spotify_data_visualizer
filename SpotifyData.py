from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  # lukee .env-tiedoston

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-top-read user-read-recently-played"
))  # spotipy lukee tunnisteet automaattisesti ympäristömuuttujista

results = sp.current_user_top_tracks(limit=10, time_range="long_term")
for item in results["items"]:
    print(item["name"], "-", item["artists"][0]["name"])
    
