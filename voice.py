import edge_tts
import asyncio
import pygame
import os
VOICE = "en-US-GuyNeural"
async def _generate_voice(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("aura_voice.mp3")
def speak(text):
    asyncio.run(_generate_voice(text))
    pygame.mixer.init()
    pygame.mixer.music.load("aura_voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.quit()
    os.remove("aura_voice.mp3")
    
# This is the voice module of Aura.