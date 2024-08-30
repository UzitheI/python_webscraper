import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_table(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find_all('table')[1]
    

    world_titles = table.find_all('th')
    world_table_titles = [title.text.strip() for title in world_titles]


    df = pd.DataFrame(columns=world_table_titles)


    column_data = table.find_all('tr')


    for row in column_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]

        # Check if the number of elements matches the number of columns
        if len(individual_row_data) == len(df.columns):
            length = len(df)
            df.loc[length] = individual_row_data
        else:
            print(f"Skipping row due to mismatch in columns: {individual_row_data}")

    return df
