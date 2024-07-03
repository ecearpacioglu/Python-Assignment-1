from deep_translator import (GoogleTranslator)

lang_dict = {"İngilizce": "en", "Türkçe": "tr", "Almanca": "de", "English": "en", "Turkish": "tr", "German": "de"}

while 1 == 1:
    translateLangToControl = input('Hangi dile çeviri yapmak istiyorsun: ')

    translateLangToControl = GoogleTranslator(source='auto', target='tr').translate(text=translateLangToControl)

    while translateLangToControl not in lang_dict.keys():
        translateLangToControl = input('Hatalı giriş yaptınız. Tekrar deneyin! Hangi dile çeviri yapmak istiyorsun: ')
        translateLangToControl = GoogleTranslator(source='auto', target='tr').translate(text=translateLangToControl)

    translateLangTo = lang_dict.get(translateLangToControl)
    print(f'Girdiğiniz Dil: {translateLangTo}')

    translateTextFrom = input('Çevirmek istediğin cümle: ')

    translateTextTo = GoogleTranslator(source='auto', target=translateLangTo).translate(text=translateTextFrom)

    print(translateTextTo)

    exit_control = input('Devam etmek için Enter\'a basmanız, çıkış yapmak için \'esc\' yazıp Enter\'a basmanız gerekmektedir: ')

    if exit_control == "esc":
        break
    else:
        continue