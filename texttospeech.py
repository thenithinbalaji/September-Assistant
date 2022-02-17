import pyttsx3


def texttospeech(text):
    texttospeech_stop("event")
    engine = pyttsx3.init()

    engine.setProperty("rate", 200)
    engine.setProperty("voice", engine.getProperty("voices")[1].id)
    engine.say(text)

    engine.runAndWait()


def texttospeech_stop(event):
    engine = pyttsx3.init()
    engine.stop()
    pass
