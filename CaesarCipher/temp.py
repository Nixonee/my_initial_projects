eng = [
    [chr(i) for i in range(65, 91)],   # заглавные A-Z
    [chr(i) for i in range(97, 123)]   # прописные a-z
]
rus = [
    [chr(i) for i in range(1040, 1072)],  # заглавные А-Я
    [chr(i) for i in range(1072, 1104)]   # прописные а-я
]




text1 = input().split()
print(text1)
im = ""

def cipherr(language, shift, text): # Функция шифрования
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

cnt = 0

for i in range(len(text1)):
    for j in text1[i]:
        if j.isalpha():
            cnt += 1
    shift = cnt
    cnt = 0
    im += cipherr("en", shift, text1[i]) + " "

print(im)
