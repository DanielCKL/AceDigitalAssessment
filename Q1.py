import pandas as pd
from pathlib import Path
import matplotlib, matplotlib.pyplot
import numpy as np
import sys
from sklearn.cluster import KMeans, OPTICS


#Read the data 
filepath=Path('data/ingredient.csv')
data=pd.read_csv(filepath)
#Create a list of columns
cols_list=data.columns.tolist()

#Set the print options
np.set_printoptions(threshold=sys.maxsize, suppress=True,linewidth=400)


#Get correlation coefficient
correlation_matrix=np.corrcoef(np.array(data).T)
counter=0

#Create list to hold low, medium, and high correlations
low_correlations=[]
medium_correlations=[]
high_correlations=[]

#Loop through the correlation matrix
for row_idx,row in enumerate(correlation_matrix):
    for col_idx in range(0,counter):
        value=row[col_idx]
        if value>0.5:
            high_correlations.append('High positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx]) + ' of '+str(value))
        elif value>=0.3:
            medium_correlations.append('Medium positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx]))
        elif value >0:
            low_correlations.append('Low positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx]))
        elif value>=-0.3:
            low_correlations.append('Low negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx]))
        elif value>=-0.5:
            medium_correlations.append('Medium negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx]))
        else:
            high_correlations.append('High negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    counter+=1 #Increment column counter by 1. We only need the lower half of the correlation matrix, as the matrix is symmetrical.

print("The additives have the following levels of correlatedness: \n")
for i in high_correlations: 
    print(i)
for i in medium_correlations: 
    print(i)
for i in low_correlations: 
    print(i)
    



    

#Get description of data 
summary=data.describe().T

normalized_sdev=(summary['std']/summary['mean']).sort_values(ascending=False)
print('\nNormalized standard deviation scores=\n\n',normalized_sdev)


#Plot histogram and kde line graphs
data.hist(bins=20)
matplotlib.pyplot.show()

figure,axis=matplotlib.pyplot.subplots(3,3)
axis=axis.ravel()
for idx,column in enumerate(data.columns):
    data[column].plot.kde(title=column ,ax=axis[idx])

matplotlib.pyplot.show()


#K-Means graph
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

matplotlib.pyplot.plot(range(1,11), inertias, marker='o')
matplotlib.pyplot.title('K-Means method')
matplotlib.pyplot.xlabel('No. of clusters')
matplotlib.pyplot.ylabel('Inertia')
matplotlib.pyplot.show()


#Use OPTICS to predict the number of clusters
clustering=OPTICS(
                  min_samples=10        #10 chosen becuase it is the number of features (9)+1
                  ).fit(data)
#print("Number of clusters according to DBScan is: ",clustering.labels_)
print('Cluster labels according to OPTICS are:', np.unique(clustering.labels_))
print('Note that noisy samples are assigned a value of -1')