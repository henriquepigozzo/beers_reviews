# beers_reviews

Here you'll find a basic Exploratory Data Analysis (EDA) projet built for learning purpose.

The dataset used is about beers and breweries reviews posted online by users at beeradvocate.com and uploated to Kaggle. The full dataset can be found following this path https://www.kaggle.com/ehallmar/beers-breweries-and-beer-reviews?select=beers.csv.

Steps taken:

- Three entities were mapped from the dataset (Beers, Breweries and Reviews);
- A relational database was built on a Postgres local server with Python (psycopg library);
- A chunk of the original dataset was sliced from the original dataset and uploaded to the database with Python (psycopg library);
- The data was queryed from the database to a Jupyer Notebook with Python;
- EDA took place using basically Pandas as Matplotlib.
