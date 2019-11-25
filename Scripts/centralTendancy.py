import pandas
import numpy as np
import matplotlib.pyplot as plt
import collections
import operator

df = pandas.read_csv('../dirtyHeart.csv')
df = pandas.DataFrame(df)

fontMean = {'color':  'darkred',
        'size': 10,
        }
fontMedian = {'color':  'green',
        'size': 10,
        }


CATEGORICAL_HEADERS = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal', 'target']
CONTINUOUS_HEADERS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']

# for col in CONTINUOUS_HEADERS:
#     bins = len(df[col].unique())
#     plt.ylabel('Frequency')
#     plt.xlabel(col)
#     y,x,patches = plt.hist(df[col], bins, edgecolor='black')
#     plt.axvline(df[col].mean(), color='darkred', linestyle='dashed', linewidth=2)
#     plt.text(df[col].mean()*1.1, plt.ylim()[1]*0.9, 'Mean: {:.2f}'.format(df[col].mean()), fontdict=fontMean)
#     plt.axvline(df[col].median(), color='green', linestyle='dashed', linewidth=2)
#     plt.text(df[col].median(), plt.ylim()[1]*0.8, 'Median: {}'.format(df[col].median()), fontdict=fontMedian)
#     yVals = y.tolist()
#     patches[yVals.index(max(yVals))].set_color('y')
#     plt.show()

for col in CATEGORICAL_HEADERS:
	d = {}
	for i, r in df.iterrows():
		if r[col] in d:
			d[r[col]] += 1
		else:
			d[r[col]] = 1
	od = collections.OrderedDict(sorted(d.items()))
	values = sorted(df[col].value_counts())
	barlist = plt.bar(range(len(od)), list(od.values()), align='center', alpha=0.5)
	plt.xticks(range(len(od)), list(od.keys()))
	plt.ylabel('Frequency')
	plt.title(col)
	barlist[int(max(od.items(), key=operator.itemgetter(1))[0])].set_color('y')
	
	plt.axvline(df[col].median(), color='green', linestyle='dashed', linewidth=2)
	plt.text(df[col].median(), plt.ylim()[1]*0.8, 'Median: {}'.format(df[col].median()), fontdict=fontMedian)
	plt.show()
