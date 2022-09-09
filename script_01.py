import pyttsx3
import speech_recognition as sr
from colorama import *
from fuzzywuzzy import fuzz
import datetime
import random
import sys
from os import system
import webbrowser


ndel = ['куча', 'чуча', 'кученция', 'кучка', 'кученька', 'кучелло',
        'не могла бы ты', 'пожалуйста', 'текущее', 'сейчас']


commands = ['текущее время', 'сейчас времени', 'который час',
            'открой браузер', 'открой интернет', 'запусти браузер',
            'привет', 'добрый день', 'здравствуй',
            'пока', 'вырубись',
            'выключи компьютер', 'выруби компьютер',
            'найди', 'посмотри', 'загугли', 'погугли', 'поищи', 'глянь']


r = sr.Recognizer()
engine = pyttsx3.init()
text = ''
j = 0
num_task = 0


def talk(speech):
    print(speech)
    engine.say(speech)
    engine.runAndWait()


def fuzzy_recognizer(rec):
    global j
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(rec, commands[i])
        if (k > 70) & (k > j):
            ans = commands[i]
            j = k
    return str(ans)


def clear_task():
    global text
    for i in ndel:
        text = text.replace(i, '').strip()
        text = text.replace('  ', ' ').strip()


def listen():
    global text
    text = ''
    with sr.Microphone() as source:
        print("Я вас слушаю...")
        r.adjust_for_ambient_noise(source)  # метод для автоматического понижени уровня шума
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ru-RU").lower()
        except sr.UnknownValueError:
            pass
        # print(text)
        system('cls')
        clear_task()
        return text


def cmd_init():
    global text, num_task
    text = fuzzy_recognizer(text)
    print(text)
    if text in cmds:
        if (text != 'пока') & (text != 'привет') & (text != 'который час') & (text != 'сейчас времени')\
                & (text != 'сейчас времени') & (text != 'добрый день') & (text != 'здравствуй')\
                & (text != 'здравствуй'):
            k = ['Секундочку', 'Сейчас сделаю', 'Уже выполняю']
            talk(random.choice(k))
        cmds[text]()
    elif text == '':
        print("Команда не распознана")
    num_task += 1
    if num_task % 10 == 0:
        talk('У вас будут еще задания?')
    engine.runAndWait()
    engine.stop()


def sklon():
    now = datetime.datetime.now()
    n = now.hour
    if n % 10 == 1 and (n % 100 < 10 or n % 100 > 20):
        return ' час'

    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 > 20):
        return ' часа'

    else:
        return ' часов'


def time():
    now = datetime.datetime.now()
    talk("Сейчас " + str(now.hour) + sklon() + " : " + str(now.minute) + " минут")


def open_brows():
    webbrowser.open('https://google.com')
    talk("Браузер открыт!")


def web_search(search):  # Создание функции для выполнения запроса и открытия вкладки с запросом в браузере
    words = ('найди', 'найти', 'ищи', 'кто такой', 'что такое')  # Создание словаря с ключевыми словами для выполнения запроса
    remove = ["пожалуйста", "ладно", "давай", "сейчас"]  # Создание списка со слов которые будут удалены из запроса
    if text.startswith(words):  # Проверка начинается, ли наш голосовой запрос с ключевых слов записанных в словаре words
        for i in words:  # Создание цикла для очистки слов находящихся в словаре words в запросе
            search = search.replace(i, '')  # Очистка ключевых слов, находящихся в словаре words с запроса
            for j in remove:  # Создание цикла для очистки слов находящихся в списке remove в запросе
                search = search.replace(j, '')  # Очистки слов находящихся в списке remove в запросе
                search = search.strip()  # Преобразование переменной search в строку
        print(search)  # Вывод текста нашего запроса
        webbrowser.open(f'https://www.google.com/search?q={search}&oq={search}'
                        f'81&aqs=chrome..69i57j46i131i433j0l5.2567j0j7&sourceid=chrome&ie=UTF-8')  # выполнение запроса в браузере


while True:  # Запуск бесконечного цикла
    web_search(listen())  # Запуск функции web_search(search) и передача в неё в качестве параметра функцию listen()


def shut():  # выключает компьютер
    global text
    talk("Подтвердите действие!")
    text = listen()
    print(text)
    if (fuzz.ratio(text, 'подтвердить') > 60) or (fuzz.ratio(text, "подтверждаю") > 60):
        talk('Действие подтверждено')
        talk('До скорых встреч!')
        system('shutdown /s /f /t 10')
        quite()
    elif fuzz.ratio(text, 'отмена') > 60:
        talk("Действие не подтверждено")
    else:
        talk("Действие не подтверждено")


def hello():
    k = ['Привет, чем могу помочь?', 'Оooo, здраствуйте', 'Приветствую']
    talk(random.choice(k))


def quite():
    x = ['Надеюсь мы скоро увидимся!', 'Рада была помочь', 'Я отключаюсь']
    talk(random.choice(x))
    engine.stop()
    system('cls')
    sys.exit(0)


cmds = {
    'текущее время': time, 'сейчас времени': time, 'который час': time,
    'открой браузер': open_brows, 'открой интернет': open_brows, 'запусти браузер': open_brows,
    'привет': hello, 'добрый день': hello, 'здравствуй': hello,
    'пока': quite, 'вырубись': quite,
    'выключи компьютер': shut, 'выруби компьютер': shut,
}


print(Fore.YELLOW + '', end='')
system('cls')


def main():
    global text, j
    try:
        listen()
        if text != '':
            cmd_init()
            j = 0
    except UnboundLocalError:
        pass
    except NameError:
        pass
    except TypeError:
        pass


while True:
    main()
