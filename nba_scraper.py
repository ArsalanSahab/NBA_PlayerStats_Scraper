from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd



# Year to Focus

year = 2020


# URL

url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

# Convert to HTML

_html = urlopen(url)


# Convert to Soup Object

soup = BeautifulSoup(_html, 'html.parser')

# Get Columns

soup.findAll('tr', limit=2)

# Get Header Text

header_text = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
header_text = header_text[1:]

# Get Data from Rows

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]for i in range(len(rows))]


# Examining in Pandas 

df = pd.DataFrame(player_stats, columns= header_text)


if __name__ == "__main__" :
    
    print(df.head())