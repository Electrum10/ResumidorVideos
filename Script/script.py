import openai

#Función para descargar el mp3 del video
def youtubeDescargar (link):
    #Declarar Librerías
    import os
    from pytube import YouTube

    #Variables
    yt = YouTube(link)

    #Lógica Pytube
    audio = yt.streams.filter(only_audio=True).first()
    output_file = audio.download()

    #Lógica OS
    basename = os.path.basename(output_file)
    nombre, formato = basename.split(".")
    audio_file = f"{nombre}.mp3"
    audio_file = audio_file.replace(" ", "-")
    os.rename(basename, audio_file)
    return audio_file
mp3_archivo = youtubeDescargar(input(f"Link de YouTube: "))

