import yt_dlp


def descargar_audio(url, carpeta, formato):
    try:
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': formato,
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print(f"Descarga completada: {url}")

    except Exception as e:
        print(f"Error al descargar {url}: {e}")
