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
tick_positions = range(1, 6)

# Heights of the bars.  In our case, the average rating for the first movie in the dataset.
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
# Set the x-axis tick positions
ax.set_xticks(tick_positions)
# Set the x-axis tick labels to num_cols and rotate by 90 degrees
ax.set_xticklabels(num_cols, rotation=90)

# Set the x-axis label to "Rating Source"
plt.xlabel("Rating Source")
# Set the y-axis label to "Average Rating"
plt.ylabel("Average Rating")
# Set the plot title
plt.title("Average User Rating For " + norm_reviews["FILM"].iloc[0])


# Plot a horizontal bar graph to compare
bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
# Generate a horizontal bar plot
ax.barh(y=bar_positions, width=bar_widths, height=0.5)
ax.set_yticklabels(num_cols)
ax.set_yticks(tick_positions)
plt.ylabel("Rating Source")
plt.xlabel("Average Rating")
plt.title("Average User Rating For " + norm_reviews["FILM"].iloc[0])

# Create scatter plot to visualizes the relationship between Fandango_Ratingvalue and RT_user_norm columns
fig, ax = plt.subplots()
ax.scatter(norm_reviews["Fandango_Ratingvalue"].values, norm_reviews["RT_user_norm"].values, marker="v")
plt.xlabel("Fandango")
plt.ylabel("Rotten Tomatoes")

# Generate scatter plots to see how Fandango ratings correlate with all 3 of the other review sites
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

df1 = norm_reviews["Fandango_Ratingvalue"].values
df2 = norm_reviews["RT_user_norm"].values
df3 = norm_reviews["Metacritic_user_nom"].values
df4 = norm_reviews["IMDB_norm"].values

ax1.scatter(df1, df2)
ax2.scatter(df1, df3)
ax3.scatter(df1, df4)

plt.xlabel("Fandango_Ratingvalue")
ax1.set(xlabel="Fandango_Ratingvalue", ylabel="RT_user_norm")
ax2.set(xlabel="Fandango_Ratingvalue", ylabel="Metacritic_user_nom")
ax3.set(xlabel="Fandango_Ratingvalue", ylabel="IMDB_norm")

# From the scatter plots, we can conclude that user ratings from IMDB and Fandango are the most similar.
# Also, ratings from Metacritic and Rotten Tomatoes have positive but weak correlation with ratings from Fandango.

# Generate histograms using 20 bins for all four columns.
# Ensure that the scales for the y-axis are the same for all histograms
fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews['Fandango_Ratingvalue'], bins=20, range=(0, 5))
ax1.set_title("Distribution of Fandango Ratings")
ax2.hist(norm_reviews['RT_user_norm'], bins=20, range=(0, 5))
ax2.set_title("Distribution of Rotten Tomatoes Ratings")
ax3.hist(norm_reviews['Metacritic_user_nom'], bins=20, range=(0, 5))
ax3.set_title("Distribution of Metacritic Ratings")
ax4.hist(norm_reviews['IMDB_norm'], bins=20, range=(0, 5))
ax4.set_title("Distribution of IMDB Ratings"        )

ax1.set_ylim(0,50)
ax2.set_ylim(0,50)
ax3.set_ylim(0,50)
ax4.set_ylim(0,50)


# Generate a box plot containing a box-and-whisker diagram for the following columns
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_ylim(0,5)
ax.set_xticklabels(num_cols, rotation=90)

plt.show()
