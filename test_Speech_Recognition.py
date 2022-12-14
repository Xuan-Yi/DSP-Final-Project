import speech_recognition as sr

r = sr.Recognizer()
WAV=sr.AudioFile('audio/烏鴉喝水兒童故事中文童話伊索寓言故事睡前故事.flac')
with WAV as source:
    audio=r.record(source)
print(r.recognize_google(audio,show_all=True,language='zh-tw'))