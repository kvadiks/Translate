print('Загрузка.')
import os
print('Загрузка..')
import sys
print('Загрузка...')
from time import sleep
sleep(0.5)
print('Загрузка....')
from translate import Translator
print('Загрузка.....')

from translate import Translator

def main():
    translator = Translator(to_lang="ru")
    while True:
        word = input("Введите английское слово для перевода (или 'exit' для выхода): ").strip()
        if word.lower() == 'exit':
            break
        try:
            translation = translator.translate(word)
            print(f"Перевод: {translation}")
        except Exception as e:
            print(f"Ошибка при переводе: {e}")

if __name__ == "__main__":
    main()