#https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis
#Kenny Colsh 10-04-19
import csv
import pandas
import matplotlib.pyplot as plt
url = "FisherDS.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pandas.read_csv(url, names=names)
# shape--We can get a quick idea of how many instances (rows) and how many attributes 
# (columns) the data contains with the shape property
print(dataset.shape)

	
# descriptions This includes the count, mean,
# the min and max values as well as some percentiles.
print(dataset.describe())

# species distribution
print(dataset.groupby('species').size()

# histograms
dataset.hist()
plt.show()