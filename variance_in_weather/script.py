import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

'''
the dataset that was stored in weather_data is missing but i can explain you what it contained kkk.
It had about 40000 Londom weather informations for a specific time.
'''

#print(london_data.head())
#print(len(london_data))
#print(type(london_data))
temp = london_data['TemperatureC']

average_temp = np.average(temp)
print(average_temp)

temperature_var = np.var(temp)
print(temperature_var)

temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

june = london_data.loc[london_data['month'] == 6]['TemperatureC']
july = london_data.loc[london_data['month'] == 7]['TemperatureC']

june_mean = np.mean(june)
july_mean = np.mean(july)

print('The average temperature in London in june and july is respectively:\n{:.4}\n{:.4}'.format(june_mean, july_mean))

june_std = np.std(june)
july_std = np.std(july)

print('The standard deviation for the temperature in London in june and july is respectively:\n{:.4}\n{:.4}'.format(june_std, july_std))

#same procedure to all months:
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")

