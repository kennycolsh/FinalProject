#https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis
#Kenny Colsh 10-04-19
#import the required library
import csv
import pandas as pd
import matplotlib.pyplot as plt

#create a dotted line seperator for visual effect
def print_dotted_line():
    print('\n','-'*80,'\n')

#import the csv and read in to panda
url = "FisherDS.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pd.read_csv(url, names=names)

#get the mean of each column
print(dataset.mean())
print_dotted_line()
print(dataset.max())

# shape--We can get a quick idea of how many instances (rows) and how many attributes 
# (columns) the data contains with the shape property
print_dotted_line()
print(dataset.shape)


print_dotted_line()
# descriptions This includes the count, mean,
# the min and max values as well as some percentiles.
print(dataset.describe())
print_dotted_line()
# species distribution
print(dataset.groupby('species').size())
print_dotted_line()
# histograms
#dataset.hist()
#plt.show()


#Mean the whole dataset:
#print( dataset.mean())
print_dotted_line()

#print(dataset.sepal-length.groupby([dataset['sepal-length']]).mean().sort_values(ascending=False))