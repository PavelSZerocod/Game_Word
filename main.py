import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words" : english_words,
            "word_definition" : word_definition
        }
    except:
        print("Произошла ошибка!")

def translate_to_russian(text):
    translator = Translator()
    try:
        translation = translator.translate(text, dest='ru')
        return translation.text
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        translated_word = translate_to_russian(word)
        translated_definition = translate_to_russian(word_definition)

        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")
        if user.lower() == translated_word.lower():
            print("Ответ верный!")
        else:
            print(f"Ответ не верный, верный ответ - {translated_word}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()

