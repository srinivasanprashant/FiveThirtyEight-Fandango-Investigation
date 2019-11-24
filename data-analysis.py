import pandas as pd

# Read fandango_scores.csv into a Dataframe named reviews.
reviews = pd.read_csv("fandango_scores.csv")
# Select certain columns and assign the resulting Dataframe to norm_reviews
norm_reviews = reviews[["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]]
print(norm_reviews.iloc[0])

