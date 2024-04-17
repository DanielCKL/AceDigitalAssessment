import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mytext="""As a term, data analytics predominantly refers to an assortment of applications, from basic business
intelligence (BI), reporting and online analytical processing (OLAP) to various forms of advanced
analytics. In that sense, it's similar in nature to business analytics, another umbrella term for
approaches to analyzing data -- with the difference that the latter is oriented to business uses, while
data analytics has a broader focus. The expansive view of the term isn't universal, though: In some
cases, people use data analytics specifically to mean advanced analytics, treating BI as a separate
category. Data analytics initiatives can help businesses increase revenues, improve operational
efficiency, optimize marketing campaigns and customer service efforts, respond more quickly to
emerging market trends and gain a competitive edge over rivals -- all with the ultimate goal of
boosting business performance. Depending on the particular application, the data that's analyzed
can consist of either historical records or new information that has been processed for real-time
analytics uses. In addition, it can come from a mix of internal systems and external data sources. At
a high level, data analytics methodologies include exploratory data analysis (EDA), which aims to find
patterns and relationships in data, and confirmatory data analysis (CDA), which applies statistical
techniques to determine whether hypotheses about a data set are true or false. EDA is often
compared to detective work, while CDA is akin to the work of a judge or jury during a court trial -- a
distinction first drawn by statistician John W. Tukey in his 1977 book Exploratory Data Analysis. Data
analytics can also be separated into quantitative data analysis and qualitative data analysis. The
former involves analysis of numerical data with quantifiable variables that can be compared or
measured statistically. The qualitative approach is more interpretive -- it focuses on understanding
the content of non-numerical data like text, images, audio and video, including common phrases,
themes and points of view."""

#Get number of lines of text
text_by_line=mytext.split('\n') 
number_of_lines=len(text_by_line)

#Split text into all lowercase words

text_by_words=mytext.lower().replace(',', ' ').replace('\n', ' ').split(' ')
number_of_instances=text_by_words.count('data')
    
#Probability of data in each line: 
print("\nProbability the word 'data' will appear (case-insensitive search)",number_of_instances/number_of_lines,'\n')



#To get the probability distribution of distinct word count across all lines, we can represent it in a histogram .
print("\nPrinting Graph...\n")
line_word_count=[]
for line in text_by_line: 
    line_word_count.append(len(np.unique(line.split(' '))))


plt.hist(line_word_count,bins=len(line_word_count)+1,alpha=0.5,density=True)
plt.xlabel('Line')
plt.ylabel('Distinct Words')
plt.show()

ax=pd.Series(line_word_count).plot.kde()
plt.show()

print("\nGraphs printed...\n")

#Probability of 'analytics' happening after 'data': 
analytics_incidence=0
for index,item in enumerate(text_by_words): 
    if item=='data':
        if text_by_words[index+1]=='analytics':
            analytics_incidence+=1
        

#   

print('\nProbability of "analytics" happening after "data": =',analytics_incidence/number_of_instances)
print('Note: This is inclusive of "analytics" appearing on the next line, since the question didn\'t specify that they had to be on the same line in this case')

