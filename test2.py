import googletrans
from time import sleep
print('These are the language and the code words (choose any one and enter the code word) : ',googletrans.LANGUAGES)
sleep(5)
c = input('Enter the code word: ')
sleep(5)
b = input('Enter the text(in english): ')
print('Processing...')
sleep(5)
translator = googletrans.Translator()
translated = translator.translate( b, dest= c )
print(translated.text)

#print(googletrans.LANGUAGES)
