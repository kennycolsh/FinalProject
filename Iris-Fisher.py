#https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis
#Kenny Colsh 10-04-19
import csv
import pandas
import matplotlib.pyplot as plt

def print_dotted_line():
    print('\n','-'*80,'\n')


url = "FisherDS.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pandas.read_csv(url, names=names)
# shape--We can get a quick idea of how many instances (rows) and how many attributes 
# (columns) the data contains with the shape property
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
print( dataset.mean())
print_dotted_line()

print(dataset.sepal-length.groupby([dataset['sepal-length']]).mean().sort_values(ascending=False))