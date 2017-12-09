from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

webpage = urlopen('https://www.apple.com/itunes/charts/songs/')
data = webpage.read()

soup = BeautifulSoup(data, 'html.parser')
div = soup.find('div','main')
print(div)
ul = div.find('ul')
print(ul)
li_list = ul.find_all('li')
print(li_list)
import pyexcel

new_list = []

for li in li_list:
    name = li.h3.a
    artist = li.h4.a
    songs = {
        'title': name.string,
        'artist': artist.string
    }
    print(songs['title'], songs['artist'], sep = ' ')
    new_list.append(songs)
    options ={
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([songs['title'] + songs['artist']])
# pyexcel.save_as(records = new_list, dest_file_name = 'ituneschart.xlsx')
