import config
import openai

openai.api_key = config.api_key

audio_file= open("D:\Descargas\prueba2.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript.text)