#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import openai
openai.api_key = "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"
#audio_file= open("/home/andres/catkin_ws/src/tutorial/audio_files/u_audio.wav", "rb")
with open("/home/andres/catkin_ws/src/tutorial/audio_files/u_audio.wav", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format="text",
        language="es"
    )
print("j" + transcript + "j")
d = "kkakakaka"
print("j" + d + "j")

transcript = transcript.strip()
print(transcript)