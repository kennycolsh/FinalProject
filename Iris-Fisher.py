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
print("MEAN")
print(dataset.mean())

print_dotted_line()

#print the max of all the columns
print("MAX")
print(dataset.max())

print_dotted_line()

#print the MIN of all the columns
print("MIN")
print(dataset.min())

# shape--We can get a quick idea of how many instances (rows) and how many attributes 
# (columns) the data contains with the shape property
print_dotted_line()
print(dataset.shape)





# histograms
dataset.hist()
plt.show()

print_dotted_line()

