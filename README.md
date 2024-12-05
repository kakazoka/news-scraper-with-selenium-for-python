# News Scraper with Selenium for Python
This automation uses Selenium for Python to scrape the latest game news from Metacritic.

## Features
- Scrapes the latest game news from Metacritic
- Extracts the title, description and link to each article
- Saves the data to a .csv file and stores it in a specified path

## Requirements
- [csv](https://docs.python.org/3/library/csv.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [os](https://docs.python.org/3/library/os.html)
- [Selenium](https://www.selenium.dev/)

## Dependencies
1. Install the required Python package using `pip`:
```bash
pip install selenium
```
2. Download and install the appropriate WebDriver for your browser:
- [Firefox](https://github.com/mozilla/geckodriver)
- [Google Chrome](https://googlechromelabs.github.io/chrome-for-testing/)
- [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)

## How to Use
1. Clone or download the repository to your local machine
2. Open the script file `main.py`
3. Modify the `service` path with the path of the WebDriver for your browser
4. Modify the `save_path` with the path of the folder where the .csv will be stored
5. Run the script

## Script Overview
1. Initializes a Selenium WebDriver
2. Opens the [Metacritic Games](https://www.metacritic.com/game/) page
3. Scrapes the title, description and link to each article
4. Saves the data in a structured format to a .csv file with the date the data was scrapped in the filename
