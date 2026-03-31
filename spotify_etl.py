from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd       
import matplotlib.pyplot as plt   
import re
import json
# Set up Client Credentials
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='ur client id',client_secret='ur client secret'))
# Full track URL (example : tylor swift 50 songs)
track_url="https://open.spotify.com/playlist/7L6mdgEKVTpXlr4UCuG6dt"
# Extract track ID directly from URL using regex
track_id=re.search(r'playlist/([a-zA-Z0-9]+)', track_url)
if track_id:
    track_id = track_id.group(1)
else:
    track_id = None
playlist=sp.playlist(track_id)
print(playlist) 

# Extract metadata
alltracks=[]
for item in playlist['tracks']['items']:
 track = item['track']
 track_data={'Track Name':track['name'],
            'Artist':track['artists'][0]['name'],
            'album':track['album']['name'],
             'Popularity':track['popularity'],
             'Duration (minutes)':track['duration_ms']/60000  ,
            'Year': track['album']['release_date'][:4]          
            }
 alltracks.append(track_data)

 
# convert metadata into dataframe

df=pd.DataFrame(alltracks)
print("track data as data frame")
print(df.head())
# convert into csv
df.to_csv('spotify_track_data.csv', index=False)
# visualization
plt.figure(figsize=(16,10))
bars = plt.bar(df['Track Name'], df['Popularity'], color='skyblue')
for bar, year in zip(bars, df['Year']):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             year, ha='center', va='bottom', fontsize=8, rotation=90)



plt.xlabel('song')
plt.ylabel('popularity')
plt.xticks(rotation=90)
plt.title('spoyify track popularity and release year')
plt.tight_layout()
plt.show()

# for line graph
plt.figure(figsize=(16,10))
plot= plt.plot(df['Track Name'], df['Popularity'],marker='o' ,color='black')
for x, y, year in zip(df['Track Name'], df['Popularity'], df['Year']):
    plt.text(x, y+1, year, ha='center', va='bottom', fontsize=8, rotation=90)
   
plt.title('spoyify track popularity and release year')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

# scatter plot
plt.figure(figsize=(16,10))


plt.scatter(df['Track Name'], df['Popularity'], color='black', marker='o')

# Add year labels
for x, y, year in zip(df['Track Name'], df['Popularity'], df['Year']):
    plt.text(x, y+1, year, ha='center', va='bottom', fontsize=8, rotation=90)

# titles and formatting
plt.title('Spotify track popularity and release year (Scatter)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



