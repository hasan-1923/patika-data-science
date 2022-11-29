import pandas as pd
import matplotlib as plt 
import numpy as np 


veriler  = pd.read_csv('Covid-19_Tests.csv')
    

print(veriler.head())

print(veriler.info())
print(veriler.hist(bins= 100, figsize=(5,5)))
plt.pyplot.show()

