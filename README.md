# Web Scraper for Wikipedia List

This project is a web scraper that extracts data from a Wikipedia list and converts it into a CSV file. The scraper is designed to handle tables from Wikipedia pages and save the results into a CSV format for further analysis or use.

## How to Use the Project

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate the project dependencies:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

- **On Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **On macOS and Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install the Requirements

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Running the Scraper

You have two options to run the scraper:

#### Option 1: Run with Jupyter Notebook

If you prefer to work with Jupyter Notebook, open the `scraping.ipynb` file:

```bash
jupyter notebook scraping.ipynb
```

This will open the notebook in your browser, where you can execute the cells to run the scraper.

#### Option 2: Run with Python Script

If you prefer to run the scraper directly as a Python script, use the following command:

```bash
python main.py
```

After running the script, you'll be prompted to insert the URL of the Wikipedia page. The scraper will then generate the required CSV file for you.

### 5. Output

The output of the scraper will be saved as a CSV file in the project directory. The name of the file will be `filename.csv`, which you can find in the `WEBCRAWLER` folder.

## Conclusion

This project provides a simple yet powerful tool to scrape data from Wikipedia lists. You can customize it further to handle different types of tables or other sources. Feel free to contribute or modify the code to suit your needs!
