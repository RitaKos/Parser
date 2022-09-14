from bs4 import BeautifulSoup
import urllib.request

# создаем запрос
request = urllib.request.urlopen('PUT_LINK')
# получаем ответ в html
html = request.read()
# приводим его к виду для поиска
soup = BeautifulSoup(html, 'html.parser')
# начинаем поиск по html
news = soup.find_all('tag_name', class_='class_name')

# достаем значения нужных атрибутов и записываем в лист
results=[]
for item in news:
    web='head_link'
    play = item.a.get('title')
    if play :
        link = web + item.a.get('href')
        results.append({
            'play_name' : play,
            'link' : link
        }
        )

# создаем файл для записи

file = open('file_name', mode='w', encoding='UTF-8')
for match in results:
    file.write(f'{match["play_name"]}\nПодобнее о матче: {match["link"]}\n\n')
file.close()

# открываем файл для чтения
file = open('champ_football_2022', mode='r', encoding='UTF-8')
what_we_have=file.read()
file.close()
# выводим прочитанную информацию
print(what_we_have)


