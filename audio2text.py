import speech_recognition as sr
import os
import io

r = sr.Recognizer()
r.recognize_google()
i = 0


for filename in os.listdir(directory):
    if filename.endswith(".WAV") or filename.endswith(".wav"):
        while i < 10:
            f = open("audio2text" + str(i) + ".txt", 'w', encoding= 'utf-8')
            with filename as source:
            audio = r.listen(source)
            f.write("TRANSCRIPT:   " + r.recognize_google(audio))
            f.close()
            i + 1
        continue
    continue
    else:
        print("Your File Type is Not Supported!")

    
