'''
XXX

Это мой шифратор / дешифратор / дешифратор без ключа.
Было прикольно это реализовать — ушло примерно пару часов (2–4).
Первый более-менее большой проект по моим меркам.
Не все ошибки убрал, но, в принципе, считаю проект завершённым.
GOOD LUCK!

XXX prod. nixonee
'''

eng = [
    [chr(i) for i in range(65, 91)],   # заглавные A-Z
    [chr(i) for i in range(97, 123)]   # прописные a-z
]
rus = [
    [chr(i) for i in range(1040, 1072)],  # заглавные А-Я
    [chr(i) for i in range(1072, 1104)]   # прописные а-я
]

def questions(): # Функция опроса пользователя
    while True: # inf debug Ошибок ввода
        language = input("Выберите язык: ru - Русский, en - Английский \n")
        if language == "ru" or language == "en":
            break
        else:
            continue
    while True: # inf debug Ошибок ввода
        direction = input("Выберите операцию: \n1. Шифрование \n2. Дешифрование \n3. Дешифрование без ключа \n")
        if direction == "3":
            return language, 0, int(direction)
        if direction == "1" or direction == "2":
            break
        else:
            continue
    while True: # inf debug Ошибок ввода
        shift = input("Выберите отступ: \n")
        if shift.isdigit() == True:
            break
        else:
            continue
    return language, int(shift), int(direction)

def cipher(language, shift): # Функция шифрования
    text = input("Введите текст: \n") # Запрос исходного текста
    text_cipher = "" # Создание строки для последующей записи зашифрованного текста
    if language == "ru": # Если язык Русский ==> Сценарий 1
        for i in range(len(text)): # Итерируем посимвольно исходный text
            if text[i].isupper() == True: # Если символ заглавный ==> Берем из 0 подсписка списка rus
                text_cipher += text_cipher.join(rus[0][(((rus[0].index(text[i]) + shift) % len(rus[0])))])
                continue
            if text[i].islower() == True: # Если символ строчный ==> Берем из 1 подсписка списка rus
                text_cipher += text_cipher.join(rus[1][(((rus[1].index(text[i]) + shift) % len(rus[1])))])
                continue
            else:
                text_cipher += text_cipher.join(text[i]) # if символ не из алфовита
    if language == "en": # Если язык Английский ==> Сценарий 2
        for i in range(len(text)): # Итерируем посимвольно исходный text
            if text[i].isupper() == True: # Если символ заглавный ==> Берем из 0 подсписка списка eng
                text_cipher += text_cipher.join(eng[0][((eng[0].index(text[i]) + shift) % len(eng[0]))])
                continue
            if text[i].islower() == True: # Если символ строчный ==> Берем из 1 подсписка списка eng
                text_cipher += text_cipher.join(eng[1][((eng[1].index(text[i]) + shift) % len(eng[1]))])
                continue
            else:
                text_cipher += text_cipher.join(text[i]) # if символ не из алфовита
    return text_cipher

def de_cipher(language, shift): # Функция дешифрования
    text = input("Введите текст: \n") # Запрос исходного текста
    text_de_cipher = "" # Создание строки для последующей записи дешифрованного текста
    if language == "ru": # Если язык Русский ==> Сценарий 1
        for i in range(len(text)): # Итерируем посимвольно исходный text
            if text[i].isupper() == True: # Если символ заглавный ==> Берем из 0 подсписка списка rus
                text_de_cipher += text_de_cipher.join(rus[0][(((rus[0].index(text[i]) - shift) % len(rus[0])))])
                continue
            if text[i].islower() == True: # Если символ строчный ==> Берем из 1 подсписка списка rus
                text_de_cipher += text_de_cipher.join(rus[1][(((rus[1].index(text[i]) - shift) % len(rus[1])))])
                continue
            else:
                text_de_cipher += text_de_cipher.join(text[i]) # if символ не из алфовита
    if language == "en": # Если язык Английский ==> Сценарий 2
        for i in range(len(text)): # Итерируем посимвольно исходный text
            if text[i].isupper() == True: # Если символ заглавный ==> Берем из 0 подсписка списка eng
                text_de_cipher += text_de_cipher.join(eng[0][((eng[0].index(text[i]) - shift) % len(eng[0]))])
                continue
            if text[i].islower() == True: # Если символ строчный ==> Берем из 1 подсписка списка eng
                text_de_cipher += text_de_cipher.join(eng[1][((eng[1].index(text[i]) - shift) % len(eng[1]))])
                continue
            else:
                text_de_cipher += text_de_cipher.join(text[i]) # if символ не из алфовита
    return text_de_cipher

