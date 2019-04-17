#https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis
#Kenny Colsh 10-04-19
#import the required library
import csv
import pandas as pd
import matplotlib.pyplot as pl
import sys

#create a dotted line seperator for visual effect
def print_dotted_line():
    print('\n','-'*80,'\n')


print(f"This script is called {sys.argv[0]}.\n")


if len(sys.argv) !=2:
    print("You should select a number between 1 and 5")
else:
    #import the csv and read in to panda
    url = "FisherDS.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
    dataset = pd.read_csv(url, names=names)

    if sys.argv[1] == '1':
        print("MEAN")#get the mean of each column
        print(dataset.mean())
        print_dotted_line()

    if sys.argv[1] == '2':
        print("MAX")#print the max of all the columns
        print(dataset.max())
        print_dotted_line()

    if sys.argv[1] == '3':
        print("MIN")#print the MIN of all the columns
        print(dataset.min())
        print_dotted_line()

    if sys.argv[1] == '4':
        print("Rows and Columns")
        print(dataset.shape)# shape--We can get a quick idea of how many instances (rows) and how many attributes 
        print_dotted_line()# (columns) the data contains with the shape property
    
    if sys.argv[1] == '5':
        print("Histogram")
        dataset.hist()
        pl.show()
        print_dotted_line()

    if sys.argv[1] == '6':
        print("Group and the mean of petal-length")
        grouped = dataset.groupby(['species'])
        print(grouped['petal-length'].mean().sort_values(ascending=False))

        print("Group and the mean of petal-width")
        print(grouped['petal-width'].mean().sort_values(ascending=False))
        #plot the graph and create the label
        pl.plot(grouped['petal-length'].mean(), label="P-Length", linestyle='--')
        pl.plot(grouped['petal-width'].mean(), label="p-Width", linestyle='--')
        #give it grid lines
        pl.grid()
        #add legends to make it more readable
        pl.legend( loc=4)
        #give the graph a title
        pl.title('petal-length by class')
        #show the Plot
        pl.show()
      





