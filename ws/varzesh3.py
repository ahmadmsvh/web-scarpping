import pandas as pd
import requests
import html5lib
from bs4 import  BeautifulSoup

url = 'https://www.varzesh3.com/'

response = requests.get(url)

bs = BeautifulSoup(response.text, 'html5lib')

standing_table_list = []

standing_table = bs.select('table.league-standing.widget-standing')[0].select('tbody')[0].select('tr')

for record in standing_table:
   standing_table_list.append([record.select('td')[i].text for i in range(len(record.select('td')))])

league_table = pd.DataFrame(standing_table_list,
                            columns=['رتبه','تیم','بازی','امتیاز'],
                            index=None
                            )
league_table.to_excel('./excel/league_table.xlsx', engine='xlsxwriter')