def de_cipher_nokey(language): # Функция расшифровки текста с неизвестным ключом
    text = input("Введите текст: \n") # Запрос исходного текста
    text_de_cipher_nokey = ""
    if language == "en":
        for shift in range(26):
            text_de_cipher_nokey = ""
            for i in range(len(text)): # Итерируем посимвольно исходный text
                if text[i].isupper() == True: # Если символ заглавный ==> Берем из 0 подсписка списка eng
                    text_de_cipher_nokey += text_de_cipher_nokey.join(eng[0][((eng[0].index(text[i]) - shift) % len(eng[0]))])
                    continue
                elif text[i].islower() == True: # Если символ строчный ==> Берем из 1 подсписка списка eng
                    text_de_cipher_nokey += text_de_cipher_nokey.join(eng[1][((eng[1].index(text[i]) - shift) % len(eng[1]))])
                    continue
                else:
                    text_de_cipher_nokey += text_de_cipher_nokey.join(text[i]) # if символ не из алфовита
            print(shift, ".", text_de_cipher_nokey)
            print()
            print("-" * 50, "\n")
    elif language == "ru":
        for shift in range(32):
            text_de_cipher_nokey = ""
            for i in range(len(text)): # Итерируем посимвольно исходный text
                if text[i].isupper() == True: # Если символ заглавный ==> Берем из 0 подсписка списка rus
                    text_de_cipher_nokey += text_de_cipher_nokey.join(rus[0][(((rus[0].index(text[i]) - shift) % len(rus[0])))])
                    continue
                elif text[i].islower() == True: # Если символ строчный ==> Берем из 1 подсписка списка rus
                    text_de_cipher_nokey += text_de_cipher_nokey.join(rus[1][(((rus[1].index(text[i]) - shift) % len(rus[1])))])
                    continue
                else:
                    text_de_cipher_nokey += text_de_cipher_nokey.join(text[i]) # if символ не из алфовита
            print(shift, ".", text_de_cipher_nokey)
            print()
            print("-" * 50, "\n")

def errors_message(): # Функция вывода в консоль красивой таблички с Ошибкой
    print()
    print("*" * 100)
    print()
    print("Ошибка введите выберите правильную операцию!!")
    print()
    print("*" * 100)
    print()

while True:  # Реализация inf цикла программы
    print()
    print("=" * 100)
    print()
    print("Добро пожаловать в Шифратор/Дешифратор Цезаря")

    language, shift, direction = questions() # Вызов & Распаковка ответов функции в переменные

    if direction == 1: # if Шифратор from ответ на direction ==> Вызов функции Шифрования
        print("Результат: ", cipher(language, shift))
        print()
    elif direction == 2: # if Дешифратор from ответ на direction ==> Вызов функции Дешифрования
        print("Результат: ", de_cipher(language, shift))
        print()
    elif direction == 3: # if Дешифратор from ответ на direction ==> Вызов функции Дешифрования без ключа
        de_cipher_nokey(language)
        print()

    while True: # Реализация inf цикла для продолжения работы or выхода из программы
        print("Если хотите выйти нажмите 1")
        cont_or_exit = input("Если хотите продолжить нажмите 2 \n")

        if cont_or_exit.isdigit(): # Обработка ошибок
            ply_choice = int(cont_or_exit)
            if ply_choice == 1:
                print()
                print("Bye :(")
                print()
                print("=" * 100)
                exit()
            elif ply_choice == 2:
                break
            else:
                errors_message()
                continue
        else: # Обработка ошибок
            errors_message()
            continue
