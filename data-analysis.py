import pandas as pd
import matplotlib.pyplot as plt
# Positions of the left sides of the 5 bars. [0.75, 1.75, 2.75, 3.75, 4.75]
from numpy import arange


# Read fandango_scores.csv into a Dataframe named reviews.
reviews = pd.read_csv("fandango_scores.csv")
# Select certain columns and assign the resulting Dataframe to norm_reviews
norm_reviews = reviews[["FILM", "RT_user_norm", "Metacritic_user_nom", "IMDB_norm", "Fandango_Ratingvalue", "Fandango_Stars"]]
print(norm_reviews.iloc[0])

bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

# Heights of the bars.  In our case, the average rating for the first movie in the dataset.
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights)
# Set the x-axis tick positions
ax.set_xticks(tick_positions)
# Set the x-axis tick labels to num_cols and rotate by 90 degrees
ax.set_xticklabels(num_cols, rotation=90)

# Set the x-axis label to "Rating Source"
plt.xlabel("Rating Source")
# Set the y-axis label to "Average Rating"
plt.ylabel("Average Rating")
# Set the plot title
plt.title("Average User Rating For Avengers: Age of Ultron (2015)")

plt.show()
