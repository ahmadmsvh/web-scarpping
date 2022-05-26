import requests
from bs4 import BeautifulSoup
import html5lib.treeadapters.sax
import lxml

url = 'https://www.daneshjooyar.com/'

response = requests.get(url)
bs = BeautifulSoup(response.text, 'html5lib')
categories_tag = bs.select('div.catlist')

cat_urls = categories_tag[0].findAll('a')
categories = []
for a in cat_urls:
   categories.append(a['href'])


for cat in categories:
   url = 'https://www.daneshjooyar.com/'+cat
   cat_name = cat.split('/')[2]

   response = requests.get(url)

   bs = BeautifulSoup(response.text, 'html5lib')
   page_numbers_ul = bs.select('ul.page-numbers')

   tags = page_numbers_ul[0].findAll('li')
   last_page_tag = tags[len(tags) - 2]
   number = last_page_tag.find('a').text
   number_of_pages = int(number)

   titles = []
   urls = []

   for page in range(1, number_of_pages + 1):
      response = requests.get(url, params={'page':'{}'.format(page)})
      bs = BeautifulSoup(response.text,'html5lib')

      courses = bs.select('div.course-area')
      courses = courses[0].select('div.course-filter-list')
      courses = courses[0].findAll('a')

      for a_tag in courses:
         title = a_tag.select('h2')[0].text
         titles.append(title)
         urls.append(a_tag['href'])

   my_doc = ''
   for i in range(len(urls)):
      my_doc += '<a href={}> <h2>{}</h2></a> \n'.format(urls[i], titles[i])


   with open('./files/{}.html'.format(cat_name), 'w') as f:
      f.write(my_doc)




