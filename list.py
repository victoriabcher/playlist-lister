from pytube import Playlist
import pandas as pd

playlist_url = 'https://www.youtube.com/playlist?list=PLQcLb-PUD9WNZnVBYDKEonioyJw3nEaOM'
output_file = 'playlist_estatistica.xlsx'
playlist = Playlist(playlist_url)

video_data = []

for video in playlist.videos:
    try:
        titulo = video.title
        duracao = video.length  # Duração em segundos
        link = video.watch_url
        canal = video.author

        video_data.append({
            'Título': titulo,
            'Duração (min)': f"{duracao // 60}m {duracao % 60}s",
            'Link': link,
            'Canal': canal,
            'Playlist': playlist.title
        })

    except Exception as e:
        print(f"Erro ao acessar o vídeo: {video.watch_url}. Erro: {e}")

df = pd.DataFrame(video_data)
df.to_excel(output_file, index=False)
print(f'Informações dos vídeos foram exportadas para {output_file}')
