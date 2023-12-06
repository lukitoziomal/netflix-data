# Netflix movies and shows notebook
### In the file ` netflix.ipynb ` you'll find data frame containing these columns:
* **title**
* **type**: MOVIE or SHOW
* **release_year**: original release year, not release on Netflix platform
* **runtime**
* **genres**: multiple values
* **production_countries**: multiple values
* **seasons**: NaN for movies
* **imdb_score**: average IMDB rating
* **imdb_votes**: amount of IMDB votes
* **original**: boolean value 

### Data analytics is categorized and split into these sections:
* **Movies vs Shows distribution**
* **Shows vs movies genres distribution**
* **Statistics about duration and rating**
* **Top 3 original movies and shows**
* **Original productions since launch**
* **Regional statistics**
* **Average rating by region**

#
Initial dataset containing over 6000 movies and shows taken from Kaggle:
https://www.kaggle.com/datasets/dgoenrique/netflix-movies-and-tv-shows/data

Original movies and shows scraped off Wikipedia, source code is in file ` scraper.py `
