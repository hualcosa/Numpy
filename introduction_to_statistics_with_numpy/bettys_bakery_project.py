# This was a project to the 'Introduction to Numpy' course 
# i've done in Codecademy. It explores basics numpy concepts
import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
recipes = np.genfromtxt('recipes.csv', delimiter=',')

print(recipes)

eggs = recipes[:, 2]
#print(eggs)
one_egg = (eggs == 1)
cookies = recipes[2, :]
#print(cookies)
double_batch = cupcakes * 2
#print(double_batch)
grocery_list = double_batch + cookies
#print(grocery_list)
