import pandas
import numpy as np
import matplotlib.pyplot as plt

df = pandas.read_csv('../dirtyHeart.csv')
df = pandas.DataFrame(df)

fontMean = {'color':  'darkred',
        'size': 10,
        }
fontMedian = {'color':  'green',
        'size': 10,
        }


CONTINUOUS_HEADERS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
trimLen = int(len(df)*.02)

for col in CONTINUOUS_HEADERS:
    c = df[col].sort_values()
    c = c.iloc[trimLen:-trimLen]
    bins = len(c.unique())
    plt.ylabel('Frequency')
    plt.xlabel(col)
    y,x,patches = plt.hist(c, bins, edgecolor='black')
    plt.axvline(c.mean(), color='darkred', linestyle='dashed', linewidth=2)
    plt.text(c.mean()*1.1, plt.ylim()[1]*0.9, 'Mean: {:.2f}'.format(c.mean()), fontdict=fontMean)
    plt.axvline(c.median(), color='green', linestyle='dashed', linewidth=2)
    plt.text(c.median(), plt.ylim()[1]*0.8, 'Median: {}'.format(c.median()), fontdict=fontMedian)
    yVals = y.tolist()
    patches[yVals.index(max(yVals))].set_color('y')
    plt.show()
