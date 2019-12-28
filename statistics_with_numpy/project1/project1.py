# coding: UTF-8

# You're part of an impartial research group that conducts phone surveys
# prior to local elections. During this election season, the group
# conducted a survey to determine how many people would vote for Cynthia
# Ceballos vs. Justin Kerrigan in the mayoral election.
# Now that the election has occurred, your group wants to compare the
# survey responses to the actual results.
# Was your survey a good indicator? Let’s find out!

import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# Converting the dataset into a numpy array
survey_responses = np.array(survey_responses)

# Calculate the number of people who answered ‘Ceballos’ and save the
# answer to the variable total_ceballos.
total_ceballos = np.sum(survey_responses == 'Ceballos')
print("Number of votes candidate Ceballos received: " + str(total_ceballos))

# Calculate the percentage of people in the survey who voted for Ceballos
# and save it to the variable percentage_ceballos.
total_ceballos_array = (survey_responses == 'Ceballos')
percentage_ceballos = np.mean(total_ceballos_array)
print("Percentage of votes for candidate Ceballos(poll results): " + str(percentage_ceballos))

# In the real election, 54% of the 10,000 town population voted for
# Cynthia Ceballos. Your supervisors are concerned because this is a very
# different outcome than what the poll predicted. They want you to 
# determine if there is something wrong with the poll or if given the
# sample size, it was an entirely reasonable result.

# Generate a binomial distribution that takes the number of total survey
# responses, the actual success rate, and the size of the town’s
# population as its parameters. Then divide the distribution by the number
# of survey responses. Save your calculation to the variable possible_surveys.
number_survey_responses = len(survey_responses)

possible_surveys = np.random.binomial(number_survey_responses, 0.54,10000)/float(number_survey_responses)
#print(possible_surveys)

# Plot a histogram of possible_surveys with a range of 0-1 and 20 bins.
plt.hist(possible_surveys, bins=20, range=(0,1))
plt.title('Probabilities of vote for Cyntia Ceballos')
plt.xlabel('Probabilites')
plt.ylabel('Number of samples')
plt.show()

# Calculate the percentage of surveys that could have an outcome of Ceballos receiving # less than 50% of the vote and save it to the variable ceballos_loss_surveys.
ceballos_loss_surveys = np.mean(possible_surveys < 0.50)
print('Percentage of surveys in which ceballos received less than 50% of the vote: {}'.format(ceballos_loss_surveys))

# Your co-worker points out that your poll would be more accurate if it had more responders.
# Generate another binomial distribution, but this time, see what would happen if you
# had instead surveyed 7,000 people. Divide the distribution by the size of the survey
# and save your findings to large_survey.

large_survey = np.random.binomial(7000, 0.54,10000)/float(7000)
print(large_survey)
ceballos_loss_new = np.mean(large_survey < 0.50)
print('Percentage of surveys in which ceballos received less than 50% of the vote for larger surveys: {}%'.format(ceballos_loss_new))
