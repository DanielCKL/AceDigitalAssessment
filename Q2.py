import pandas as pd
from pathlib import Path
import matplotlib, matplotlib.pyplot
import numpy as np
import sys
from sklearn.cluster import KMeans, OPTICS


#Read the data 
filepath=Path('data/palm_ffb.csv')
data=pd.read_csv(filepath,index_col='Date')
#Create a list of columns
cols_list=data.columns.tolist()
np.set_printoptions(threshold=sys.maxsize, suppress=True,linewidth=400)


#First, we should get a general description of the data: 
summary=data.describe().T
print(summary.to_string())

#Then, get the normalized deviations of all the standard deviations to see which has the most significant variations
print("\n",(summary['std']/summary['mean']).sort_values(ascending=False),'\n')

#Next, check the correlations of the output feature (FFB_Yield) to all the other variables
#print(np.corrcoef(np.array(summary)))
correlation_matrix=np.corrcoef(np.array(data).T)
#Create list to hold low, medium, and high correlations
low_correlations=[]
medium_correlations=[]
high_correlations=[]
counter=0


col_idx=len(data.columns)-1 #We only care about the correlation between the output (FBB_Yield) and the other variables
#Loop through the correlation matrix
for row_idx,row in enumerate(correlation_matrix):
    
    value=row[col_idx]
    if value>0.5:
        high_correlations.append('High positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx]) + ' of '+str(value))
    elif value>=0.3:
        medium_correlations.append('Medium positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    elif value >0:
        low_correlations.append('Low positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    elif value>=-0.3:
        low_correlations.append('Low negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    elif value>=-0.5:
        medium_correlations.append('Medium negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    else:
        high_correlations.append('High negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value)+ ' of '+str(value))
counter+=1 #Increment column counter by 1. We only need the lower half of the correlation matrix, as the matrix is symmetrical.

print("The features have the following levels of Spearman correlatedness: \n")
for i in high_correlations: 
    print(i)
for i in medium_correlations: 
    print(i)
for i in low_correlations: 
    print(i)

#Trying again with Kendall correlation
correlation_matrix=np.array(data.corr(method='kendall'))

low_correlations=[]
medium_correlations=[]
high_correlations=[]
counter=0

col_idx=len(data.columns)-1 #We only care about the correlation between the output (FBB_Yield) and the other variables
#Loop through the correlation matrix
print("For Kendall correlation: \n")
for row_idx,row in enumerate(correlation_matrix):
    
    value=row[col_idx]
    if value>0.5:
        high_correlations.append('High positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx]) + ' of '+str(value))
    elif value>=0.3:
        medium_correlations.append('Medium positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    elif value >0:
        low_correlations.append('Low positive correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    elif value>=-0.3:
        low_correlations.append('Low negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    elif value>=-0.5:
        medium_correlations.append('Medium negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value))
    else:
        high_correlations.append('High negative correlation between '+str(cols_list[col_idx]) + ' and '+str(cols_list[row_idx])+ ' of '+str(value)+ ' of '+str(value))
counter+=1 #Increment column counter by 1. We only need the lower half of the correlation matrix, as the matrix is symmetrical.

print("The features have the following levels of Kendall correlatedness: \n")
for i in high_correlations: 
    print(i)
for i in medium_correlations: 
    print(i)
for i in low_correlations: 
    print(i)