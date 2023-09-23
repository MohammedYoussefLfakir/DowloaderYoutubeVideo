import os
from pytube import YouTube

# Demande à l'utilisateur de saisir l'URL de la vidéo YouTube
video_url = input("Entrez l'URL de la vidéo YouTube : ")

# Emplacement où vous voulez enregistrer les vidéos
download_path = "C:\\Users\\simo\\Desktop"

def download_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Téléchargement en cours : {percentage:.2f}%")

def download_youtube_video(url, download_folder):
    try:
        yt = YouTube(url, on_progress_callback=download_progress)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if video:
            print(f"Téléchargement de '{yt.title}' en meilleure qualité disponible...")
            video.download(output_path=download_folder)
            print("Téléchargement terminé.")
        else:
            print("Aucun format vidéo compatible trouvé.")
    except Exception as e:
        print("Une erreur est survenue :", str(e))

if __name__ == "__main__":
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    download_youtube_video(video_url, download_path)
