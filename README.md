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

### Example of Output
| Title                                          | Description                                                                                                                                                                                                                                                        | Link                                                                            |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 2024 Video Game Awards Tracker                 | Here are the games released during 2024 that have won major industry awards or received nominations for those awards. We'll update our awards tracker whenever new awards and nominations are announced.                                                           | https://www.metacritic.com/news/2024-game-of-the-year-awards-tracker/           |
| Reviews for Sony's PlayStation 5 Pro Console   | Sony's newest version of the PlayStation 5 console is a "Pro" model that promises greatly improved visuals thanks to hardware and software enhancements. But do the improvements justify its nearly $700 cost? Find out what critics are saying about the PS5 Pro. | https://www.metacritic.com/news/playstation-5-pro-console-review-roundup/       |
| The 20 Best Original Games of the 21st Century | We rank the highest-scoring "original" games (that aren't sequels or remakes or based on existing IP) released since January 1, 2000.                                                                                                                              | https://www.metacritic.com/pictures/best-original-games-of-the-21st-century/    |
| Every Silent Hill Game, Ranked                 | We rank every video game in Konami's Silent Hill franchise from worst to best by Metascore.                                                                                                                                                                        | https://www.metacritic.com/pictures/ever-silent-hill-game-ranked-worst-to-best/ |
| Every Metacritic Game of the Year Winner       | These are the best-reviewed games released each year in the 21st century.                                                                                                                                                                                          | https://www.metacritic.com/pictures/every-metacritic-game-of-the-year-winner/   |
