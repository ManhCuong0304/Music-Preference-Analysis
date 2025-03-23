import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

# 🔹 Set up API credentials
SPOTIFY_CLIENT_ID = "..."
SPOTIFY_CLIENT_SECRET = "..."

# 🔹 Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 🔹 Load your song list from Excel
df = pd.read_excel("songs.xlsx")  # Make sure your file has an "Artist" column

# 🔹 Function to get genres for an artist
def get_genre(artist):
    try:
        # Search for the artist
        results = sp.search(q=f"artist:{artist}", type="artist", limit=1)

        if results["artists"]["items"]:
            artist_info = results["artists"]["items"][0]
            genres = ", ".join(artist_info.get("genres", []))

            return genres if genres else "Unknown Genre"
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status == 429:  # Rate limit error
            retry_after = int(e.headers.get("Retry-After", 10))  # Default 10s if not provided
            print(f"⚠️ Rate limit exceeded. Retrying in {retry_after} seconds...")
            time.sleep(retry_after)
            return get_genre(artist)  # Retry request
    except Exception as e:
        print(f"Error fetching genre for {artist}: {e}")
        return "Error"

# 🔹 Remove duplicates to avoid redundant API calls
df["Artist"] = df["Artist"].str.strip()  # Remove extra spaces
unique_artists = df["Artist"].drop_duplicates()

# 🔹 Get genres for unique artists
artist_genres = {artist: get_genre(artist) for artist in unique_artists}

# 🔹 Map the genres back to the DataFrame
df["Genre"] = df["Artist"].map(artist_genres)

# 🔹 Save to a new Excel file
df.to_excel("songs_with_genres.xlsx", index=False)

print("Done! Check 'songs_with_genres.xlsx'")
