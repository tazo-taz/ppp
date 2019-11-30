import speech_recognition as sr  # import the library
import webbrowser as wb      #


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()                # initialize recognizer

with sr.Microphone() as source:   # mention source it will be either Microphone or audio files.
    print('Say Something!')
    audio = r.listen(source)      # listen to the source
    print('Done!')

try:
    text = r.recognize_google(audio)      # use recognizer to convert our audio into text part
    print('Google thinks you said:\n' + text)   # In case of voice recognized  clearly
    lang = 'en'

    f_text = 'https://www.google.co.in/search?q=' + text
    wb.get(chrome_path).open(f_text)

except Exception as e:
    print(e)        # In case of voice not recognized  clearly
