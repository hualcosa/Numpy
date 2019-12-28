import codecademylib
import numpy as np


# Load the data from the file and save it as calorie_stats
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

# How much higher is the average calorie count of your competition?
# Save the answer to the variable average_calories

average_calories = np.mean(calorie_stats)
print(average_calories)

# Does the average calorie count adequately reflect the distribution of the dataset?
# Sort the data and save the result to the variable calorie_stats_sorted
calorie_stats_sorted = np.sort(calorie_stats)
#print(calorie_stats_sorted)

# Let’s see if the median is a better representative of the dataset.
# Calculate the median of the dataset and save your answer to median_calories
median_calories = np.median(calorie_stats)
#print(median_calories)

# find the lowest percentile that is greater than 60 calories
nth_percentile = np.percentile(calorie_stats, 4)
#print(nth_percentile)

# let’s calculate the percentage of cereals that have more than 60 calories per serving. Save your answer to the variable more_calories
more_calories = np.mean(calorie_stats > 60)
#print(more_calories)

# Calculate the amount of variation by finding the standard deviation
calorie_std = np.std(calorie_stats)
print(calorie_std)

#Can we make the generalization that most cereals have around 100 calories or is the spread even greater?
q1 = np.percentile(calorie_stats, 25)
q3 = np.percentile(calorie_stats, 75)
interquartile_range = q3 - q1
print(interquartile_range)

# As the median is 110 and the interquartile range are 10, we can say tha most cereal have between 100 and 120 calories