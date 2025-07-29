import pandas as pd
import requests
from bs4 import BeautifulSoup

#QB SCRAPER BELOW
url = 'https://www.nfl.com/stats/player-stats/category/passing/2024/reg/all/passingyards/desc'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

playerStats = []  # list to store individual player stats

# Inspect page source to adjust selectors accordingly
for row in soup.find_all('tr')[1:]:  # tr for header rows
    cols = row.find_all('td')  # td for data rows
    if cols:
        player = cols[0].text.split()
        yards = cols[1].text.split()
        att = cols[2].text.split()
        cmp = cols[3].text.split()
        cmpPercent = cols[4].text.split()
        td = cols[5].text.split()

        #Clean the data
        player = ''.join(player)
        yards = ''.join(yards)
        att = ''.join(att)
        cmp = ''.join(cmp)
        cmpPercent = ''.join(cmpPercent)
        td = ''.join(td)

        #Append the data as a dictionary
        playerStats.append({
            'Position': 'QB',
            'Player': str(player),
            'Yards': float(yards),
            'Attempts': float(att),
            'Completions': int(cmp),
            'CompletionPercent': float(cmpPercent),
            'Touchdowns': float(td)
        })

# Create DataFrame from the list of dictionaries
df = pd.DataFrame(playerStats)

# Save to CSV, setting index to False
df.to_csv('data/nfl_stats.csv', index=False)
