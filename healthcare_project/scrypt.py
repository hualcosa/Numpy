import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
#print(healthcare.head())

# captures the all the unique elements with a certain DRG definition.
print(healthcare["DRG Definition"].unique())

# captures only patients with chest pain.
chest_pain = healthcare[healthcare["DRG Definition"] == "313 - CHEST PAIN"]

# gets every chest pain diagnosis in Alabama.
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == 'AL']

# gets average covered charges for chest pain.
costs = alabama_chest_pain[' Average Covered Charges ']. values

# makes a boxplot with the array of costs.
#plt.boxplot(costs)
#plt.show() 

# find and store every state where people have chest pain.
# we could with list comprehemsion with the following code:
# states = []
# states = [provider for provider in chest_pain['Provider State'] if provider not in states]
# But Pandas dataframe has a much shorter way to do it 
states = chest_pain['Provider State'].unique()

# separate the dataser into a dataset for each state.
datasets = []
for state in states:
    datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges ']. values)

# plotting a boxplot for each state
plt.figure(figsize=(20,6))
plt.boxplot(datasets, labels=states)
plt.show()