from googletrans import Translator

translator = Translator()


def translation(text, language):
    return translator.translate(text, dest=language)


translation_text_one = translation('Texto de prueba de la traduccion!', 'en')
print(translation_text_one.text)

translation_text_two = translation('안녕하세요.', 'en')
print(translation_text_two.text)
