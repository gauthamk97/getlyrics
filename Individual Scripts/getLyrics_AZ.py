#Gets lyrics for a single song from AZLyrics

from bs4 import BeautifulSoup
import urllib, requests, json, os, eyed3

artist = raw_input("Artist name : ")
song = raw_input("Song name : ")

#Using AZLyrics' search to find lyrics page
searchUrl='http://search.azlyrics.com/search.php?q='+artist+'+'+song
searchPage = urllib.urlopen(searchUrl).read()
searchSoup = BeautifulSoup(searchPage, 'html.parser')

#URL of lyrics page
try:
    alltds = searchSoup.find_all('td')
    url = alltds[0].a['href'] #Will invoke Index Error if problem
    for td in alltds:
        if td.has_attr('class'):
            url = td.a['href']
            break
except IndexError:
    print "Couldn't find that song"
    exit()

mainPage = urllib.urlopen(url).read()
soup = BeautifulSoup(mainPage, 'html.parser')

#Finding div that contains the div that contains the lyrics
for div in soup.find_all('div'):
    if div.has_attr('class'):
        if [u'col-xs-12', u'col-lg-8', u'text-center'] == div['class']:
            mainDiv = div
            for div in mainDiv.find_all('div'):
                if not div.has_attr('class'):
                    print div.text
            break


