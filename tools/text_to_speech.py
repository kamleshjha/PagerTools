from flask import request, send_file
from gtts import gTTS

def text_to_speech_route():
    text = request.form["text"]
    tts = gTTS(text)
    tts.save("output.mp3")
    return send_file("output.mp3", as_attachment=True)