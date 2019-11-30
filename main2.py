import speech_recognition as sr  # import the library
import webbrowser as wb  #

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()  # initialize recognizer

with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
    print('Say Something!')
    audio = r.listen(source)  # listen to the source
    print('done,')

try:
    text = r.recognize_google(audio)  # use recognizer to convert our audio into text part
    lang = 'en'
    print(text)
    if 'search in google' in text.lower():
        f_text = 'https://www.google.co.in/search?q=' + text[16:]
        wb.get(chrome_path).open(f_text)
    else:
        print(text)


except:
    print("xmis amocnoba ver moxerxda")  # In case of voice not recognized  clearly
