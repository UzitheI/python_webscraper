from scraping import scrape_table

if __name__ == "__main__":

    url = input("Please enter the Wikipedia URL: ")
    

    df = scrape_table(url)
    

    print(df)
    

    df.to_csv('filename.csv', index=False)
