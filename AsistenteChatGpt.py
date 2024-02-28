from openai import OpenAI
from gtts import gTTS
import pygame
from io import BytesIO


api_key = "codigo de chat gpt"
client = OpenAI(api_key=api_key)

messages = [
    {"role": "system", "content": "Eres un asistente de oficina."},
    {"role": "user", "content": "Explica la IA."},
    {"role": "user", "content": "Crea una historia corta al respecto."},
]


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(completion.choices[0].message)


texto =str(completion.choices[0].message)

# Crear el archivo de audio
tts = gTTS(text=texto, lang='es')
audio_file = BytesIO()
tts.write_to_fp(audio_file)
audio_file.seek(0)

# Reproducir el audio
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()

# Esperar hasta que termine de reproducirse el audio
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
