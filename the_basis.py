# текст в голос
import pyttsx3

engine = pyttsx3.init()


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


program = True

while program:
    k = input('Введите текст ')
    if k != 'пока':
        talk(k)
    if k == 'пока':
        talk('До скорых встреч')
        program = False


# голос в текст
# import speech_recognition as sr
#
# r = sr.Recognizer()
#
#
# def listen():
#     with sr.Microphone() as source:
#         print('Скажите что-нибудь...')
#         r.adjust_for_ambient_noise(source)  # метод авто понижения уровня шума
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio, language='ru-RU')
#         except sr.UnknownValueError:
#             pass
#         print(text)
#         return text
#
#
# listen()
