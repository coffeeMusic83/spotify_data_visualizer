# Spotify Data Visualizer

Sovellus, joka hakee omaa Spotify-kuunteludataa ja visualisoi sitä.
Projekti on tekeillä oman mielenkiinnon takia.

## 🚧 Tila: kehitteillä

Tällä hetkellä toteutettu:
- ✅ Autentikointi Spotify Web API:in (OAuth)
- ✅ Käyttäjän top-kappaleiden haku

Seuraavaksi tulossa:
- ⏳ Streamlit-käyttöliittymä
- ⏳ Datan visualisointi (esim. top artistit, kuunteluajat, genret)
- ⏳ Extended Streaming History -datan analysointi

## Teknologiat

- Python
- [Spotipy](https://spotipy.readthedocs.io/) (Spotify Web API -kirjasto)
- python-dotenv
- Streamlit (tulossa)
- pandas (tulossa)

## Miten ajaa paikallisesti

1. Kloonaa repo:
```
   git clone https://github.com/coffeeMusic83/spotify_data_visualizer.git
   cd spotify_data_visualizer
```

2. Luo virtuaaliympäristö ja asenna riippuvuudet:
```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
```

3. Luo Spotify-sovellus osoitteessa [developer.spotify.com](https://developer.spotify.com/dashboard), ja luo `.env`-tiedosto projektin juureen:
```
   SPOTIPY_CLIENT_ID=oma_client_id
   SPOTIPY_CLIENT_SECRET=oma_client_secret
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

4. Aja sovellus:
```
   python SpotifyData.py
```

## Mitä opin

- OAuth-autentikoinnin toteuttaminen ulkoiseen API:in
- Tunnisteiden ja ympäristömuuttujien turvallinen käsittely (.env, .gitignore)
- Git/GitHub-työnkulun perusteet