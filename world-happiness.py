
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# load data
df2015 = pd.read_csv("2015.csv")
df2016 = pd.read_csv("2016.csv")
df2016.head()


f, ax = plt.subplots(figsize=(9, 6))
corrmat = df2016.corr()
sns.heatmap(corrmat,linewidths=1,annot=True, vmax=.3, square=True)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.savefig("graph1.png")


sns.pairplot(df2016[['Happiness Score','Economy (GDP per Capita)','Family','Health (Life Expectancy)']])
plt.savefig("graph2.png")


f, ax = plt.subplots(figsize=(9, 6))
sns.swarmplot(x="Region", y="Happiness Score",  data=df2016, picker=1)
plt.xticks(rotation=90)

# click to display the country and its hapiness score
def onpick(event):
    country = df2016.iloc[event.ind[0]]['Country']
    score = df2016.iloc[event.ind[0]]['Happiness Score']
    plt.gca().set_title('Happiness score of {} is {}'.format(country, score))
    
plt.gcf().canvas.mpl_connect('pick_event', onpick)
plt.savefig("graph3.png")
