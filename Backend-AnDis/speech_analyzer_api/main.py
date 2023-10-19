import config
import openai

openai.api_key = config.api_key

#audio_file= open("D:\Descargas\AudioLarguito.mp3", "rb")
#transcript = openai.Audio.transcribe("whisper-1", audio_file)

#print(transcript.text)

def transcribe_audio(audio_file_path):
    with open("D:\Descargas\AudioLarguito.mp3", 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

audio = transcribe_audio("D:\Descargas\AudioLarguito.mp3")

##RESUMEN
def abstract_summary_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Eres una IA altamente capacitada y capacitada en comprensión y resumen de idiomas. Me gustaría que leyeras el siguiente texto y lo resumieras abstracto conciso. Trate de retener los puntos más importantes, proporcionando un resumen coherente y legible que pueda ayudar a una persona a comprender los puntos principales de la discusión sin necesidad de leer el texto completo. Evite detalles innecesarios o puntos tangenciales. Empieza con 'Tu discurso trata de'. Solo español"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

##Puntos Clave
def key_points_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about. In Spanish"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#ANALISIS DE SENTIMIENTO
def sentiment_analysis(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible. In spanish"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

#PALABRAS CLAVE
def key_words(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "Dime las palabras clave de la transcripción, sé preciso, sólo las palabras clave o key words"
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

##Printeando transcripción
print("TRANSCRIPCIÓN.\n"+audio+"\n")
##Probando resumen
resumen = abstract_summary_extraction(audio)
print("Probando resumen.\n"+ resumen+"\n")
##Probando puntos clave
puntos_clave = key_points_extraction(audio)
print("Probando puntos clave\n"+ puntos_clave+"\n")
##Probando analisis de sentimientos
#analisis_sentimientos = sentiment_analysis(audio)
#print("Probando análisis de sentimientos.\n"+ analisis_sentimientos)
##Probando palabras clave
palabras_clave = key_words(audio)
print("Probando palabras clave\n"+ key_words(audio)+"\n")

