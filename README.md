# Analyzing Latin American QAnon Telegram group chats

This repository has data and analysis supporting my Columbia Journalism School thesis project: "Latin Americanization of QAnon: Why and how is the US conspiracy theory thriving in South American countries?" 
The project was completed on August 11, 2021. 

## Data

The analysis explores data from Latin American QAnon Telegram group chats. Using the Telegram Lite application, I downloaded hundreds of html files containing the messages shared on those groups. I scraped the files using Beautiful Soup Python Library and created a database for each country: Venezuela, Argentina, Colombia, Uruguay, Peru, Mexico and Chile. The databases include the day and time the messages were sent, username and text of the message. 

## Analysis
I used natural language processing to evaluate the most common words used in the chats. I installed the count vectorization package from the scikit-learn free machine learning library and looked at term frequency. I customized the count vectorizer with Natural Language Toolkit. I eliminated the Spanish stop words,removed punctuation marks and converted all the words into lowercase. 

To analyze when most of the users joined the chat, what users participated the most and the time frame when most of the messages were sent, I used Pandas built-in functions. I also included regular expressions to evaluate where most forwarded messages came from and to analyze the urls and domains shared on the group chat. 
I used Term Frequency Inverse Document Frequency from scikit-learn to apply K-means. In other words, I used an unsupervised learning algorithm to identify similar groups or clusters of data points within the data. My intention was to summarize the large amounts of text and uncover useful insights by looking at the top terms per cluster.

Finally, I used the Spacy library to recognize the entities mentioned in the text messages and divided the search results by persons, locations, organizations and miscellaneous. For it to work, I increased the maximum number of characters Spacy can handle according to each dataset. 
The repository contains the following:

## Files:
- `PATRIOTAS por la VERDAD!_2021-07-16`, which includes the messages of the [Uruguayan Telegram chat](https://t.me/joinchat/R2Cm5nxDIA7FFMr7) in `.html` format. The code I used to scrape those files is in  `uruguay.py`, and the data analysis can be found in the notebook `Uruguay.ipynb`

- `Q ANON CHILE_2021-07-16`, which includes the messages of the [Chilean Telegram chat](https://t.me/QANONSCHILE) in `.html` format. The code I used to scrape those files is in `chile.py`, and the data analysis can be found in the notebook `Chile.ipynb`

- `Q AnonPeru_2021-05-07`, which includes the messages of the [Peruvian Telegram chat](https://t.me/movimientoqanonperu) in `.html` format. The code I used to scrape those files is in `peru.py`, and the data analysis can be found in the notebook `Peru.ipynb`

- `Q-Anons Colombia 🇨🇴 Dark to Light_2021-07-16`, which includes the messages of the [Colombian Telegram chat](https://t.me/QAnonsColombia) in `.html` format. The code I used to scrape those files is in `colombia.py`, and the data analysis can be found in the notebook `Colombia.ipynb`

- `QAnon Argentina_2021-07-16`, which includes the messages of the [Argentinean Telegram chat](https://t.me/QanonArgentinaDiosyPatria) in `.html` format. The code I used to scrape those files is in `argentina.py`, and the data analysis can be found in the notebook `Argentina.ipynb`

- `Qanon México_2021-07-16`, which includes the messages of the [Mexican Telegram chat](https://t.me/Qanonmexico) in `.html` format. The code I used to scrape those files is in `mexico.py`, and the data analysis can be found in the notebook `Mexico.ipynb`

- `Activity`, which includes the `.csv’s` files with the number of messages sent per day in each Telegram group chat, and an analysis of the Telegram activity can be found in `activity.ipynb`

- `Joined`, which includes the `.csv’s` files with the number of users who joined per day in each Telegram group chat, and an analysis can be found in `joined.ipynb`

## Contact
If you have any questions about this repository, you can reach out to biancapallaro@gmail.com 
