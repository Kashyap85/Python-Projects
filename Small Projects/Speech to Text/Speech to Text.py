import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak')
    print("Listening Your Voice...........")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        
        y='You said : {}'.format(text)
        print(y)
                   
    except:
        print('Sorry could not recognize your voice')
